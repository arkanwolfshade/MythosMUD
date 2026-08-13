# .get_memory_alerts

> 9 nodes

## Key Concepts

- **.get_memory_alerts()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_usage()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_stats()** (3 connections) — `server/realtime/memory_monitor.py`
- **.should_cleanup()** (3 connections) — `server/realtime/memory_monitor.py`
- **Any** (2 connections)
- **Get memory-related alerts based on current usage and connection statistics.…** (1 connections) — `server/realtime/memory_monitor.py`
- **Check if cleanup should be triggered. Returns: bool: True if cleanup should be…** (1 connections) — `server/realtime/memory_monitor.py`
- **Get current memory usage as percentage. Returns: float: Memory usage as a…** (1 connections) — `server/realtime/memory_monitor.py`
- **Get detailed memory statistics. Returns: dict: Memory statistics including RSS,…** (1 connections) — `server/realtime/memory_monitor.py`

## Relationships

- [get_logger](get_logger.md) (4 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*