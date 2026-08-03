# memory realtime monitor

> 9 nodes

## Key Concepts

- **.get_memory_usage()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_alerts()** (4 connections) — `server/realtime/memory_monitor.py`
- **.should_cleanup()** (3 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_stats()** (3 connections) — `server/realtime/memory_monitor.py`
- **Any** (2 connections)
- **Check if cleanup should be triggered.          Returns:             bool: True i** (1 connections) — `server/realtime/memory_monitor.py`
- **Get current memory usage as percentage.          Returns:             float: Mem** (1 connections) — `server/realtime/memory_monitor.py`
- **Get detailed memory statistics.          Returns:             dict: Memory stati** (1 connections) — `server/realtime/memory_monitor.py`
- **Get memory-related alerts based on current usage and connection statistics.** (1 connections) — `server/realtime/memory_monitor.py`

## Relationships

- [NATS Messaging](NATS_Messaging.md) (4 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*