# server realtime memory monitor as

> 8 nodes

## Key Concepts

- **.get_memory_alerts()** (5 connections) — `server/realtime/memory_monitor.py`
- **_as_int()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_usage()** (4 connections) — `server/realtime/memory_monitor.py`
- **.should_cleanup()** (3 connections) — `server/realtime/memory_monitor.py`
- **Coerce a duck-typed counter to int without using typing.Any.** (1 connections) — `server/realtime/memory_monitor.py`
- **Check if cleanup should be triggered. Returns: bool: True if cleanup should be…** (1 connections) — `server/realtime/memory_monitor.py`
- **Get current memory usage as percentage. Returns: float: Memory usage as a…** (1 connections) — `server/realtime/memory_monitor.py`
- **Get memory-related alerts based on current usage and connection statistics.…** (1 connections) — `server/realtime/memory_monitor.py`

## Relationships

- [server realtime memory monitor memorymonitor](server_realtime_memory_monitor_memorymonitor.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server realtime memory monitor collect](server_realtime_memory_monitor_collect.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*