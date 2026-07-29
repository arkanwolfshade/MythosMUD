# task registry

> 29 nodes

## Key Concepts

- **task_registry.py** (10 connections) — `server/app/task_registry.py`
- **Any** (10 connections)
- **._setup_task_tracking()** (9 connections) — `server/app/task_registry.py`
- **Task** (8 connections)
- **TaskMetadata** (7 connections) — `server/app/task_registry.py`
- **.register_task()** (7 connections) — `server/app/task_registry.py`
- **._create_task_completion_callback()** (5 connections) — `server/app/task_registry.py`
- **unregister_task()** (5 connections) — `server/app/task_registry.py`
- **get_registry()** (5 connections) — `server/app/task_registry.py`
- **.__init__()** (4 connections) — `server/app/task_registry.py`
- **.unregister_task()** (4 connections) — `server/app/task_registry.py`
- **.cancel_task()** (4 connections) — `server/app/task_registry.py`
- **._cleanup_registry_collections()** (4 connections) — `server/app/task_registry.py`
- **register_task()** (4 connections) — `server/app/task_registry.py`
- **.get_registry_info()** (3 connections) — `server/app/task_registry.py`
- **.__repr__()** (2 connections) — `server/app/task_registry.py`
- **Convenience function for registering tasks with global registry.** (2 connections) — `server/app/task_registry.py`
- **Centralized TaskRegistry for MythosMUD server task lifecycle management.  This m** (1 connections) — `server/app/task_registry.py`
- **Metadata for tracked asyncio.Tasks.** (1 connections) — `server/app/task_registry.py`
- **Initialize task metadata.          Args:             task: The asyncio.Task inst** (1 connections) — `server/app/task_registry.py`
- **String representation of task metadata for logging.** (1 connections) — `server/app/task_registry.py`
- **Create callback function for task completion cleanup.** (1 connections) — `server/app/task_registry.py`
- **Set up tracking for a newly created task.** (1 connections) — `server/app/task_registry.py`
- **Register and create a tracked asyncio.Task.          Args:             coro: The** (1 connections) — `server/app/task_registry.py`
- **Unregister task from tracking, optionally force-cancelling.          Args:** (1 connections) — `server/app/task_registry.py`
- *... and 4 more nodes in this community*

## Relationships

- [Cancel lifecycle/critical tasks first (Phase](Cancel_lifecycle-critical_tasks_first_%28Phase.md) (15 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [monitoring](monitoring.md) (2 shared connections)
- [memory lifespan coordinator](memory_lifespan_coordinator.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`

## Audit Trail

- EXTRACTED: 105 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*