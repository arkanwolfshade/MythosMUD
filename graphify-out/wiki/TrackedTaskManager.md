# TrackedTaskManager

> 45 nodes

## Key Concepts

- **TrackedTaskManager** (22 connections) — `server/app/tracked_task_manager.py`
- **test_tracked_task_manager.py** (20 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **get_global_tracked_manager()** (19 connections) — `server/app/tracked_task_manager.py`
- **tracked_task_manager.py** (16 connections) — `server/app/tracked_task_manager.py`
- **game_tick_service.py** (10 connections) — `server/services/game_tick_service.py`
- **asyncio** (8 connections)
- **memory_leak_prevention_channel_start_session()** (5 connections) — `server/app/tracked_task_manager.py`
- **.create_supervised_task()** (5 connections) — `server/app/tracked_task_manager.py`
- **.create_tracked_task()** (5 connections) — `server/app/tracked_task_manager.py`
- **patch_asyncio_create_task_with_tracking()** (4 connections) — `server/app/tracked_task_manager.py`
- **reset_global_tracked_manager()** (4 connections) — `server/app/tracked_task_manager.py`
- **.__init__()** (3 connections) — `server/app/tracked_task_manager.py`
- **.set_task_registry()** (3 connections) — `server/app/tracked_task_manager.py`
- **reset_global()** (3 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_audit_orphans_counts_untracked()** (3 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_cleanup_orphaned_tasks_cancels_running()** (3 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_create_supervised_task_completes()** (3 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_create_tracked_task_registry_failure_falls_back()** (3 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_create_tracked_task_runs_coro()** (3 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_create_tracked_task_with_registry()** (3 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_patch_asyncio_create_task_with_tracking()** (3 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **.actively_tracked_task_count()** (2 connections) — `server/app/tracked_task_manager.py`
- **.audit_orphans()** (2 connections) — `server/app/tracked_task_manager.py`
- **.cleanup_orphaned_tasks()** (2 connections) — `server/app/tracked_task_manager.py`
- **test_global_manager_singleton()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- *... and 20 more nodes in this community*

## Relationships

- [TaskRegistry](TaskRegistry.md) (5 shared connections)
- [PeriodicOrphanAuditor](PeriodicOrphanAuditor.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [MemoryThresholdMonitor](MemoryThresholdMonitor.md) (3 shared connections)
- [GameTickService](GameTickService.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [MessageBuilder](MessageBuilder.md) (2 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [asyncio.md](asyncio.md.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/app/tracked_task_manager.py`
- `server/services/game_tick_service.py`
- `server/tests/unit/app/test_tracked_task_manager.py`

## Audit Trail

- EXTRACTED: 98 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*