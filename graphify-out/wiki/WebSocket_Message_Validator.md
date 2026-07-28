# WebSocket Message Validator

> 62 nodes · cohesion 0.03

## Key Concepts

- **test_websocket_handler_validation_errors.py** (39 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_chat_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_chat_message_no_player()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_player()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_with_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_with_broadcast()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_websocket_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_process_websocket_command_player_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_system_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_restores_csrf_from_message_jwt_when_metadata_token_missing()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_validation_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_check_rate_limit_exceeded()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_check_rate_limit_no_connection_id()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_check_rate_limit_passed()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_cleanup_connection_exception()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_cleanup_connection_runtime_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_runtime_error_disconnected()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_runtime_error_other()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_websocket_disconnect()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_websocket_disconnect_no_connection_id()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_is_websocket_disconnected()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_process_exception_in_message_loop()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_send_error_response_runtime_error_close_message()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- *... and 37 more nodes in this community*

## Relationships

- [Database Manager Tests](Database_Manager_Tests.md) (7 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (6 shared connections)
- [Npc Event Reaction](Npc_Event_Reaction.md) (4 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 136 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*