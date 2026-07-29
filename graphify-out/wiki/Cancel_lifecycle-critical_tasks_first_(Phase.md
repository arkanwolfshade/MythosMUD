# Cancel lifecycle/critical tasks first (Phase

> 28 nodes

## Key Concepts

- **TaskRegistry** (33 connections) — `server/app/task_registry.py`
- **.shutdown_all()** (7 connections) — `server/app/task_registry.py`
- **.get_task_lifecycle_metrics()** (5 connections) — `server/app/task_registry.py`
- **._ensure_unique_task_name()** (3 connections) — `server/app/task_registry.py`
- **._track_task_creation_metrics()** (3 connections) — `server/app/task_registry.py`
- **._extract_service_name()** (3 connections) — `server/app/task_registry.py`
- **._cancel_lifecycle_tasks()** (3 connections) — `server/app/task_registry.py`
- **._cancel_remaining_tasks()** (3 connections) — `server/app/task_registry.py`
- **._wait_for_task_completion()** (3 connections) — `server/app/task_registry.py`
- **._forcible_cleanup_on_timeout()** (3 connections) — `server/app/task_registry.py`
- **.list_active_tasks()** (3 connections) — `server/app/task_registry.py`
- **.get_active_task_count()** (3 connections) — `server/app/task_registry.py`
- **.get_task_stats_by_type()** (3 connections) — `server/app/task_registry.py`
- **.__init__()** (2 connections) — `server/app/task_registry.py`
- **Centralized asyncio task registry for lifecycle-tracking with timeout management** (1 connections) — `server/app/task_registry.py`
- **Initialize TaskRegistry with empty task collections.** (1 connections) — `server/app/task_registry.py`
- **Ensure task name is unique by appending timestamp if needed.** (1 connections) — `server/app/task_registry.py`
- **Track task creation for metrics.** (1 connections) — `server/app/task_registry.py`
- **Extract service name from task name or use task type.** (1 connections) — `server/app/task_registry.py`
- **Cancel lifecycle/critical tasks first (Phase 1).** (1 connections) — `server/app/task_registry.py`
- **Cancel remaining active tasks (Phase 2).** (1 connections) — `server/app/task_registry.py`
- **Wait for task completion with timeout.** (1 connections) — `server/app/task_registry.py`
- **Forcibly cancel any lingering tasks that didn't respond to graceful cancellation** (1 connections) — `server/app/task_registry.py`
- **Gracefully shutdown all tracked tasks with timeout coordination.          Implem** (1 connections) — `server/app/task_registry.py`
- **Return list of currently registered TaskMetadata.** (1 connections) — `server/app/task_registry.py`
- *... and 3 more nodes in this community*

## Relationships

- [task registry](task_registry.md) (15 shared connections)
- [Any](Any.md) (4 shared connections)
- [.initialize()](initialize%28%29.md) (3 shared connections)
- [memory lifespan coordinator](memory_lifespan_coordinator.md) (1 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`

## Audit Trail

- EXTRACTED: 88 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*