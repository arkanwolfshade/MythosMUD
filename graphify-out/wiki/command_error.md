# command_error

> 40 nodes · cohesion 0.13

## Key Concepts

- **TaskRegistry** (49 connections) — `server/app/task_registry.py`
- **test_task_registry.py** (24 connections) — `server/tests/unit/app/test_task_registry.py`
- **asyncio** (14 connections)
- **TaskRegistry** (14 connections)
- **task_registry.py** (13 connections) — `server/app/task_registry.py`
- **get_registry()** (9 connections) — `server/app/task_registry.py`
- **_sleep_briefly()** (9 connections) — `server/tests/unit/app/test_task_registry.py`
- **unregister_task()** (7 connections) — `server/app/task_registry.py`
- **test_module_level_helpers()** (7 connections) — `server/tests/unit/app/test_task_registry.py`
- **register_task()** (6 connections) — `server/app/task_registry.py`
- **test_register_closes_coro_when_create_task_fails()** (6 connections) — `server/tests/unit/app/test_task_registry.py`
- **.get_task_lifecycle_metrics()** (5 connections) — `server/app/task_registry.py`
- **test_cancel_task_by_name()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_get_registry_info_and_metrics()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_list_active_tasks_and_stats_by_type()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_and_unregister_task()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_duplicate_name_gets_suffix()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_during_shutdown_raises()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_shutdown_all_clears_active_tasks()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_task_metadata_repr()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **._cleanup_registry_collections()** (4 connections) — `server/app/task_registry.py`
- **registry()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_cancel_missing_task_returns_false()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_shutdown_all_idempotent_warning()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_unregister_missing_task_returns_false()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- *... and 15 more nodes in this community*

## Relationships

- [Feature Requirements Document: Random Stats Generator](Feature_Requirements_Document-_Random_Stats_Generator.md) (16 shared connections)
- [Semgrep Configuration](Semgrep_Configuration.md) (7 shared connections)
- [Room](Room.md) (5 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (3 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (3 shared connections)
- [EventHandler](EventHandler.md) (3 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [Player](Player.md) (2 shared connections)
- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/tests/unit/app/test_task_registry.py`

## Audit Trail

- EXTRACTED: 126 (87%)
- INFERRED: 19 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*