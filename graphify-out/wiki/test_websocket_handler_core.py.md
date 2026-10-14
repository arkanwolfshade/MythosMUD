# test_websocket_handler_core.py

> 68 nodes

## Key Concepts

- **test_websocket_handler_core.py** (47 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **asyncio** (28 connections)
- **handle_websocket_message()** (11 connections) — `server/realtime/websocket_handler.py`
- **test_handle_websocket_message()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_chat()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_command()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception_should_break()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_chat_message()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_empty_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_single_word_no_args()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_whitespace_only()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_with_provided_args()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_aliases_dir()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_app_in_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_app_state()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_player()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_type_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_send_error_response()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_send_system_message()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **WebSocket** (4 connections)
- **test_cleanup_connection()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_json_decode_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- *... and 43 more nodes in this community*

## Relationships

- [test_websocket_handler_commands.py](test_websocket_handler_commands.py.md) (11 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (11 shared connections)
- [ErrorType](ErrorType.md) (6 shared connections)
- [test_websocket_handler_app_state_connection.py](test_websocket_handler_app_state_connection.py.md) (4 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (3 shared connections)
- [send_system_message](send_system_message.md) (3 shared connections)
- [get_help_content](get_help_content.md) (3 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (2 shared connections)
- [ValueError](ValueError.md) (2 shared connections)
- [help_content.py](help_content.py.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`

## Audit Trail

- EXTRACTED: 121 (85%)
- INFERRED: 22 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*