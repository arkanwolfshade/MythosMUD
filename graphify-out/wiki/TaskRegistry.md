# TaskRegistry

> 23 nodes

## Key Concepts

- **TaskRegistry** (49 connections) — `server/app/task_registry.py`
- **test_task_registry.py** (24 connections) — `server/tests/unit/app/test_task_registry.py`
- **asyncio** (14 connections)
- **_sleep_briefly()** (9 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_module_level_helpers()** (6 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_closes_coro_when_create_task_fails()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_cancel_task_by_name()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_get_registry_info_and_metrics()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_list_active_tasks_and_stats_by_type()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_and_unregister_task()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_duplicate_name_gets_suffix()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_during_shutdown_raises()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_shutdown_all_clears_active_tasks()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_task_metadata_repr()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **_hang_until_cancelled()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **registry()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_cancel_missing_task_returns_false()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_shutdown_all_idempotent_warning()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_unregister_missing_task_returns_false()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **fixture** (1 connections)
- **MonkeyPatch** (1 connections)
- **Centralized asyncio task registry for lifecycle-tracking with timeout…** (1 connections) — `server/app/task_registry.py`
- **Unit tests for asyncio TaskRegistry lifecycle management.** (1 connections) — `server/tests/unit/app/test_task_registry.py`

## Relationships

- [Any](Any.md) (12 shared connections)
- [task_registry.py](task_registry.py.md) (8 shared connections)
- [.shutdown_all](shutdown_all.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (3 shared connections)
- [.get_task_lifecycle_metrics](get_task_lifecycle_metrics.md) (3 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/tests/unit/app/test_task_registry.py`

## Audit Trail

- EXTRACTED: 81 (82%)
- INFERRED: 18 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*