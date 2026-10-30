"""Explicit task boundaries and evidence; never infer acceptance from conversation text."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import tempfile
import uuid

import usage


def persist(path, record):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent, delete=False) as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
        temporary = Path(f.name)
    temporary.replace(path)


def records(store):
    return [(p, json.loads(p.read_text(encoding='utf-8'))) for p in sorted((store / 'tasks').glob('*.json'))]


def header(rows):
    return next((r for r in rows if r.get('type') == 'session'), {})


def boundary(rows, index=None):
    index = len(rows) if index is None else index
    # Native auto-title metadata is mutable and is not billable event content.
    stable = [({'type': 'title'} if r.get('type') == 'title' else
               {k: r.get(k) for k in ('type', 'id', 'timestamp')} if r.get('type') == 'session' else r)
              for r in rows[:index]]
    digest = hashlib.sha256(json.dumps(stable, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    return {'index': index, 'prefix_sha256': digest,
            'event_id': rows[index - 1].get('id') if index else None}


def checked(rows, mark):
    if len(rows) < mark['index'] or boundary(rows, mark['index']) != mark:
        raise ValueError('Source history changed before a recorded boundary; attribution refused')
    return mark['index']


def root_rows(session):
    rows, warnings = usage.entries(session)
    source = header(rows)
    if not source.get('id'):
        raise ValueError('Missing root session header')
    if source.get('parentSession') or source.get('seanceSource'):
        raise ValueError('Use an original root session, not a fork or child')
    if warnings:
        raise ValueError('Finish the incomplete source entry before recording a boundary')
    return rows


def begin(session, store, task_kind, reason, kind='real', start_event=None, effort='unknown'):
    rows = root_rows(session)
    sid = header(rows)['id']
    existing = [r for _, r in records(store) if r['session_id'] == sid]
    if any(r['end'] is None for r in existing):
        raise ValueError('Close or resume the existing task; overlapping tasks are not allowed')
    start = len(rows)
    if start_event:
        matches = [i for i, row in enumerate(rows) if row.get('id') == start_event]
        if len(matches) != 1:
            raise ValueError('Start event must identify exactly one existing event')
        start = matches[0]
    if any(start < r['end']['index'] for r in existing):
        raise ValueError('Task range overlaps an existing task')
    task_id = str(uuid.uuid4())
    skill = Path(__file__).resolve().parent.parent
    hashes = {name: hashlib.sha256((skill / name).read_bytes()).hexdigest()
              for name in ('SKILL.md', 'cost-policy.md', 'scripts/usage.py', 'scripts/tasks.py')}
    record = {'schema': 1, 'task_id': task_id, 'session_id': sid,
              'unit': 'explicit_task', 'started_at': datetime.now(timezone.utc).isoformat(),
              'task_kind': task_kind, 'kind': kind, 'decision_reason': reason,
              'declared_effort': effort, 'skill_hashes': hashes,
              'start': boundary(rows, start), 'end': None, 'children': {},
              'outcome': 'unknown', 'evidence': [], 'attempts': []}
    persist(store / 'tasks' / (task_id + '.json'), record)
    return record


def load_task(session, store, task_id):
    rows = root_rows(session)
    matches = [(p, r) for p, r in records(store) if r['task_id'] == task_id]
    if len(matches) != 1 or matches[0][1]['session_id'] != header(rows)['id']:
        raise ValueError('Task does not belong to this root session')
    path, record = matches[0]
    checked(rows, record['start'])
    return path, record, rows


def attach(session, store, task_id, child):
    path, record, _ = load_task(session, store, task_id)
    if record['end'] is not None:
        raise ValueError('Resume the task before attaching a worker')
    # Native descendant directory is the ownership boundary; never accept arbitrary logs.
    if not child.resolve().is_relative_to(session.with_suffix('').resolve()):
        raise ValueError('Worker transcript is not a descendant of this root session')
    rows, warnings = usage.entries(child)
    sid = header(rows).get('id')
    if not sid or warnings:
        raise ValueError('Worker needs a valid, complete session header and log')
    if any(sid in r['children'] and r['task_id'] != task_id for _, r in records(store)):
        raise ValueError('Worker already belongs to another task; attribution refused')
    record['children'][sid] = None
    persist(path, record)
    return record


def snapshot(session, record):
    rows = root_rows(session)
    start = checked(rows, record['start'])
    end = checked(rows, record['end']) if record['end'] else len(rows)
    source = usage.snapshot(session)
    available = {}
    for child in session.with_suffix('').rglob('*.jsonl'):
        child_rows, warnings = usage.entries(child)
        if header(child_rows).get('id'):
            available[header(child_rows)['id']] = (child_rows, warnings)
    for sid, mark in record['children'].items():
        if sid not in available:
            raise ValueError('Attached worker transcript missing; previous record retained')
        if mark:
            checked(available[sid][0], mark)
    calls = []
    for call in source['calls']:
        if call['scope'] == 'main':
            include = start <= call['event_index'] < end
        else:
            sid = call['session_id']
            mark = record['children'].get(sid)
            include = sid in record['children'] and (mark is None or call['event_index'] < mark['index'])
        if include:
            calls.append(call)
    dispatches = sum(len(part.get('arguments', {}).get('tasks', [part.get('arguments', {})]))
                     for row in rows[start:end] for part in row.get('message', {}).get('content', [])
                     if isinstance(part, dict) and part.get('type') == 'toolCall' and part.get('name') == 'task')
    warnings = []
    if dispatches > len(record['children']):
        warnings.append('Some task dispatches have no explicitly attached worker transcript')
    if any(c['recorded_api_cost_usd'] is None for c in calls):
        warnings.append('Some model calls have no recorded cost')
    # Source warnings are conservative: retain them rather than claim a complete measurement.
    warnings.extend(source['warnings'])
    return dict(record, calls=calls, warnings=warnings,
                observed_models=sorted({c['model'] for c in calls}),
                strategy='delegated' if record['children'] else ('dispatch_without_child_evidence' if dispatches else 'inline'))


def finish(session, store, task_id, outcome, evidence):
    path, record, rows = load_task(session, store, task_id)
    if record['end'] is not None:
        raise ValueError('Task is already closed')
    if outcome == 'accepted' and not evidence:
        raise ValueError('Acceptance requires a non-sensitive verification reference')
    record['end'] = boundary(rows)
    record['outcome'], record['evidence'] = outcome, evidence
    for child in session.with_suffix('').rglob('*.jsonl'):
        child_rows, warnings = usage.entries(child)
        if header(child_rows).get('id') in record['children']:
            if warnings:
                raise ValueError('Attached worker has an incomplete final entry')
            record['children'][header(child_rows)['id']] = boundary(child_rows)
    record = snapshot(session, record)
    record['attempts'].append({'outcome': outcome, 'evidence': evidence, 'end': record['end']})
    persist(path, record)
    return record


def resume(session, store, task_id):
    path, record, rows = load_task(session, store, task_id)
    if record['end'] is None:
        raise ValueError('Task is already active')
    checked(rows, record['end'])
    # A resumed task cannot consume another task's work in the intervening range.
    if any(r['session_id'] == record['session_id'] and r['task_id'] != task_id
           and r['start']['index'] >= record['end']['index'] for _, r in records(store)):
        raise ValueError('Another task has started; cannot resume across its work')
    record.update(end=None, outcome='unknown', evidence=[], calls=[], warnings=[])
    record['children'] = dict.fromkeys(record['children'])
    persist(path, record)
    return record


def report(store, include_smoke=False):
    result = []
    for _, record in records(store):
        if record['kind'] == 'smoke' and not include_smoke:
            continue
        calls = record.get('calls', [])
        costs = {scope: sum((Decimal(c['recorded_api_cost_usd']) for c in calls
                            if c['scope'] == scope and c['recorded_api_cost_usd'] is not None), Decimal(0))
                 for scope in ('main', 'child')}
        result.append({k: v for k, v in record.items() if k != 'calls'} | {
            'recorded_api_cost_usd': str(sum(costs.values())) if record['end'] else None,
            'main_cost_usd': str(costs['main']) if record['end'] else None,
            'child_cost_usd': str(costs['child']) if record['end'] else None,
            'comparable_candidate': bool(record['end'] and record['kind'] == 'real'
                and record['outcome'] != 'unknown' and calls and not record.get('warnings'))})
    return {'tasks': result, 'note': 'Explicit bounded tasks only. Open tasks have no final totals. Candidates still require matched scope, effort and acceptance; no causal savings claim.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path, default=usage.DEFAULT_STORE)
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('begin', 'attach', 'end', 'resume'):
        cmd = commands.add_parser(name)
        cmd.add_argument('session', type=Path)
        if name == 'begin':
            cmd.add_argument('--task-kind', required=True)
            cmd.add_argument('--reason', required=True, help='Short non-sensitive dispatch decision code')
            cmd.add_argument('--kind', choices=['real', 'smoke', 'mixed'], default='real')
            cmd.add_argument('--start-event')
            cmd.add_argument('--effort', default='unknown', help='Declared setting, not verified runtime evidence')
        else:
            cmd.add_argument('--task-id', required=True)
        if name == 'attach':
            cmd.add_argument('--child-session', type=Path, required=True)
        if name == 'end':
            cmd.add_argument('--outcome', choices=['accepted', 'blocked', 'failed', 'unknown'], required=True)
            cmd.add_argument('--evidence', action='append', default=[], help='Non-sensitive check ID/result, never raw logs')
    args = parser.parse_args()
    try:
        if args.command == 'begin':
            record = begin(args.session, args.data_dir, args.task_kind, args.reason, args.kind, args.start_event, args.effort)
        elif args.command == 'attach':
            record = attach(args.session, args.data_dir, args.task_id, args.child_session)
        elif args.command == 'resume':
            record = resume(args.session, args.data_dir, args.task_id)
        else:
            record = finish(args.session, args.data_dir, args.task_id, args.outcome, args.evidence)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    print(json.dumps({k: record[k] for k in ('task_id', 'session_id', 'outcome')}, indent=2))


if __name__ == '__main__':
    main()
