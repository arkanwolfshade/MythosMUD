# test websocket handler helpers extended

> 48 nodes

## Key Concepts

- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_entered()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_left()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_npc_entered()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_npc_left()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_xp_awarded()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_dp_updated()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_died()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_dp_decay()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_respawned()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_delirium_respawned()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_create_player_entered_message()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_create_player_left_message()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **mock_task_registry()** (2 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_subscribe_to_events()** (2 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_get_next_sequence()** (2 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_room_occupants_update_internal_success()** (2 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_room_occupants_update_internal_error()** (2 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_room_occupants_update()** (2 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_get_room_occupants()** (2 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_occupants_snapshot_to_player()** (2 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_shutdown()** (2 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **Unit tests for event handler.  Tests the event_handler module classes and functi** (1 connections) — `server/tests/unit/realtime/test_event_handler.py`
- *... and 23 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (13 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (4 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [combat initialization](combat_initialization.md) (2 shared connections)
- [.set player combat service()](set_player_combat_service%28%29.md) (2 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [.is required()](is_required%28%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_event_handler.py`

## Audit Trail

- EXTRACTED: 111 (90%)
- INFERRED: 12 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*