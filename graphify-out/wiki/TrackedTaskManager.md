# TrackedTaskManager

> 18 nodes

## Key Concepts

- **TrackedTaskManager** (14 connections) — `server/app/tracked_task_manager.py`
- **.create_supervised_task()** (5 connections) — `server/app/tracked_task_manager.py`
- **.create_tracked_task()** (5 connections) — `server/app/tracked_task_manager.py`
- **.__init__()** (3 connections) — `server/app/tracked_task_manager.py`
- **.set_task_registry()** (3 connections) — `server/app/tracked_task_manager.py`
- **.actively_tracked_task_count()** (2 connections) — `server/app/tracked_task_manager.py`
- **.audit_orphans()** (2 connections) — `server/app/tracked_task_manager.py`
- **.cleanup_orphaned_tasks()** (2 connections) — `server/app/tracked_task_manager.py`
- **Any** (2 connections)
- **Task** (2 connections)
- **Create a task with enhanced supervision for legacy cleanup scenarios. Args:…** (1 connections) — `server/app/tracked_task_manager.py`
- **Audit and reclaim orphaned task candidates across the system. Returns: Number…** (1 connections) — `server/app/tracked_task_manager.py`
- **Proactively clean up orphaned tasks by cancelling leak prevention violations.…** (1 connections) — `server/app/tracked_task_manager.py`
- **Return count of currently tracked task references within the manager's…** (1 connections) — `server/app/tracked_task_manager.py`
- **Attach a TaskRegistry instance to this Tracker for shared coordination. Args:…** (1 connections) — `server/app/tracked_task_manager.py`
- **Central namespace for tracked task lifecycle coordination preventing orphaned…** (1 connections) — `server/app/tracked_task_manager.py`
- **Initialize the TrackedTaskManager. Args: task_registry: Optional TaskRegistry…** (1 connections) — `server/app/tracked_task_manager.py`
- **Create a managed asyncio.Task with mandatory lifecycle tracking. Args: coro:…** (1 connections) — `server/app/tracked_task_manager.py`

## Relationships

- [bundles/game.py](bundles-game.py.md) (3 shared connections)
- [TaskRegistry](TaskRegistry.md) (3 shared connections)
- [get_global_tracked_manager](get_global_tracked_manager.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/app/tracked_task_manager.py`

## Audit Trail

- EXTRACTED: 46 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*