# server realtime websocket handler handle

> 81 nodes

## Key Concepts

- **test_websocket_handler_validation_errors.py** (40 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **asyncio** (25 connections)
- **handle_chat_message()** (17 connections) — `server/realtime/websocket_handler.py`
- **send_system_message()** (13 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_system_message.py** (9 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_validate_message_validation_error()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_system_message_disconnected()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_warning()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_handle_chat_message_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_chat_message_no_player()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_current_room_id()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_player()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_with_args()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_with_broadcast()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_websocket_message_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_process_websocket_command_player_no_current_room_id()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_runtime_error_close_message()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_runtime_error_disconnected()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_runtime_error_other()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_websocket_disconnect()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_system_message_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_restores_csrf_from_message_jwt_when_metadata_token_missing()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- *... and 56 more nodes in this community*

## Relationships

- [server realtime websocket handler commands](server_realtime_websocket_handler_commands.md) (14 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (8 shared connections)
- [server realtime websocket handler app](server_realtime_websocket_handler_app.md) (5 shared connections)
- [server container main get container](server_container_main_get_container.md) (4 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (4 shared connections)
- [server realtime message validator](server_realtime_message_validator.md) (4 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 144 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*