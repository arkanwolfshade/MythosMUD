# TrackedTaskManager

> 44 nodes · cohesion 0.08

## Key Concepts

- **TrackedTaskManager** (22 connections) — `server/app/tracked_task_manager.py`
- **get_global_tracked_manager()** (19 connections) — `server/app/tracked_task_manager.py`
- **test_tracked_task_manager.py** (19 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **tracked_task_manager.py** (15 connections) — `server/app/tracked_task_manager.py`
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
- **Any** (2 connections)
- **Task** (2 connections)
- **TaskRegistry** (2 connections)
- **.actively_tracked_task_count()** (2 connections) — `server/app/tracked_task_manager.py`
- **.audit_orphans()** (2 connections) — `server/app/tracked_task_manager.py`
- *... and 19 more nodes in this community*

## Relationships

- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (5 shared connections)
- [Room](Room.md) (4 shared connections)
- [look_container.py](look_container.py.md) (4 shared connections)
- [command_error](command_error.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)
- [test_combat_assist.py](test_combat_assist.py.md) (1 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)

## Source Files

- `server/app/tracked_task_manager.py`
- `server/tests/unit/app/test_tracked_task_manager.py`

## Audit Trail

- EXTRACTED: 88 (91%)
- INFERRED: 9 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*