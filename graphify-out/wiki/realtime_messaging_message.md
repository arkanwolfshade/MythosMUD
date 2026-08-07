# realtime messaging message

> 28 nodes

## Key Concepts

- **Any** (10 connections)
- **._setup_task_tracking()** (9 connections) — `server/app/task_registry.py`
- **Task** (8 connections)
- **TaskMetadata** (7 connections) — `server/app/task_registry.py`
- **.register_task()** (7 connections) — `server/app/task_registry.py`
- **._create_task_completion_callback()** (5 connections) — `server/app/task_registry.py`
- **.__init__()** (4 connections) — `server/app/task_registry.py`
- **.unregister_task()** (4 connections) — `server/app/task_registry.py`
- **.cancel_task()** (4 connections) — `server/app/task_registry.py`
- **._ensure_unique_task_name()** (3 connections) — `server/app/task_registry.py`
- **._track_task_creation_metrics()** (3 connections) — `server/app/task_registry.py`
- **._extract_service_name()** (3 connections) — `server/app/task_registry.py`
- **.list_active_tasks()** (3 connections) — `server/app/task_registry.py`
- **.get_registry_info()** (3 connections) — `server/app/task_registry.py`
- **.__repr__()** (2 connections) — `server/app/task_registry.py`
- **Metadata for tracked asyncio.Tasks.** (1 connections) — `server/app/task_registry.py`
- **Initialize task metadata.          Args:             task: The asyncio.Task inst** (1 connections) — `server/app/task_registry.py`
- **String representation of task metadata for logging.** (1 connections) — `server/app/task_registry.py`
- **Ensure task name is unique by appending timestamp if needed.** (1 connections) — `server/app/task_registry.py`
- **Track task creation for metrics.** (1 connections) — `server/app/task_registry.py`
- **Extract service name from task name or use task type.** (1 connections) — `server/app/task_registry.py`
- **Create callback function for task completion cleanup.** (1 connections) — `server/app/task_registry.py`
- **Set up tracking for a newly created task.** (1 connections) — `server/app/task_registry.py`
- **Register and create a tracked asyncio.Task.          Args:             coro: The** (1 connections) — `server/app/task_registry.py`
- **Unregister task from tracking, optionally force-cancelling.          Args:** (1 connections) — `server/app/task_registry.py`
- *... and 3 more nodes in this community*

## Relationships

- [follow service game](follow_service_game.md) (16 shared connections)

## Source Files

- `server/app/task_registry.py`

## Audit Trail

- EXTRACTED: 88 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*