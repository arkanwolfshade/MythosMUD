# Memory Threshold Monitor

> 36 nodes · cohesion 0.07

## Key Concepts

- **MemoryThresholdMonitor** (10 connections) — `server/app/memory_cleanup_service.py`
- **PeriodicOrphanAuditor** (9 connections) — `server/app/memory_lifespan_coordinator.py`
- **create_memory_cleanup_monitor()** (6 connections) — `server/app/memory_cleanup_service.py`
- **.get_memory_status_report()** (6 connections) — `server/app/memory_cleanup_service.py`
- **.schedule_periodic_auditing()** (5 connections) — `server/app/memory_lifespan_coordinator.py`
- **get_managed_task_cleanup_implementation_for_task_four_spec_compliance()** (4 connections) — `server/app/memory_cleanup_service.py`
- **.managed_task_cleanup()** (4 connections) — `server/app/memory_cleanup_service.py`
- **._background_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._do_full_cleanup_audit()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **.force_single_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._flush_memory_indexes_cache()** (3 connections) — `server/app/memory_cleanup_service.py`
- **._get_active_task_count()** (3 connections) — `server/app/memory_cleanup_service.py`
- **._get_current_memory_usage()** (3 connections) — `server/app/memory_cleanup_service.py`
- **.__init__()** (3 connections) — `server/app/memory_cleanup_service.py`
- **create_lifespan_memory_service()** (3 connections) — `server/app/memory_lifespan_coordinator.py`
- **.__init__()** (3 connections) — `server/app/memory_lifespan_coordinator.py`
- **.stop_audit_scheduler()** (2 connections) — `server/app/memory_lifespan_coordinator.py`
- **Generate status report for diagnostic monitoring.          Returns:** (1 connections) — `server/app/memory_cleanup_service.py`
- **Runtime detection and cleanup of orphaned tasks based on memory thresholds.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Create an instance of the MemoryThresholdMonitor with user-specified parameters.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Factory function returning implementation conforming to Task 4.3 Specified Inter** (1 connections) — `server/app/memory_cleanup_service.py`
- **Runtime monitor for detecting memory threshold violations requiring cleanup.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Initialize the memory threshold monitoring service.          Args:             m** (1 connections) — `server/app/memory_cleanup_service.py`
- **Get current memory usage in bytes for this process.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Get count of active tasks in the current event loop.** (1 connections) — `server/app/memory_cleanup_service.py`
- *... and 11 more nodes in this community*

## Relationships

- [[NPC Admin API]] (10 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`

## Audit Trail

- EXTRACTED: 94 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
