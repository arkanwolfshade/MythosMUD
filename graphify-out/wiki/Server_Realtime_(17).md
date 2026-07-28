# Server Realtime (17)

> 76 nodes

## Key Concepts

- **websocket_handler_commands.py** (32 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (28 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **resolve_websocket_connection_manager()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **_websocket_unified_command_result()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **event_handler()** (6 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_process_websocket_command_attaches_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_send_invalid_command_empty()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_broadcast_command_room_if_needed()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **Path** (4 connections)
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_invoke_get_room_state_event()** (3 connections) — `server/realtime/websocket_handler_commands.py`
- **test_handle_game_command_broadcasts_when_result_requests()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_game_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_with_provided_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_player()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_app_state()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_app_in_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- *... and 51 more nodes in this community*

## Relationships

- [Server Realtime (34)](Server_Realtime_%2834%29.md) (11 shared connections)
- [Server Realtime (13)](Server_Realtime_%2813%29.md) (7 shared connections)
- [Server Realtime (29)](Server_Realtime_%2829%29.md) (6 shared connections)
- [Server Realtime (36)](Server_Realtime_%2836%29.md) (5 shared connections)
- [Server Error Handlers (2)](Server_Error_Handlers_%282%29.md) (4 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (4 shared connections)
- [Server Realtime (54)](Server_Realtime_%2854%29.md) (3 shared connections)
- [Server Realtime (44)](Server_Realtime_%2844%29.md) (3 shared connections)
- [Server Commands (3)](Server_Commands_%283%29.md) (2 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (2 shared connections)
- [Server Realtime (38)](Server_Realtime_%2838%29.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 257 (86%)
- INFERRED: 42 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*