# startup services npc

> 6 nodes

## Key Concepts

- **.create_tracked_task()** (5 connections) — `server/app/tracked_task_manager.py`
- **.create_supervised_task()** (5 connections) — `server/app/tracked_task_manager.py`
- **Any** (2 connections)
- **Task** (2 connections)
- **Create a managed asyncio.Task with mandatory lifecycle tracking.          Args:** (1 connections) — `server/app/tracked_task_manager.py`
- **Create a task with enhanced supervision for legacy cleanup scenarios.          A** (1 connections) — `server/app/tracked_task_manager.py`

## Relationships

- [schemas player rationale](schemas_player_rationale.md) (2 shared connections)

## Source Files

- `server/app/tracked_task_manager.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*