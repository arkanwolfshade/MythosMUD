# Server Realtime (78)

> 19 nodes

## Key Concepts

- **MemoryMonitor** (14 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_usage()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_alerts()** (4 connections) — `server/realtime/memory_monitor.py`
- **_max_connection_age_seconds()** (3 connections) — `server/realtime/memory_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/memory_monitor.py`
- **.should_cleanup()** (3 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_stats()** (3 connections) — `server/realtime/memory_monitor.py`
- **Any** (2 connections)
- **.update_cleanup_time()** (2 connections) — `server/realtime/memory_monitor.py`
- **.force_garbage_collection()** (2 connections) — `server/realtime/memory_monitor.py`
- **Connection age threshold (seconds). Higher in e2e/local to avoid mid-run drops.** (1 connections) — `server/realtime/memory_monitor.py`
- **Monitor memory usage and trigger cleanup when needed.      This class provides m** (1 connections) — `server/realtime/memory_monitor.py`
- **Initialize the memory monitor with default settings.** (1 connections) — `server/realtime/memory_monitor.py`
- **Check if cleanup should be triggered.          Returns:             bool: True i** (1 connections) — `server/realtime/memory_monitor.py`
- **Get current memory usage as percentage.          Returns:             float: Mem** (1 connections) — `server/realtime/memory_monitor.py`
- **Get detailed memory statistics.          Returns:             dict: Memory stati** (1 connections) — `server/realtime/memory_monitor.py`
- **Get memory-related alerts based on current usage and connection statistics.** (1 connections) — `server/realtime/memory_monitor.py`
- **Update the last cleanup time to the current time.** (1 connections) — `server/realtime/memory_monitor.py`
- **Force garbage collection to free memory.** (1 connections) — `server/realtime/memory_monitor.py`

## Relationships

- [Server Commands](Server_Commands.md) (4 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (1 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (1 shared connections)
- [Server Realtime (64)](Server_Realtime_%2864%29.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`

## Audit Trail

- EXTRACTED: 48 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*