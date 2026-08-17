# server app task registry

> 7 nodes

## Key Concepts

- **task_registry.py** (12 connections) — `server/app/task_registry.py`
- **unregister_task()** (7 connections) — `server/app/task_registry.py`
- **register_task()** (6 connections) — `server/app/task_registry.py`
- **._cleanup_registry_collections()** (4 connections) — `server/app/task_registry.py`
- **Convenience function for registering tasks with global registry.** (2 connections) — `server/app/task_registry.py`
- **Centralized TaskRegistry for MythosMUD server task lifecycle management. This…** (1 connections) — `server/app/task_registry.py`
- **Clean up active collections after final shutdown.** (1 connections) — `server/app/task_registry.py`

## Relationships

- [server app task registry get](server_app_task_registry_get.md) (8 shared connections)
- [server app task registry py](server_app_task_registry_py.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server app task registry rationale](server_app_task_registry_rationale.md) (1 shared connections)
- [holidayresolver](holidayresolver.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*