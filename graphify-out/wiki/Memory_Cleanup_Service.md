# Memory Cleanup Service

> 13 nodes

## Key Concepts

- **.get_memory_status_report()** (6 connections) — `server/app/memory_cleanup_service.py`
- **MemoryStatusReport** (4 connections) — `server/app/memory_cleanup_service.py`
- **._get_current_memory_usage()** (4 connections) — `server/app/memory_cleanup_service.py`
- **._get_active_task_count()** (3 connections) — `server/app/memory_cleanup_service.py`
- **.managed_task_cleanup()** (3 connections) — `server/app/memory_cleanup_service.py`
- **_rss_bytes_from_memory_info()** (3 connections) — `server/app/memory_cleanup_service.py`
- **TypedDict** (1 connections)
- **Generate status report for diagnostic monitoring. Returns: Dictionary…** (1 connections) — `server/app/memory_cleanup_service.py`
- **Runtime detection and cleanup of orphaned tasks based on memory thresholds.…** (1 connections) — `server/app/memory_cleanup_service.py`
- **Narrow psutil memory_info().rss for basedpyright (stubs disagree with mypy's…** (1 connections) — `server/app/memory_cleanup_service.py`
- **Diagnostic payload from MemoryThresholdMonitor.get_memory_status_report.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Get current memory usage in bytes for this process.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Get count of active tasks in the current event loop.** (1 connections) — `server/app/memory_cleanup_service.py`

## Relationships

- [Test Memory Cleanup Service](Test_Memory_Cleanup_Service.md) (4 shared connections)
- [Memory Lifespan Coordinator](Memory_Lifespan_Coordinator.md) (2 shared connections)

## Source Files

- `server/app/memory_cleanup_service.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*