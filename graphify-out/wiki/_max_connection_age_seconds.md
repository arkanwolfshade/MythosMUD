# _max_connection_age_seconds

> 7 nodes

## Key Concepts

- **_max_connection_age_seconds()** (7 connections) — `server/realtime/memory_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/memory_monitor.py`
- **test_max_connection_age_default()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_max_connection_age_e2e()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_max_connection_age_local()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **Connection age threshold (seconds). Higher in e2e/local to avoid mid-run drops.** (1 connections) — `server/realtime/memory_monitor.py`
- **Initialize the memory monitor with default settings.** (1 connections) — `server/realtime/memory_monitor.py`

## Relationships

- [MemoryMonitor](MemoryMonitor.md) (5 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*