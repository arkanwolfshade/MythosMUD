# test_websocket_handler_commands.py

> 68 nodes

## Key Concepts

- **test_websocket_handler_commands.py** (41 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **websocket_handler_commands.py** (36 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_game_command()** (32 connections) — `server/realtime/websocket_handler_commands.py`
- **process_websocket_command()** (20 connections) — `server/realtime/websocket_handler_commands.py`
- **resolve_and_setup_app_state_services()** (19 connections) — `server/realtime/websocket_handler_app_state.py`
- **asyncio** (18 connections)
- **create_websocket_request_context()** (11 connections) — `server/realtime/request_context.py`
- **Path** (11 connections)
- **resolve_websocket_connection_manager()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **_run_game_command_with_unified_result()** (10 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **_websocket_unified_command_result()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_player_cm()** (7 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_command_response_keeps_system_error_from_command_error()** (7 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **test_command_response_carries_the_handlers_segments_untouched()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_command_response_defaults_to_command_output_category()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_command_response_keeps_a_handler_supplied_category()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_attaches_room_state()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_room_broadcast_defaults_to_command_output_category()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_room_broadcast_uses_broadcast_category_override()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- *... and 43 more nodes in this community*

## Relationships

- [test_websocket_handler_app_state_connection.py](test_websocket_handler_app_state_connection.py.md) (17 shared connections)
- [MessageCategory](MessageCategory.md) (12 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (11 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (6 shared connections)
- [ErrorType](ErrorType.md) (6 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (6 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (5 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (3 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [look_command.py](look_command.py.md) (2 shared connections)

## Source Files

- `server/realtime/request_context.py`
- `server/realtime/websocket_handler_app_state.py`
- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`

## Audit Trail

- EXTRACTED: 213 (87%)
- INFERRED: 33 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*