# Combat Disconnect Bug

> 19 nodes · cohesion 0.12

## Key Concepts

- **MemoryMonitor** (14 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_alerts()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_usage()** (4 connections) — `server/realtime/memory_monitor.py`
- **_max_connection_age_seconds()** (3 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_stats()** (3 connections) — `server/realtime/memory_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/memory_monitor.py`
- **.should_cleanup()** (3 connections) — `server/realtime/memory_monitor.py`
- **.force_garbage_collection()** (2 connections) — `server/realtime/memory_monitor.py`
- **.update_cleanup_time()** (2 connections) — `server/realtime/memory_monitor.py`
- **Any** (2 connections)
- **Get memory-related alerts based on current usage and connection statistics.** (1 connections) — `server/realtime/memory_monitor.py`
- **Update the last cleanup time to the current time.** (1 connections) — `server/realtime/memory_monitor.py`
- **Force garbage collection to free memory.** (1 connections) — `server/realtime/memory_monitor.py`
- **Connection age threshold (seconds). Higher in e2e/local to avoid mid-run drops.** (1 connections) — `server/realtime/memory_monitor.py`
- **Monitor memory usage and trigger cleanup when needed.      This class provides m** (1 connections) — `server/realtime/memory_monitor.py`
- **Initialize the memory monitor with default settings.** (1 connections) — `server/realtime/memory_monitor.py`
- **Check if cleanup should be triggered.          Returns:             bool: True i** (1 connections) — `server/realtime/memory_monitor.py`
- **Get current memory usage as percentage.          Returns:             float: Mem** (1 connections) — `server/realtime/memory_monitor.py`
- **Get detailed memory statistics.          Returns:             dict: Memory stati** (1 connections) — `server/realtime/memory_monitor.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (1 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)
- [Whisper Reply Command Tests](Whisper_Reply_Command_Tests.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`

## Audit Trail

- EXTRACTED: 48 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*