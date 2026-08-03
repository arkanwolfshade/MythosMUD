# websocket validation realtime

> 52 nodes

## Key Concepts

- **test_websocket_handler_validation_errors.py** (39 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_validation_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_restores_csrf_from_message_jwt_when_metadata_token_missing()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_chat_message_no_player()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_chat_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_websocket_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_system_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_process_websocket_command_player_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_is_websocket_disconnected()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_check_rate_limit_no_connection_id()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_check_rate_limit_passed()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_check_rate_limit_exceeded()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_success()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_passes_expected_token_from_connection_metadata()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_websocket_disconnect()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_runtime_error_disconnected()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_runtime_error_close_message()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_runtime_error_other()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_websocket_disconnect()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_websocket_disconnect_no_connection_id()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_runtime_error_disconnected()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_runtime_error_other()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_process_exception_in_message_loop()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_cleanup_connection_exception()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_cleanup_connection_runtime_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- *... and 27 more nodes in this community*

## Relationships

- [room look commands](room_look_commands.md) (9 shared connections)
- [realtime player connection](realtime_player_connection.md) (5 shared connections)
- [realtime message validator](realtime_message_validator.md) (4 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)

## Source Files

- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 121 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*