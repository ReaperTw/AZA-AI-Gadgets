import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import subprocess
import sys
import tasks

spec = importlib.util.spec_from_file_location('usage', Path(__file__).with_name('usage.py'))
usage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(usage)


def write_log(path, session_id, *events, **header):
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [dict(type='session', id=session_id, timestamp='2026-10-28T00:00:00Z', **header), *events]
    path.write_text(''.join(json.dumps(r) + '\n' for r in rows), encoding='utf-8')


def call(identity, total='0.01', *, side=False):
    event = dict(provider='openai-codex', model='gpt-6-luna', responseId=identity,
                 usage=dict(input=100, output=20, cacheRead=50, cacheWrite=0))
    if total is not None:
        event['usage']['cost'] = {'total': total}
    if side:
        return dict(type='model_usage', id=identity, purpose='title', **event)
    return dict(type='message', id=identity, message=dict(role='assistant', **event,
                 content=[{'type': 'text', 'text': 'PRIVATE CONTENT MUST NOT BE COPIED'}]))


class Accounting(unittest.TestCase):
    def test_call_provenance_and_effective_effort(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'root.jsonl'
            write_log(root, 'root', dict(type='thinking_level_change', thinkingLevel='medium'),
                      call('a'), call('extra', side=True))
            record = usage.snapshot(root)
            self.assertEqual(record['calls'][0]['effort'], 'medium')
            self.assertEqual(record['calls'][1]['effort'], 'unknown')
            self.assertEqual(record['calls'][0]['session_id'], 'root')
            self.assertEqual(record['calls'][0]['event_id'], 'a')
    def test_children_side_calls_and_duplicate_events(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'root.jsonl'
            dispatch = dict(type='message', id='dispatch', message=dict(role='assistant', content=[
                dict(type='toolCall', name='task', arguments=dict(tasks=[dict(agent='omp-luna')]))]))
            write_log(root, 'root', call('a'), call('a'), call('title', '0.002', side=True), dispatch)
            write_log(root.with_suffix('') / 'worker.jsonl', 'child', call('b', '0.003'), parentSession='root')
            record = usage.snapshot(root)
            self.assertEqual(len(record['calls']), 3)
            self.assertEqual(record['dispatch_count'], 1)
            self.assertEqual(record['child_sessions'], 1)
            self.assertEqual(record['warnings'], ['root.jsonl: model call without usage'])
            self.assertNotIn('PRIVATE CONTENT', json.dumps(record))
            store = Path(tmp) / 'store'
            usage.save(record, store, outcome='accepted', kind='real', task_kind='parser')
            usage.save(usage.snapshot(root), store)
            self.assertEqual(len(list(store.glob('*.json'))), 1)
            group = usage.report(store)['groups'][0]
            self.assertEqual(group['recorded_api_cost_usd'], '0.015')
            self.assertEqual(group['main_cost_usd'], '0.012')
            self.assertEqual(group['child_cost_usd'], '0.003')
            self.assertEqual(group['outcomes']['accepted'], 1)
            self.assertEqual(group['tokens']['input'], 300)

    def test_missing_cost_is_not_invented_and_smoke_is_excluded(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'root.jsonl'
            store = Path(tmp) / 'store'
            write_log(root, 'root', call('a', None))
            record = usage.snapshot(root)
            self.assertIsNone(record['calls'][0]['recorded_api_cost_usd'])
            usage.save(record, store, kind='smoke')
            self.assertEqual(usage.report(store)['groups'], [])
            self.assertEqual(usage.report(store, True)['groups'][0]['missing_cost_calls'], 1)

    def test_partial_line_and_fork(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'root.jsonl'
            write_log(root, 'root', call('a'))
            with root.open('a') as f:
                f.write('{"partial":')
            self.assertIn('unfinished', usage.snapshot(root)['warnings'][0])
            with root.open('a') as f:
                f.write('\n')
            with self.assertRaises(ValueError):
                usage.snapshot(root)
            write_log(root, 'fork', call('a'), parentSession='original')
            with self.assertRaises(ValueError):
                usage.snapshot(root)

    def test_missing_child_evidence_and_cross_sample_dedup(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'root.jsonl'
            dispatch = dict(type='message', id='d', message=dict(role='assistant', usage={}, content=[
                dict(type='toolCall', name='task', arguments=dict(tasks=[dict(agent='omp-luna')]))]))
            write_log(root, 'one', call('same'), dispatch)
            record = usage.snapshot(root)
            self.assertTrue(any('missing or dispatch failed' in w for w in record['warnings']))
            store = Path(tmp) / 'store'
            usage.save(record, store)
            write_log(root, 'two', call('same'))
            usage.save(usage.snapshot(root), store)
            groups = usage.report(store)['groups']
            self.assertEqual(sum(usage.Decimal(g['recorded_api_cost_usd']) for g in groups), usage.Decimal('.01'))
            self.assertEqual(sum(g['shared_calls'] for g in groups), 1)

    def test_task_boundaries_acceptance_rework_and_children(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, store = Path(tmp) / 'root.jsonl', Path(tmp) / 'store'
            write_log(root, 'root', call('prior', '1'))
            task = tasks.begin(root, store, 'parser', 'independent-package', effort='medium')
            task_id = task['task_id']
            with self.assertRaises(ValueError):
                tasks.begin(root, store, 'other', 'small')
            def append(*events):
                with root.open('a', encoding='utf-8') as f:
                    for event in events:
                        f.write(json.dumps(event) + '\n')
            append(call('work', '.02'), call('side', '.003', side=True))
            child = root.with_suffix('') / 'worker.jsonl'
            write_log(child, 'worker', call('child', '.004'), parentSession='root')
            tasks.attach(root, store, task_id, child)
            with self.assertRaises(ValueError):
                tasks.finish(root, store, task_id, 'accepted', [])
            tasks.finish(root, store, task_id, 'failed', ['parser-edge:failed'])
            tasks.resume(root, store, task_id)
            append(call('repair', '.01'))
            result = tasks.finish(root, store, task_id, 'accepted', ['parser-edge:passed'])
            self.assertEqual({c['event_id'] for c in result['calls']}, {'work', 'side', 'child', 'repair'})
            self.assertEqual([a['outcome'] for a in result['attempts']], ['failed', 'accepted'])
            report = tasks.report(store)['tasks'][0]
            self.assertEqual(report['recorded_api_cost_usd'], '0.037')
            self.assertEqual(report['child_cost_usd'], '0.004')
            append(call('later', '9'))
            again = tasks.snapshot(root, result)
            self.assertEqual(again['calls'], result['calls'])
            next_task = tasks.begin(root, store, 'other', 'small')
            with self.assertRaises(ValueError):
                tasks.resume(root, store, task_id)
            with self.assertRaises(ValueError):
                tasks.attach(root, store, next_task['task_id'], child)

    def test_native_title_metadata_does_not_break_task_boundaries(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, store = Path(tmp) / 'root.jsonl', Path(tmp) / 'store'
            write_log(root, 'root', call('before'))
            original = root.read_text(encoding='utf-8')
            root.write_text(json.dumps({'type': 'title', 'title': 'first'}) + '\n' + original,
                            encoding='utf-8')
            record = tasks.begin(root, store, 'parser', 'small')
            root.write_text(json.dumps({'type': 'title', 'title': 'updated'}) + '\n' + original
                            + json.dumps(call('work', '.02')) + '\n', encoding='utf-8')
            result = tasks.finish(root, store, record['task_id'], 'accepted', ['native-boundary:passed'])
            self.assertEqual([c['event_id'] for c in result['calls']], ['work'])

    def test_task_refuses_rewritten_history_and_foreign_worker(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, store = Path(tmp) / 'root.jsonl', Path(tmp) / 'store'
            write_log(root, 'root', call('before'))
            task = tasks.begin(root, store, 'parser', 'small')
            foreign = Path(tmp) / 'foreign.jsonl'
            write_log(foreign, 'foreign', call('foreign'))
            with self.assertRaises(ValueError):
                tasks.attach(root, store, task['task_id'], foreign)
            write_log(root, 'root', call('replacement'))
            with self.assertRaises(ValueError):
                tasks.finish(root, store, task['task_id'], 'accepted', ['test:passed'])

    def test_incremental_scan_refreshes_changed_children_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            session_root, store = Path(tmp) / 'sessions', Path(tmp) / 'store'
            root = session_root / 'project' / 'root.jsonl'
            use = dict(type='message', message=dict(role='user', content=[
                dict(type='text', text='Use AZA-Omp-Orchestrate')]))
            write_log(root, 'root', use, call('main'))
            command = [sys.executable, str(Path(__file__).with_name('usage.py')),
                       '--data-dir', str(store), 'collect', '--scan', '--sessions-root', str(session_root)]
            subprocess.run(command, check=True, capture_output=True)
            snapshot = next(store.glob('*.json'))
            old = snapshot.read_bytes()
            subprocess.run(command, check=True, capture_output=True)
            self.assertEqual(snapshot.read_bytes(), old)
            child = root.with_suffix('') / 'child.jsonl'
            write_log(child, 'child', call('child', '.03'), parentSession='root')
            subprocess.run(command, check=True, capture_output=True)
            group = usage.report(store)['groups'][0]
            self.assertEqual(group['recorded_api_cost_usd'], '0.04')
            child.unlink()
            subprocess.run(command, check=True, capture_output=True)
            self.assertEqual(usage.report(store)['groups'][0]['recorded_api_cost_usd'], '0.01')


if __name__ == '__main__':
    unittest.main()
