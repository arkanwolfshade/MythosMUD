# follow service game

> 78 nodes

## Key Concepts

- **TaskRegistry** (49 connections) — `server/app/task_registry.py`
- **test_task_registry.py** (23 connections) — `server/tests/unit/app/test_task_registry.py`
- **task_registry.py** (11 connections) — `server/app/task_registry.py`
- **Any** (10 connections)
- **._setup_task_tracking()** (9 connections) — `server/app/task_registry.py`
- **get_registry()** (9 connections) — `server/app/task_registry.py`
- **_sleep_briefly()** (9 connections) — `server/tests/unit/app/test_task_registry.py`
- **Task** (8 connections)
- **TaskMetadata** (7 connections) — `server/app/task_registry.py`
- **.register_task()** (7 connections) — `server/app/task_registry.py`
- **.shutdown_all()** (7 connections) — `server/app/task_registry.py`
- **unregister_task()** (7 connections) — `server/app/task_registry.py`
- **register_task()** (6 connections) — `server/app/task_registry.py`
- **._create_task_completion_callback()** (5 connections) — `server/app/task_registry.py`
- **.get_task_lifecycle_metrics()** (5 connections) — `server/app/task_registry.py`
- **test_module_level_helpers()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **.__init__()** (4 connections) — `server/app/task_registry.py`
- **.unregister_task()** (4 connections) — `server/app/task_registry.py`
- **.cancel_task()** (4 connections) — `server/app/task_registry.py`
- **._cleanup_registry_collections()** (4 connections) — `server/app/task_registry.py`
- **test_register_closes_coro_when_create_task_fails()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **._ensure_unique_task_name()** (3 connections) — `server/app/task_registry.py`
- **._track_task_creation_metrics()** (3 connections) — `server/app/task_registry.py`
- **._extract_service_name()** (3 connections) — `server/app/task_registry.py`
- **._cancel_lifecycle_tasks()** (3 connections) — `server/app/task_registry.py`
- *... and 53 more nodes in this community*

## Relationships

- [schemas player rationale](schemas_player_rationale.md) (5 shared connections)
- [time service rationale](time_service_rationale.md) (4 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [health models rationale](health_models_rationale.md) (2 shared connections)
- [metrics memory leak](metrics_memory_leak.md) (1 shared connections)
- [command combat models](command_combat_models.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/tests/unit/app/test_task_registry.py`

## Audit Trail

- EXTRACTED: 297 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*