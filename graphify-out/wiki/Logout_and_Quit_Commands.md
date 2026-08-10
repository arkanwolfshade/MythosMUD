# Logout and Quit Commands

> 95 nodes

## Key Concepts

- **websocket_handler_commands.py** (32 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (28 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **resolve_websocket_connection_manager()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **_websocket_unified_command_result()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **create_websocket_request_context()** (9 connections) — `server/realtime/request_context.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **is_client_disconnected_exception()** (6 connections) — `server/realtime/websocket_helpers.py`
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
- **test_handle_game_command_empty_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_whitespace_only()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_single_word_no_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- *... and 70 more nodes in this community*

## Relationships

- [Player Combat XP](Player_Combat_XP.md) (25 shared connections)
- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (6 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (6 shared connections)
- [Combat Command Helpers](Combat_Command_Helpers.md) (6 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [Game State Provider](Game_State_Provider.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (2 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (1 shared connections)

## Source Files

- `server/realtime/request_context.py`
- `server/realtime/websocket_handler_commands.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 295 (86%)
- INFERRED: 47 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*