# test_websocket_handler_core.py

> 70 nodes

## Key Concepts

- **test_websocket_handler_core.py** (43 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **asyncio** (28 connections)
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **_websocket_unified_command_result()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_websocket_message()** (11 connections) — `server/realtime/websocket_handler.py`
- **test_handle_game_command_empty_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_whitespace_only()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception_should_break()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_chat()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_aliases_dir()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_app_in_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_app_state()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_player()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_type_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_send_error_response()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_process_websocket_command_player_no_current_room_id()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **WebSocket** (4 connections)
- **test_cleanup_connection()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_with_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- *... and 45 more nodes in this community*

## Relationships

- [handle_game_command](handle_game_command.md) (9 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (9 shared connections)
- [test_websocket_handler_commands.py](test_websocket_handler_commands.py.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [send_system_message](send_system_message.md) (4 shared connections)
- [test_websocket_handler_app_state_connection.py](test_websocket_handler_app_state_connection.py.md) (2 shared connections)
- [.state](state.md) (2 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (2 shared connections)
- [test_websocket_handler_coverage_gaps.py](test_websocket_handler_coverage_gaps.py.md) (1 shared connections)
- [look_command.py](look_command.py.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 139 (90%)
- INFERRED: 15 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*