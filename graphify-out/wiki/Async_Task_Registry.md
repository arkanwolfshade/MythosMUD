# Async Task Registry

> 4 nodes · cohesion 0.04

## Key Concepts

- **Any** (10 connections) — `server/app/task_registry.py`
- **Task** (8 connections) — `server/app/task_registry.py`
- **Any** (3 connections) — `server/app/tracked_task_manager.py`
- **Task** (3 connections) — `server/app/tracked_task_manager.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`

## Audit Trail

- EXTRACTED: 22 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*