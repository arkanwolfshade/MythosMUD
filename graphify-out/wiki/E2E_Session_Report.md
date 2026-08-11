# E2E Session Report

> 30 nodes

## Key Concepts

- **get_global_tracked_manager()** (18 connections) — `server/app/tracked_task_manager.py`
- **PeriodicOrphanAuditor** (9 connections) — `server/app/memory_lifespan_coordinator.py`
- **.get_memory_status_report()** (6 connections) — `server/app/memory_cleanup_service.py`
- **.managed_task_cleanup()** (4 connections) — `server/app/memory_cleanup_service.py`
- **.schedule_periodic_auditing()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._background_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._do_full_cleanup_audit()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **.force_single_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._get_current_memory_usage()** (3 connections) — `server/app/memory_cleanup_service.py`
- **._get_active_task_count()** (3 connections) — `server/app/memory_cleanup_service.py`
- **.__init__()** (3 connections) — `server/app/memory_lifespan_coordinator.py`
- **create_lifespan_memory_service()** (3 connections) — `server/app/memory_lifespan_coordinator.py`
- **memory_leak_prevention_channel_start_session()** (3 connections) — `server/app/tracked_task_manager.py`
- **.stop_audit_scheduler()** (2 connections) — `server/app/memory_lifespan_coordinator.py`
- **Any** (1 connections)
- **Get current memory usage in bytes for this process.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Get count of active tasks in the current event loop.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Generate status report for diagnostic monitoring.          Returns:** (1 connections) — `server/app/memory_cleanup_service.py`
- **Runtime detection and cleanup of orphaned tasks based on memory thresholds.** (1 connections) — `server/app/memory_cleanup_service.py`
- **Any** (1 connections)
- **Periodic background auditor that investigates orphanage patterns and memory cond** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Initialize the periodic orphan auditor.          Args:             check_interva** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Start the background auditing scheduler responsible for identifying orphan vecto** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Primary background cycle consuming auditor implementation.          Executes per** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Core capability for granular investigation cycles.          Repeated universal a** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- *... and 5 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (12 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (4 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (1 shared connections)
- [Validate Calendar](Validate_Calendar.md) (1 shared connections)
- [Typography Layout Spec](Typography_Layout_Spec.md) (1 shared connections)
- [Components Panels Monitoringpaneltestfixtures](Components_Panels_Monitoringpaneltestfixtures.md) (1 shared connections)

## Source Files

- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/tracked_task_manager.py`

## Audit Trail

- EXTRACTED: 85 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*