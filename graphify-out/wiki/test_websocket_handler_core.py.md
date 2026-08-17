# test_websocket_handler_core.py

> 72 nodes

## Key Concepts

- **test_websocket_handler_core.py** (43 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **asyncio** (28 connections)
- **handle_websocket_message()** (11 connections) — `server/realtime/websocket_handler.py`
- **test_handle_chat_message()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_empty_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_single_word_no_args()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_whitespace_only()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_with_provided_args()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
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
- **test_send_system_message()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **WebSocket** (4 connections)
- **test_cleanup_connection()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- *... and 47 more nodes in this community*

## Relationships

- [handle_game_command](handle_game_command.md) (11 shared connections)
- [ConnectionManager](ConnectionManager.md) (5 shared connections)
- [ErrorType](ErrorType.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [send_system_message](send_system_message.md) (3 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (2 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [test_websocket_handler_coverage_gaps.py](test_websocket_handler_coverage_gaps.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`

## Audit Trail

- EXTRACTED: 121 (90%)
- INFERRED: 14 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*