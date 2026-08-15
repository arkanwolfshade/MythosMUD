# .shutdown_all

> 12 nodes

## Key Concepts

- **.shutdown_all()** (7 connections) — `server/app/task_registry.py`
- **._cleanup_registry_collections()** (4 connections) — `server/app/task_registry.py`
- **._cancel_lifecycle_tasks()** (3 connections) — `server/app/task_registry.py`
- **._cancel_remaining_tasks()** (3 connections) — `server/app/task_registry.py`
- **._forcible_cleanup_on_timeout()** (3 connections) — `server/app/task_registry.py`
- **._wait_for_task_completion()** (3 connections) — `server/app/task_registry.py`
- **Cancel lifecycle/critical tasks first (Phase 1).** (1 connections) — `server/app/task_registry.py`
- **Cancel remaining active tasks (Phase 2).** (1 connections) — `server/app/task_registry.py`
- **Wait for task completion with timeout.** (1 connections) — `server/app/task_registry.py`
- **Forcibly cancel any lingering tasks that didn't respond to graceful…** (1 connections) — `server/app/task_registry.py`
- **Clean up active collections after final shutdown.** (1 connections) — `server/app/task_registry.py`
- **Gracefully shutdown all tracked tasks with timeout coordination. Implements…** (1 connections) — `server/app/task_registry.py`

## Relationships

- [TaskRegistry](TaskRegistry.md) (6 shared connections)
- [task_registry.py](task_registry.py.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*