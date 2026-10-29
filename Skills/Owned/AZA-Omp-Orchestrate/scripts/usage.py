"""Private metadata-only snapshots of OMP root sessions and their children."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import tempfile

DEFAULT_STORE = Path.home() / '.omp' / 'agent' / 'orchestration-data'
DEFAULT_SESSIONS = Path.home() / '.omp' / 'agent' / 'sessions'
TOKENS = ('input', 'output', 'cacheRead', 'cacheWrite')


def entries(path):
    data = path.read_bytes()
    lines = data.splitlines()
    rows, warnings = [], []
    for index, line in enumerate(lines):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except (ValueError, UnicodeDecodeError):
            if index == len(lines) - 1 and not data.endswith(b'\n'):
                warnings.append(f'{path.name}: unfinished final entry omitted')
            else:
                raise ValueError(f'{path}: malformed entry {index + 1}') from None
    return rows, warnings


def relevant(rows):
    for row in rows:
        msg = row.get('message', {})
        for part in msg.get('content', []) if isinstance(msg.get('content'), list) else []:
            if part.get('type') == 'text' and msg.get('role') == 'user' and ('AZA-Omp-Orchestrate' in part.get('text', '') or 'omp-orchestrate' in part.get('text', '')):
                return True
            if part.get('type') == 'toolCall' and part.get('name') == 'read':
                if 'AZA-Omp-Orchestrate' in str(part.get('arguments', {}).get('path', '')) or 'omp-orchestrate' in str(part.get('arguments', {}).get('path', '')):
                    return True
    return False


def snapshot(path):
    root, warnings = entries(path)
    header = next((r for r in root if r.get('type') == 'session'), None)
    if not header or not header.get('id'):
        raise ValueError(f'{path}: missing session header')
    if header.get('parentSession') or header.get('seanceSource'):
        raise ValueError(f'{path}: forked/imported lineage requires separate accounting; not a clean trial')
    children = sorted(path.with_suffix('').rglob('*.jsonl')) if path.with_suffix('').is_dir() else []
    calls, seen, agents, main_models = [], set(), Counter(), set()
    dispatches = 0
    for file in [path, *children]:
        rows, extra = (root, []) if file == path else entries(file)
        warnings.extend(extra)
        for row in rows:
            msg = row.get('message', {})
            if msg.get('role') == 'assistant':
                if file == path and msg.get('model'):
                    main_models.add(f"{msg.get('provider', 'unknown')}/{msg['model']}")
                for part in msg.get('content', []) if isinstance(msg.get('content'), list) else []:
                    if part.get('type') == 'toolCall' and part.get('name') == 'task':
                        args = part.get('arguments', {})
                        tasks = args.get('tasks', [args])
                        dispatches += len(tasks)
                        agents.update(t.get('agent', 'task') for t in tasks)
            if row.get('type') == 'model_usage':
                event = row
                purpose = row.get('purpose', 'side-call')
            elif row.get('type') == 'message' and msg.get('role') == 'assistant':
                event = msg
                purpose = 'conversation'
            else:
                continue
            usage = event.get('usage')
            if not isinstance(usage, dict):
                warnings.append(f'{file.name}: model call without usage')
                continue
            provider, model = event.get('provider', 'unknown'), event.get('model', 'unknown')
            # Response IDs prevent repeated persisted messages/fork copies double charging.
            identity = event.get('responseId') or row.get('id')
            if not identity:
                raise ValueError(f'{file}: usage entry has no stable identity')
            key = hashlib.sha256(f'{provider}|{model}|{identity}'.encode()).hexdigest()
            if key in seen:
                continue
            seen.add(key)
            cost = usage.get('cost', {}).get('total')
            if cost is not None and (not Decimal(str(cost)).is_finite() or Decimal(str(cost)) < 0):
                raise ValueError(f'{file}: invalid recorded cost')
            calls.append({'key': key, 'model': f'{provider}/{model}',
                          'scope': 'main' if file == path else 'child', 'purpose': purpose,
                          'tokens': {k: usage.get(k) for k in TOKENS},
                          'recorded_api_cost_usd': str(cost) if cost is not None else None})
    if dispatches > len(children):
        warnings.append('Some dispatched child transcripts are missing or dispatch failed; child costs may be incomplete')
    return {'schema': 1, 'session_id': header['id'], 'started_at': header.get('timestamp'),
            'collected_at': datetime.now(timezone.utc).isoformat(),
            'unit': 'whole_root_session_not_individual_task',
            'strategy': 'delegated' if children else ('dispatch_without_child_evidence' if dispatches else 'inline'),
            'main_models': sorted(main_models), 'child_sessions': len(children),
            'dispatch_count': dispatches, 'selected_agents': dict(agents),
            'warnings': warnings, 'calls': calls}


def save(record, store, *, outcome=None, kind=None, task_kind=None):
    store.mkdir(parents=True, exist_ok=True)
    name = hashlib.sha256(record['session_id'].encode()).hexdigest() + '.json'
    target = store / name
    old = json.loads(target.read_text(encoding='utf-8')) if target.exists() else {}
    for key, value, default in [('outcome', outcome, 'unknown'), ('kind', kind, 'unclassified'),
                                ('task_kind', task_kind, 'unclassified')]:
        record[key] = value if value is not None else old.get(key, default)
    # One file/session; recollection replaces the snapshot, never appends usage twice.
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=store, delete=False) as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
        temporary = Path(f.name)
    temporary.replace(target)
    return target


def report(store, include_smoke=False):
    groups, seen = {}, set()
    for path in sorted(store.glob('*.json')):
        record = json.loads(path.read_text(encoding='utf-8'))
        if record.get('schema') != 1:
            raise ValueError(f'{path}: unsupported schema')
        if not include_smoke and record['kind'] == 'smoke':
            continue
        key = (record['kind'], record['task_kind'], ','.join(record['main_models']), record['strategy'])
        group = groups.setdefault(key, {'samples': 0, 'outcomes': Counter(), 'cost': Decimal(0),
                                        'missing_cost_calls': 0, 'shared_calls': 0, 'warnings': 0,
                                        'main_cost': Decimal(0), 'child_cost': Decimal(0),
                                        'tokens': Counter(), 'missing_token_fields': 0})
        group['samples'] += 1
        group['outcomes'][record['outcome']] += 1
        group['warnings'] += len(record['warnings'])
        for call in record['calls']:
            if call['key'] in seen:
                group['shared_calls'] += 1
                continue
            seen.add(call['key'])
            group['tokens'].update({k: v for k, v in call['tokens'].items() if v is not None})
            group['missing_token_fields'] += sum(v is None for v in call['tokens'].values())
            if call['recorded_api_cost_usd'] is None:
                group['missing_cost_calls'] += 1
            else:
                cost = Decimal(call['recorded_api_cost_usd'])
                group['cost'] += cost
                group[call['scope'] + '_cost'] += cost
    result = []
    for key, group in groups.items():
        known_cost = str(group.pop('cost'))
        main_cost, child_cost = str(group.pop('main_cost')), str(group.pop('child_cost'))
        result.append(dict(zip(('kind', 'task_kind', 'main_models', 'strategy'), key), **group,
                           recorded_api_cost_usd=known_cost, main_cost_usd=main_cost, child_cost_usd=child_cost))
    return {'groups': result, 'note': 'Recorded API estimates, not subscription charges. Missing/shared calls or mixed-task sessions limit comparisons. Different tasks do not establish causal savings; include matched Sol-only trials and acceptance outcomes.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path, default=DEFAULT_STORE)
    commands = parser.add_subparsers(dest='command', required=True)
    collect = commands.add_parser('collect')
    collect.add_argument('session', nargs='?', type=Path)
    collect.add_argument('--scan', action='store_true', help='Refresh relevant top-level sessions; does not infer acceptance')
    collect.add_argument('--sessions-root', type=Path, default=DEFAULT_SESSIONS)
    collect.add_argument('--outcome', choices=['accepted', 'blocked', 'failed', 'unknown'])
    collect.add_argument('--kind', choices=['real', 'smoke', 'mixed', 'unclassified'])
    collect.add_argument('--task-kind', help='Use a short non-sensitive comparison category, not a prompt')
    summary = commands.add_parser('summary')
    summary.add_argument('--include-smoke', action='store_true')
    args = parser.parse_args()
    if args.command == 'summary':
        print(json.dumps(report(args.data_dir, args.include_smoke), ensure_ascii=False, indent=2))
        return
    if bool(args.session) == args.scan:
        parser.error('provide one session path OR --scan')
    if args.scan and any((args.outcome, args.kind, args.task_kind)):
        parser.error('label individual sessions, not all scanned sessions')
    paths = sorted(args.sessions_root.glob('*/*.jsonl')) if args.scan else [args.session]
    saved = 0
    for path in paths:
        try:
            if args.scan:
                rows, _ = entries(path)
                if not relevant(rows):
                    continue
            record = snapshot(path)
            save(record, args.data_dir, outcome=args.outcome, kind=args.kind, task_kind=args.task_kind)
            saved += 1
        except (ValueError, OSError) as exc:
            if not args.scan:
                raise
            print(f'SKIPPED {path.name}: {exc}')
    print(f'Saved/refreshed {saved} session snapshots in {args.data_dir}')


if __name__ == '__main__':
    main()
