# Any

> 18 nodes

## Key Concepts

- **TrackedTaskManager** (14 connections) — `server/app/tracked_task_manager.py`
- **.create_tracked_task()** (5 connections) — `server/app/tracked_task_manager.py`
- **.create_supervised_task()** (5 connections) — `server/app/tracked_task_manager.py`
- **.__init__()** (3 connections) — `server/app/tracked_task_manager.py`
- **.set_task_registry()** (3 connections) — `server/app/tracked_task_manager.py`
- **Any** (2 connections)
- **Task** (2 connections)
- **.audit_orphans()** (2 connections) — `server/app/tracked_task_manager.py`
- **.cleanup_orphaned_tasks()** (2 connections) — `server/app/tracked_task_manager.py`
- **.actively_tracked_task_count()** (2 connections) — `server/app/tracked_task_manager.py`
- **Central namespace for tracked task lifecycle coordination preventing orphaned me** (1 connections) — `server/app/tracked_task_manager.py`
- **Initialize the TrackedTaskManager.          Args:             task_registry: Opt** (1 connections) — `server/app/tracked_task_manager.py`
- **Create a managed asyncio.Task with mandatory lifecycle tracking.          Args:** (1 connections) — `server/app/tracked_task_manager.py`
- **Create a task with enhanced supervision for legacy cleanup scenarios.          A** (1 connections) — `server/app/tracked_task_manager.py`
- **Audit and reclaim orphaned task candidates across the system.          Returns:** (1 connections) — `server/app/tracked_task_manager.py`
- **Proactively clean up orphaned tasks by cancelling leak prevention violations.** (1 connections) — `server/app/tracked_task_manager.py`
- **Return count of currently tracked task references within the manager's supervisi** (1 connections) — `server/app/tracked_task_manager.py`
- **Attach a TaskRegistry instance to this Tracker for shared coordination.** (1 connections) — `server/app/tracked_task_manager.py`

## Relationships

- [Cancel lifecycle/critical tasks first (Phase](Cancel_lifecycle-critical_tasks_first_%28Phase.md) (3 shared connections)
- [.initialize()](initialize%28%29.md) (3 shared connections)
- [memory lifespan coordinator](memory_lifespan_coordinator.md) (2 shared connections)

## Source Files

- `server/app/tracked_task_manager.py`

## Audit Trail

- EXTRACTED: 46 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*