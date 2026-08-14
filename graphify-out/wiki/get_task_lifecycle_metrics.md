# .get_task_lifecycle_metrics

> 6 nodes

## Key Concepts

- **.get_task_lifecycle_metrics()** (5 connections) — `server/app/task_registry.py`
- **.get_active_task_count()** (3 connections) — `server/app/task_registry.py`
- **.get_task_stats_by_type()** (3 connections) — `server/app/task_registry.py`
- **Get count of active tasks.** (1 connections) — `server/app/task_registry.py`
- **Get task breakdown by type.** (1 connections) — `server/app/task_registry.py`
- **Get task lifecycle metrics including creation and completion rates.** (1 connections) — `server/app/task_registry.py`

## Relationships

- [TaskRegistry](TaskRegistry.md) (3 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*