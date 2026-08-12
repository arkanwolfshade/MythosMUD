# TaskRegistry

> 60 nodes

## Key Concepts

- **TaskRegistry** (33 connections) — `server/app/task_registry.py`
- **Any** (10 connections)
- **._setup_task_tracking()** (9 connections) — `server/app/task_registry.py`
- **Task** (8 connections)
- **TaskMetadata** (7 connections) — `server/app/task_registry.py`
- **.register_task()** (7 connections) — `server/app/task_registry.py`
- **.shutdown_all()** (7 connections) — `server/app/task_registry.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **._create_task_completion_callback()** (5 connections) — `server/app/task_registry.py`
- **.get_task_lifecycle_metrics()** (5 connections) — `server/app/task_registry.py`
- **unregister_task()** (5 connections) — `server/app/task_registry.py`
- **register_task()** (4 connections) — `server/app/task_registry.py`
- **.__init__()** (4 connections) — `server/app/task_registry.py`
- **.cancel_task()** (4 connections) — `server/app/task_registry.py`
- **._cleanup_registry_collections()** (4 connections) — `server/app/task_registry.py`
- **.unregister_task()** (4 connections) — `server/app/task_registry.py`
- **._cancel_lifecycle_tasks()** (3 connections) — `server/app/task_registry.py`
- **._cancel_remaining_tasks()** (3 connections) — `server/app/task_registry.py`
- **._ensure_unique_task_name()** (3 connections) — `server/app/task_registry.py`
- **._extract_service_name()** (3 connections) — `server/app/task_registry.py`
- **._forcible_cleanup_on_timeout()** (3 connections) — `server/app/task_registry.py`
- **.get_active_task_count()** (3 connections) — `server/app/task_registry.py`
- **.get_registry_info()** (3 connections) — `server/app/task_registry.py`
- **.get_task_stats_by_type()** (3 connections) — `server/app/task_registry.py`
- **.list_active_tasks()** (3 connections) — `server/app/task_registry.py`
- *... and 35 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (6 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [GameBundle](GameBundle.md) (2 shared connections)
- [time.py](time.py.md) (1 shared connections)
- [ScheduleService](ScheduleService.md) (1 shared connections)
- [MetricsCollector](MetricsCollector.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`
- `server/time/tick_scheduler.py`

## Audit Trail

- EXTRACTED: 191 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*