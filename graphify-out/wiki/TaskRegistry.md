# TaskRegistry

> 80 nodes

## Key Concepts

- **TaskRegistry** (49 connections) — `server/app/task_registry.py`
- **test_task_registry.py** (25 connections) — `server/tests/unit/app/test_task_registry.py`
- **asyncio** (14 connections)
- **task_registry.py** (12 connections) — `server/app/task_registry.py`
- **Any** (10 connections)
- **get_registry()** (9 connections) — `server/app/task_registry.py`
- **._setup_task_tracking()** (9 connections) — `server/app/task_registry.py`
- **_sleep_briefly()** (9 connections) — `server/tests/unit/app/test_task_registry.py`
- **Task** (8 connections)
- **TaskMetadata** (7 connections) — `server/app/task_registry.py`
- **.register_task()** (7 connections) — `server/app/task_registry.py`
- **.shutdown_all()** (7 connections) — `server/app/task_registry.py`
- **unregister_task()** (7 connections) — `server/app/task_registry.py`
- **register_task()** (6 connections) — `server/app/task_registry.py`
- **test_module_level_helpers()** (6 connections) — `server/tests/unit/app/test_task_registry.py`
- **._create_task_completion_callback()** (5 connections) — `server/app/task_registry.py`
- **.get_task_lifecycle_metrics()** (5 connections) — `server/app/task_registry.py`
- **test_register_closes_coro_when_create_task_fails()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **.__init__()** (4 connections) — `server/app/task_registry.py`
- **.cancel_task()** (4 connections) — `server/app/task_registry.py`
- **._cleanup_registry_collections()** (4 connections) — `server/app/task_registry.py`
- **.unregister_task()** (4 connections) — `server/app/task_registry.py`
- **test_cancel_task_by_name()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_get_registry_info_and_metrics()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_list_active_tasks_and_stats_by_type()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- *... and 55 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (4 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (1 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/tests/unit/app/test_task_registry.py`

## Audit Trail

- EXTRACTED: 159 (90%)
- INFERRED: 18 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*