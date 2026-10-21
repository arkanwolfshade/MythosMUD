# test_player_presence_tracker.py

> 89 nodes · cohesion 0.04

## Key Concepts

- **NPCThreadManager** (62 connections) — `server/npc/threading.py`
- **test_npc_thread_manager_internals.py** (32 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **asyncio** (17 connections)
- **._execute_wander_movement()** (7 connections) — `server/npc/threading.py`
- **._parse_behavior_config()** (7 connections) — `server/npc/threading.py`
- **._npc_thread_worker()** (6 connections) — `server/npc/threading.py`
- **._execute_npc_behavior()** (5 connections) — `server/npc/threading.py`
- **._process_wander_action()** (5 connections) — `server/npc/threading.py`
- **.restart_npc_thread()** (5 connections) — `server/npc/threading.py`
- **.start_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._process_npc_message()** (4 connections) — `server/npc/threading.py`
- **._resolve_wander_npc()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (4 connections) — `server/npc/threading.py`
- **test_bridge_send_message_to_npc_swallows_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_no_instance_service()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_npc_not_active()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_success()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_swallows_inner_execute_error()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_swallows_outer_unexpected_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_parse_behavior_config_dict_attr()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_parse_behavior_config_invalid_json_string()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_parse_behavior_config_json_non_dict()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_parse_behavior_config_valid_json_string()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_process_wander_action_handles_unexpected_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- *... and 64 more nodes in this community*

## Relationships

- [StatisticsAggregator](StatisticsAggregator.md) (11 shared connections)
- [ErrorType](ErrorType.md) (5 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (2 shared connections)
- [command_parser.py](command_parser.py.md) (2 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)
- [Domain Model Anemic Anti-Pattern Audit](Domain_Model_Anemic_Anti-Pattern_Audit.md) (1 shared connections)
- [dependencies](dependencies.md) (1 shared connections)
- [websocket_integration.py](websocket_integration.py.md) (1 shared connections)
- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_thread_manager_internals.py`

## Audit Trail

- EXTRACTED: 144 (81%)
- INFERRED: 33 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*