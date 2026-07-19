# WebSocket Handler Helpers

> 50 nodes · cohesion 0.04

## Key Concepts

- **test_websocket_handler_validation_errors.py** (38 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_websocket_message_error()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_websocket_handler_helpers.py** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **test_cleanup_connection_runtime_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_chat_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_chat_message_no_player()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_with_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_process_websocket_command_player_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_runtime_error_close_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_runtime_error_disconnected()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_runtime_error_other()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_restores_csrf_from_message_jwt_when_metadata_token_missing()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_validation_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **Test _is_websocket_disconnected() returns True for disconnection messages.** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **test_is_websocket_disconnected_false()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **test_is_websocket_disconnected_true()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **Test _send_error_response handles RuntimeError with close message.** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **Test handle_game_command processes command with provided args.** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_check_rate_limit_exceeded()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_check_rate_limit_no_connection_id()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_check_rate_limit_passed()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_cleanup_connection_exception()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_websocket_disconnect()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_websocket_disconnect_no_connection_id()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_is_websocket_disconnected()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- *... and 25 more nodes in this community*

## Relationships

- [[Database Manager Tests]] (8 shared connections)
- [[WebSocket Message Validator]] (7 shared connections)
- [[WebSocket Command Handler]] (5 shared connections)
- [[Help and WebSocket Core]] (3 shared connections)
- [[Realtime Websocket Handler]] (2 shared connections)
- [[Pydantic Error Handlers]] (1 shared connections)
- [[Standardized Error Responses]] (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 122 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
