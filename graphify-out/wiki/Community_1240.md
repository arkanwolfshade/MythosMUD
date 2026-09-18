# Community 1240

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

- [Community 730](Community_730.md) (3 shared connections)
- [Community 891](Community_891.md) (1 shared connections)
- [Community 42](Community_42.md) (1 shared connections)
- [Community 107](Community_107.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*