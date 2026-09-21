# _task_qualname

> 9 nodes

## Key Concepts

- **_task_qualname()** (6 connections) — `server/realtime/memory_monitor.py`
- **_FakeTask** (4 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_task_qualname_falls_back_when_coro_has_no_qualname()** (4 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **.get_coro()** (3 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **Task** (1 connections)
- **Return the coroutine qualname a task was created from, for leak attribution.…** (1 connections) — `server/realtime/memory_monitor.py`
- **Stand-in for asyncio.Task whose coroutine has no __qualname__ (e.g. a plain…** (1 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **Return a coroutine-like value with no __qualname__ attribute.** (1 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **`_task_qualname` degrades to the coroutine's type name rather than raising.** (1 connections) — `server/tests/unit/realtime/test_memory_monitor.py`

## Relationships

- [MemoryMonitor](MemoryMonitor.md) (3 shared connections)
- [collect_idle_memory_sample](collect_idle_memory_sample.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*