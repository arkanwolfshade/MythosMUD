# WebSocket Command Handler

> 119 nodes · cohesion 0.03

## Key Concepts

- **websocket_handler_commands.py** (32 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (28 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_websocket_handler_app_state_connection.py** (23 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **resolve_and_setup_app_state_services()** (20 connections) — `server/realtime/websocket_handler_app_state.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **websocket_handler_app_state.py** (11 connections) — `server/realtime/websocket_handler_app_state.py`
- **resolve_websocket_connection_manager()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **_websocket_unified_command_result()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **request_context.py** (9 connections) — `server/realtime/request_context.py`
- **create_websocket_request_context()** (9 connections) — `server/realtime/request_context.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **is_client_disconnected_exception()** (6 connections) — `server/realtime/websocket_helpers.py`
- **event_handler()** (6 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_process_websocket_command_attaches_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_services_from_container()** (4 connections) — `server/realtime/websocket_handler_app_state.py`
- **_broadcast_command_room_if_needed()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_send_invalid_command_empty()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **Path** (4 connections)
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- *... and 94 more nodes in this community*

## Relationships

- [Database Manager Tests](Database_Manager_Tests.md) (22 shared connections)
- [WebSocket Request Context](WebSocket_Request_Context.md) (10 shared connections)
- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (9 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (7 shared connections)
- [WebSocket Message Validator](WebSocket_Message_Validator.md) (6 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (5 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (4 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (3 shared connections)
- [Room Planning Archive](Room_Planning_Archive.md) (2 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (2 shared connections)
- [Command Request App State](Command_Request_App_State.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)

## Source Files

- `server/realtime/request_context.py`
- `server/realtime/websocket_handler_app_state.py`
- `server/realtime/websocket_handler_commands.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`

## Audit Trail

- EXTRACTED: 404 (91%)
- INFERRED: 39 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*