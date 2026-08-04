# npc shopkeeper rationale

> 104 nodes

## Key Concepts

- **threading.py** (48 connections) — `server/npc/threading.py`
- **NPCThreadManager** (29 connections) — `server/npc/threading.py`
- **test_npc_threading_messages.py** (23 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **__init__.py** (22 connections) — `server/npc/__init__.py`
- **NPCActionMessage** (16 connections) — `server/npc/threading.py`
- **NPCMessageQueue** (16 connections) — `server/npc/threading.py`
- **NPCCommunicationBridge** (14 connections) — `server/npc/threading.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **Any** (11 connections)
- **NPCActionType** (9 connections) — `server/npc/threading.py`
- **._npc_thread_worker()** (8 connections) — `server/npc/threading.py`
- **._process_wander_action()** (8 connections) — `server/npc/threading.py`
- **run_test_ci.py** (6 connections) — `scripts/run_test_ci.py`
- **._move_with_integration()** (6 connections) — `server/npc/npc_base.py`
- **.from_dict()** (6 connections) — `server/npc/threading.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **.start_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (5 connections) — `server/npc/threading.py`
- **.restart_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._process_npc_message()** (5 connections) — `server/npc/threading.py`
- **._execute_npc_behavior()** (5 connections) — `server/npc/threading.py`
- **exception_metrics.py** (4 connections) — `server/monitoring/exception_metrics.py`
- **.to_dict()** (4 connections) — `server/npc/threading.py`
- **.from_json()** (4 connections) — `server/npc/threading.py`
- **.get_messages()** (4 connections) — `server/npc/threading.py`
- *... and 79 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (19 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (9 shared connections)
- [command parser rationale](command_parser_rationale.md) (9 shared connections)
- [idle movement npc](idle_movement_npc.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (3 shared connections)
- [logging handlers structured](logging_handlers_structured.md) (2 shared connections)
- [command exploration models](command_exploration_models.md) (2 shared connections)
- [commands logout helpers](commands_logout_helpers.md) (2 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (2 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/monitoring/exception_metrics.py`
- `server/npc/__init__.py`
- `server/npc/npc_base.py`
- `server/npc/threading.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 389 (94%)
- INFERRED: 23 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*