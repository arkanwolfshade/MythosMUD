# Community 346

> 49 nodes

## Key Concepts

- **test_websocket_handler_commands.py** (37 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **handle_game_command()** (31 connections) — `server/realtime/websocket_handler_commands.py`
- **asyncio** (16 connections)
- **resolve_websocket_connection_manager()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **Path** (9 connections)
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_run_game_command_with_unified_result()** (8 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (7 connections) — `server/realtime/websocket_handler_commands.py`
- **test_command_response_defaults_to_command_output_category()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_command_response_keeps_a_handler_supplied_category()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_attaches_room_state()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_room_broadcast_defaults_to_command_output_category()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_room_broadcast_uses_broadcast_category_override()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_player_cm()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_game_command_broadcasts_when_result_requests()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_player_not_found_is_system_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_missing_room_attr()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_invoke_get_room_state_event()** (3 connections) — `server/realtime/websocket_handler_commands.py`
- **_send_invalid_command_empty()** (3 connections) — `server/realtime/websocket_handler_commands.py`
- **test_attach_room_state_to_result_adds_room_state_when_available()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- *... and 24 more nodes in this community*

## Relationships

- [WebSocket Message Types](WebSocket_Message_Types.md) (14 shared connections)
- [Community 41](Community_41.md) (12 shared connections)
- [Community 229](Community_229.md) (7 shared connections)
- [Community 98](Community_98.md) (6 shared connections)
- [Community 271](Community_271.md) (5 shared connections)
- [NPC Movement Events](NPC_Movement_Events.md) (2 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (1 shared connections)
- [Community 164](Community_164.md) (1 shared connections)
- [Community 329](Community_329.md) (1 shared connections)
- [Community 212](Community_212.md) (1 shared connections)
- [Community 78](Community_78.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`

## Audit Trail

- EXTRACTED: 130 (85%)
- INFERRED: 23 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*