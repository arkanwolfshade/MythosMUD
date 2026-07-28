# Server App (5)

> 19 nodes

## Key Concepts

- **MemoryThresholdMonitor** (10 connections) — `server/app/memory_cleanup_service.py`
- **.get_memory_status_report()** (6 connections) — `server/app/memory_cleanup_service.py`
- **create_memory_cleanup_monitor()** (6 connections) — `server/app/memory_cleanup_service.py`
- **.managed_task_cleanup()** (4 connections) — `server/app/memory_cleanup_service.py`
- **get_managed_task_cleanup_implementation_for_task_four_spec_compliance()** (4 connections) — `server/app/memory_cleanup_service.py`
- **.__init__()** (3 connections) — `server/app/memory_cleanup_service.py`
- **._get_current_memory_usage()** (3 connections) — `server/app/memory_cleanup_service.py`
- **._get_active_task_count()** (3 connections) — `server/app/memory_cleanup_service.py`
- **._flush_memory_indexes_cache()** (3 connections) — `server/app/memory_cleanup_service.py`
- **Any** (1 connections)
- **Runtime monitor for detecting memory threshold violations requiring cleanup.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Initialize the memory threshold monitoring service.          Args:             m** (1 connections) — `server/app/memory_cleanup_service.py`
- **Get current memory usage in bytes for this process.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Get count of active tasks in the current event loop.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Flush persistent in-memory indexes associated with cached memory residency.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Generate status report for diagnostic monitoring.          Returns:** (1 connections) — `server/app/memory_cleanup_service.py`
- **Runtime detection and cleanup of orphaned tasks based on memory thresholds.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Create an instance of the MemoryThresholdMonitor with user-specified parameters.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Factory function returning implementation conforming to Task 4.3 Specified Inter** (1 connections) — `server/app/memory_cleanup_service.py`

## Relationships

- [Server Commands](Server_Commands.md) (4 shared connections)
- [Server Realtime (19)](Server_Realtime_%2819%29.md) (2 shared connections)

## Source Files

- `server/app/memory_cleanup_service.py`

## Audit Trail

- EXTRACTED: 52 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*