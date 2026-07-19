# App Tracked Task

> 6 nodes · cohesion 0.47

## Key Concepts

- **.create_tracked_task()** (6 connections) — `server/app/tracked_task_manager.py`
- **.create_supervised_task()** (5 connections) — `server/app/tracked_task_manager.py`
- **Any** (3 connections) — `server/app/tracked_task_manager.py`
- **Task** (3 connections) — `server/app/tracked_task_manager.py`
- **Create a task with enhanced supervision for legacy cleanup scenarios.          A** (1 connections) — `server/app/tracked_task_manager.py`
- **Create a managed asyncio.Task with mandatory lifecycle tracking.          Args:** (1 connections) — `server/app/tracked_task_manager.py`

## Relationships

- [[NPC Admin API]] (2 shared connections)
- [[Async Task Registry]] (2 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/app/tracked_task_manager.py`

## Audit Trail

- EXTRACTED: 16 (84%)
- INFERRED: 3 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
