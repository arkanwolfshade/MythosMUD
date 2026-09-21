# idle_sampler_enabled

> 10 nodes

## Key Concepts

- **idle_sampler_enabled()** (5 connections) — `server/realtime/memory_monitor.py`
- **test_idle_sampler_writes_jsonl_and_stops()** (5 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_collect_idle_sample_task_qualnames_attributes_by_coroutine()** (4 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_idle_sampler_disabled_by_default()** (4 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_idle_sampler_stays_stopped_when_disabled()** (4 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **asyncio** (4 connections)
- **MonkeyPatch** (4 connections)
- **Path** (2 connections)
- **Return True when the opt-in idle sampler env flag is set.** (1 connections) — `server/realtime/memory_monitor.py`
- **`task_qualnames` counts pending tasks by coroutine qualname, not `Task-N` names.** (1 connections) — `server/tests/unit/realtime/test_memory_monitor.py`

## Relationships

- [MemoryMonitor](MemoryMonitor.md) (9 shared connections)
- [._run_idle_sampler](_run_idle_sampler.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [collect_idle_memory_sample](collect_idle_memory_sample.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 22 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*