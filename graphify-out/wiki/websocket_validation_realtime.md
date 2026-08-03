# websocket validation realtime

> 74 nodes

## Key Concepts

- **test_websocket_handler_validation_errors.py** (39 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **send_system_message()** (13 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_system_message.py** (8 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_send_system_message_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_warning()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_disconnected()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_validate_message_validation_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_restores_csrf_from_message_jwt_when_metadata_token_missing()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_with_broadcast()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_player()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_with_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_websocket_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_system_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_process_websocket_command_player_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **mock_websocket()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_is_websocket_disconnected()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_check_rate_limit_no_connection_id()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_check_rate_limit_passed()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_check_rate_limit_exceeded()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_success()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_passes_expected_token_from_connection_metadata()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- *... and 49 more nodes in this community*

## Relationships

- [websocket handler realtime](websocket_handler_realtime.md) (14 shared connections)
- [realtime message validator](realtime_message_validator.md) (4 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 174 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*