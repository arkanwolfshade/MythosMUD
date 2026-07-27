# App Tracked Task

> 5 nodes · cohesion 0.40

## Key Concepts

- **.__init__()** (3 connections) — `server/app/tracked_task_manager.py`
- **.set_task_registry()** (3 connections) — `server/app/tracked_task_manager.py`
- **TaskRegistry** (3 connections) — `server/app/tracked_task_manager.py`
- **Attach a TaskRegistry instance to this Tracker for shared coordination.** (1 connections) — `server/app/tracked_task_manager.py`
- **Initialize the TrackedTaskManager.          Args:             task_registry: Opt** (1 connections) — `server/app/tracked_task_manager.py`

## Relationships

- [[NPC Admin API]] (2 shared connections)
- [[Async Task Registry]] (1 shared connections)

## Source Files

- `server/app/tracked_task_manager.py`

## Audit Trail

- EXTRACTED: 10 (91%)
- INFERRED: 1 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
