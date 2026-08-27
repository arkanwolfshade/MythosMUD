# get_global_tracked_manager

> 26 nodes

## Key Concepts

- **get_global_tracked_manager()** (19 connections) — `server/app/tracked_task_manager.py`
- **tracked_task_manager.py** (16 connections) — `server/app/tracked_task_manager.py`
- **memory_cleanup_service.py** (12 connections) — `server/app/memory_cleanup_service.py`
- **memory_lifespan_coordinator.py** (12 connections) — `server/app/memory_lifespan_coordinator.py`
- **game_tick_service.py** (10 connections) — `server/services/game_tick_service.py`
- **create_memory_cleanup_monitor()** (8 connections) — `server/app/memory_cleanup_service.py`
- **get_managed_task_cleanup_implementation_for_task_four_spec_compliance()** (6 connections) — `server/app/memory_cleanup_service.py`
- **memory_leak_prevention_channel_start_session()** (5 connections) — `server/app/tracked_task_manager.py`
- **.force_single_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **reset_global_tracked_manager()** (4 connections) — `server/app/tracked_task_manager.py`
- **.__init__()** (3 connections) — `server/app/memory_lifespan_coordinator.py`
- **reset_global()** (3 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **Any** (1 connections)
- **fixture** (1 connections)
- **Managed Task Cleanup Service - Runtime Detection for Memory Threshold…** (1 connections) — `server/app/memory_cleanup_service.py`
- **Create an instance of the MemoryThresholdMonitor with user-specified…** (1 connections) — `server/app/memory_cleanup_service.py`
- **Factory function returning implementation conforming to Task 4.3 Specified…** (1 connections) — `server/app/memory_cleanup_service.py`
- **Memory Lifespan Coordinator - Centralized Periodic Auditing for Orphaned Task…** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Execute a single investigation loop synchronously producing operator summary.…** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **# TODO: Improve graceful shutdown with early cancellation # pylint:…** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Initialize the periodic orphan auditor. Args: check_interval_seconds: Seconds…** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Global TrackedTaskManager for Memory Leak Prevention Infrastructure. This…** (1 connections) — `server/app/tracked_task_manager.py`
- **Access the singleton global TrackedTaskManager for usage across the server.…** (1 connections) — `server/app/tracked_task_manager.py`
- **Reset the global tracked manager for testing.** (1 connections) — `server/app/tracked_task_manager.py`
- **Initialize session-local memory leak prevention coordinator to enable long-…** (1 connections) — `server/app/tracked_task_manager.py`
- *... and 1 more nodes in this community*

## Relationships

- [TrackedTaskManager](TrackedTaskManager.md) (10 shared connections)
- [MemoryThresholdMonitor](MemoryThresholdMonitor.md) (9 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [PeriodicOrphanAuditor](PeriodicOrphanAuditor.md) (7 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (4 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [TaskRegistry](TaskRegistry.md) (2 shared connections)
- [GameTickService](GameTickService.md) (2 shared connections)
- [.start](start.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)
- [EventPublisher](EventPublisher.md) (1 shared connections)

## Source Files

- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/tracked_task_manager.py`
- `server/services/game_tick_service.py`
- `server/tests/unit/app/test_tracked_task_manager.py`

## Audit Trail

- EXTRACTED: 83 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*