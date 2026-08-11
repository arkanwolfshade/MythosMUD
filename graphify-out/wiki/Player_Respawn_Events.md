# Player Respawn Events

> 38 nodes

## Key Concepts

- **Any** (10 connections)
- **._setup_task_tracking()** (9 connections) — `server/app/task_registry.py`
- **Task** (8 connections)
- **TaskMetadata** (7 connections) — `server/app/task_registry.py`
- **.register_task()** (7 connections) — `server/app/task_registry.py`
- **._create_task_completion_callback()** (5 connections) — `server/app/task_registry.py`
- **.get_task_lifecycle_metrics()** (5 connections) — `server/app/task_registry.py`
- **unregister_task()** (5 connections) — `server/app/task_registry.py`
- **.__init__()** (4 connections) — `server/app/task_registry.py`
- **.unregister_task()** (4 connections) — `server/app/task_registry.py`
- **.cancel_task()** (4 connections) — `server/app/task_registry.py`
- **register_task()** (4 connections) — `server/app/task_registry.py`
- **._ensure_unique_task_name()** (3 connections) — `server/app/task_registry.py`
- **._track_task_creation_metrics()** (3 connections) — `server/app/task_registry.py`
- **._extract_service_name()** (3 connections) — `server/app/task_registry.py`
- **.list_active_tasks()** (3 connections) — `server/app/task_registry.py`
- **.get_registry_info()** (3 connections) — `server/app/task_registry.py`
- **.get_active_task_count()** (3 connections) — `server/app/task_registry.py`
- **.get_task_stats_by_type()** (3 connections) — `server/app/task_registry.py`
- **.__repr__()** (2 connections) — `server/app/task_registry.py`
- **Metadata for tracked asyncio.Tasks.** (1 connections) — `server/app/task_registry.py`
- **Initialize task metadata.          Args:             task: The asyncio.Task inst** (1 connections) — `server/app/task_registry.py`
- **String representation of task metadata for logging.** (1 connections) — `server/app/task_registry.py`
- **Ensure task name is unique by appending timestamp if needed.** (1 connections) — `server/app/task_registry.py`
- **Track task creation for metrics.** (1 connections) — `server/app/task_registry.py`
- *... and 13 more nodes in this community*

## Relationships

- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (14 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)

## Source Files

- `server/app/task_registry.py`

## Audit Trail

- EXTRACTED: 113 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*