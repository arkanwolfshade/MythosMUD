# TaskRegistry

> 87 nodes

## Key Concepts

- **TaskRegistry** (49 connections) — `server/app/task_registry.py`
- **test_task_registry.py** (24 connections) — `server/tests/unit/app/test_task_registry.py`
- **asyncio** (14 connections)
- **TaskRegistry** (14 connections)
- **task_registry.py** (13 connections) — `server/app/task_registry.py`
- **Any** (10 connections)
- **get_registry()** (9 connections) — `server/app/task_registry.py`
- **._setup_task_tracking()** (9 connections) — `server/app/task_registry.py`
- **_sleep_briefly()** (9 connections) — `server/tests/unit/app/test_task_registry.py`
- **.shutdown_all()** (8 connections) — `server/app/task_registry.py`
- **Task** (8 connections)
- **TaskMetadata** (7 connections) — `server/app/task_registry.py`
- **.register_task()** (7 connections) — `server/app/task_registry.py`
- **unregister_task()** (7 connections) — `server/app/task_registry.py`
- **test_module_level_helpers()** (7 connections) — `server/tests/unit/app/test_task_registry.py`
- **register_task()** (6 connections) — `server/app/task_registry.py`
- **test_register_closes_coro_when_create_task_fails()** (6 connections) — `server/tests/unit/app/test_task_registry.py`
- **._create_task_completion_callback()** (5 connections) — `server/app/task_registry.py`
- **.get_task_lifecycle_metrics()** (5 connections) — `server/app/task_registry.py`
- **test_cancel_task_by_name()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_get_registry_info_and_metrics()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_list_active_tasks_and_stats_by_type()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_and_unregister_task()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_duplicate_name_gets_suffix()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_during_shutdown_raises()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- *... and 62 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (3 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [event_handler.py](event_handler.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [ground_channel.py](ground_channel.py.md) (2 shared connections)
- [.initialize](initialize.md) (1 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (1 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/events/event_bus.py`
- `server/tests/unit/app/test_task_registry.py`
- `server/tests/unit/commands/test_ground_channel.py`

## Audit Trail

- EXTRACTED: 180 (89%)
- INFERRED: 22 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*