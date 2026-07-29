# memory lifespan coordinator

> 30 nodes

## Key Concepts

- **get_global_tracked_manager()** (16 connections) — `server/app/tracked_task_manager.py`
- **tracked_task_manager.py** (14 connections) — `server/app/tracked_task_manager.py`
- **memory_lifespan_coordinator.py** (10 connections) — `server/app/memory_lifespan_coordinator.py`
- **PeriodicOrphanAuditor** (9 connections) — `server/app/memory_lifespan_coordinator.py`
- **game_tick_service.py** (9 connections) — `server/services/game_tick_service.py`
- **.schedule_periodic_auditing()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._background_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._do_full_cleanup_audit()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **.force_single_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **create_lifespan_memory_service()** (3 connections) — `server/app/memory_lifespan_coordinator.py`
- **memory_leak_prevention_channel_start_session()** (3 connections) — `server/app/tracked_task_manager.py`
- **.stop_audit_scheduler()** (2 connections) — `server/app/memory_lifespan_coordinator.py`
- **reset_global_tracked_manager()** (2 connections) — `server/app/tracked_task_manager.py`
- **patch_asyncio_create_task_with_tracking()** (2 connections) — `server/app/tracked_task_manager.py`
- **Any** (1 connections)
- **Memory Lifespan Coordinator - Centralized Periodic Auditing for Orphaned Task Pr** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Periodic background auditor that investigates orphanage patterns and memory cond** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Start the background auditing scheduler responsible for identifying orphan vecto** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Primary background cycle consuming auditor implementation.          Executes per** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Core capability for granular investigation cycles.          Repeated universal a** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Execute a single investigation loop synchronously producing operator summary.** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Stop the periodic orphan auditor background enforcement.** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Create a centralized memory operations coordinator instance targeted for     app** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **# TODO: Improve graceful shutdown with early cancellation  # pylint: disable=fix** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Global TrackedTaskManager for Memory Leak Prevention Infrastructure.  This modul** (1 connections) — `server/app/tracked_task_manager.py`
- *... and 5 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (9 shared connections)
- [Any](Any.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [NPCEventHandler](NPCEventHandler.md) (3 shared connections)
- [event publisher()](event_publisher%28%29.md) (2 shared connections)
- [GameTickService](GameTickService.md) (2 shared connections)
- [task registry](task_registry.md) (1 shared connections)
- [Cancel lifecycle/critical tasks first (Phase](Cancel_lifecycle-critical_tasks_first_%28Phase.md) (1 shared connections)
- [.start()](start%28%29.md) (1 shared connections)

## Source Files

- `server/app/memory_lifespan_coordinator.py`
- `server/app/tracked_task_manager.py`
- `server/services/game_tick_service.py`

## Audit Trail

- EXTRACTED: 100 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*