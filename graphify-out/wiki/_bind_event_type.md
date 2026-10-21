# ._bind_event_type

> 47 nodes · cohesion 0.07

## Key Concepts

- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **asyncio** (16 connections)
- **event_handler()** (7 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **fixture** (4 connections)
- **test_event_handler_handle_npc_entered()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_npc_left()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_delirium_respawned()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_died()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_dp_decay()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_dp_updated()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_entered()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_left()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_respawned()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_xp_awarded()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_room_occupants_update_internal_error()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **mock_task_registry()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_create_player_entered_message()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_create_player_left_message()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_get_room_occupants()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_occupants_snapshot_to_player()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_room_occupants_update()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_room_occupants_update_internal_personalizes()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_room_occupants_update_internal_success()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- *... and 22 more nodes in this community*

## Relationships

- [BaseEvent](BaseEvent.md) (7 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [PlayerRespawnWrapper](PlayerRespawnWrapper.md) (4 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [ADR-023: Package Ownership (`game/` vs `services/` vs `npc/`) and Fan-Out Watch List](ADR-023-_Package_Ownership_`game-`_vs_`services-`_vs_`npc-`_and_Fan-Out_Watch_List.md) (2 shared connections)
- [look_container.py](look_container.py.md) (2 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (2 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)
- [command_parser.py](command_parser.py.md) (1 shared connections)
- [test_disconnect_catchup.py](test_disconnect_catchup.py.md) (1 shared connections)
- [test_room_subscription_manager_drops.py](test_room_subscription_manager_drops.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_event_handler.py`

## Audit Trail

- EXTRACTED: 86 (83%)
- INFERRED: 17 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*