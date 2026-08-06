# schemas player rationale

> 37 nodes

## Key Concepts

- **TrackedTaskManager** (22 connections) — `server/app/tracked_task_manager.py`
- **test_tracked_task_manager.py** (18 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **.create_tracked_task()** (5 connections) — `server/app/tracked_task_manager.py`
- **.create_supervised_task()** (5 connections) — `server/app/tracked_task_manager.py`
- **memory_leak_prevention_channel_start_session()** (5 connections) — `server/app/tracked_task_manager.py`
- **reset_global_tracked_manager()** (4 connections) — `server/app/tracked_task_manager.py`
- **patch_asyncio_create_task_with_tracking()** (4 connections) — `server/app/tracked_task_manager.py`
- **.__init__()** (3 connections) — `server/app/tracked_task_manager.py`
- **.set_task_registry()** (3 connections) — `server/app/tracked_task_manager.py`
- **Any** (2 connections)
- **Task** (2 connections)
- **.audit_orphans()** (2 connections) — `server/app/tracked_task_manager.py`
- **.cleanup_orphaned_tasks()** (2 connections) — `server/app/tracked_task_manager.py`
- **.actively_tracked_task_count()** (2 connections) — `server/app/tracked_task_manager.py`
- **reset_global()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_create_tracked_task_runs_coro()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_create_tracked_task_with_registry()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_create_tracked_task_registry_failure_falls_back()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_create_supervised_task_completes()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_audit_orphans_counts_untracked()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_cleanup_orphaned_tasks_cancels_running()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_global_manager_singleton()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_set_task_registry()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_memory_leak_prevention_session_start()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_patch_asyncio_create_task_with_tracking()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- *... and 12 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (9 shared connections)
- [follow service game](follow_service_game.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [scripts worktree ops](scripts_worktree_ops.md) (1 shared connections)

## Source Files

- `server/app/tracked_task_manager.py`
- `server/tests/unit/app/test_tracked_task_manager.py`

## Audit Trail

- EXTRACTED: 111 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*