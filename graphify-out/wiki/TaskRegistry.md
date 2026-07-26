# TaskRegistry

> 78 nodes · cohesion 0.04

## Key Concepts

- **TaskRegistry** (33 connections) — `server/app/task_registry.py`
- **TrackedTaskManager** (14 connections) — `server/app/tracked_task_manager.py`
- **memory_leak_metrics.py** (12 connections) — `server/monitoring/memory_leak_metrics.py`
- **task_registry.py** (10 connections) — `server/app/task_registry.py`
- **Any** (10 connections)
- **._setup_task_tracking()** (9 connections) — `server/app/task_registry.py`
- **Task** (8 connections)
- **get_registry()** (7 connections) — `server/app/task_registry.py`
- **TaskMetadata** (7 connections) — `server/app/task_registry.py`
- **.register_task()** (7 connections) — `server/app/task_registry.py`
- **.shutdown_all()** (7 connections) — `server/app/task_registry.py`
- **._create_task_completion_callback()** (5 connections) — `server/app/task_registry.py`
- **.get_task_lifecycle_metrics()** (5 connections) — `server/app/task_registry.py`
- **unregister_task()** (5 connections) — `server/app/task_registry.py`
- **.create_supervised_task()** (5 connections) — `server/app/tracked_task_manager.py`
- **.create_tracked_task()** (5 connections) — `server/app/tracked_task_manager.py`
- **register_task()** (4 connections) — `server/app/task_registry.py`
- **.__init__()** (4 connections) — `server/app/task_registry.py`
- **.cancel_task()** (4 connections) — `server/app/task_registry.py`
- **._cleanup_registry_collections()** (4 connections) — `server/app/task_registry.py`
- **.unregister_task()** (4 connections) — `server/app/task_registry.py`
- **._cancel_lifecycle_tasks()** (3 connections) — `server/app/task_registry.py`
- **._cancel_remaining_tasks()** (3 connections) — `server/app/task_registry.py`
- **._ensure_unique_task_name()** (3 connections) — `server/app/task_registry.py`
- **._extract_service_name()** (3 connections) — `server/app/task_registry.py`
- *... and 53 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (7 shared connections)
- [__init__.py](__init__.py.md) (4 shared connections)
- [lifespan.py](lifespan.py.md) (4 shared connections)
- [monitoring.py](monitoring.py.md) (3 shared connections)
- [get_cache_manager](get_cache_manager.md) (1 shared connections)
- [test_memory_leak_metrics.py](test_memory_leak_metrics.py.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`
- `server/monitoring/memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 254 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*