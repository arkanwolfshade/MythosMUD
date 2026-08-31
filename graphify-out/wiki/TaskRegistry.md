# TaskRegistry

> 52 nodes

## Key Concepts

- **TaskRegistry** (51 connections) — `server/app/task_registry.py`
- **test_task_registry.py** (25 connections) — `server/tests/unit/app/test_task_registry.py`
- **asyncio** (14 connections)
- **task_registry.py** (13 connections) — `server/app/task_registry.py`
- **get_registry()** (9 connections) — `server/app/task_registry.py`
- **_sleep_briefly()** (9 connections) — `server/tests/unit/app/test_task_registry.py`
- **.shutdown_all()** (7 connections) — `server/app/task_registry.py`
- **unregister_task()** (7 connections) — `server/app/task_registry.py`
- **register_task()** (6 connections) — `server/app/task_registry.py`
- **test_module_level_helpers()** (6 connections) — `server/tests/unit/app/test_task_registry.py`
- **.get_task_lifecycle_metrics()** (5 connections) — `server/app/task_registry.py`
- **test_register_closes_coro_when_create_task_fails()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **._cleanup_registry_collections()** (4 connections) — `server/app/task_registry.py`
- **test_cancel_task_by_name()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_get_registry_info_and_metrics()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_list_active_tasks_and_stats_by_type()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_and_unregister_task()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_duplicate_name_gets_suffix()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_during_shutdown_raises()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_shutdown_all_clears_active_tasks()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_task_metadata_repr()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **._cancel_lifecycle_tasks()** (3 connections) — `server/app/task_registry.py`
- **._cancel_remaining_tasks()** (3 connections) — `server/app/task_registry.py`
- **._forcible_cleanup_on_timeout()** (3 connections) — `server/app/task_registry.py`
- **.get_active_task_count()** (3 connections) — `server/app/task_registry.py`
- *... and 27 more nodes in this community*

## Relationships

- [Any](Any.md) (16 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (5 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (4 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)
- [asyncio.md](asyncio.md.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/tests/unit/app/test_task_registry.py`

## Audit Trail

- EXTRACTED: 126 (88%)
- INFERRED: 18 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*