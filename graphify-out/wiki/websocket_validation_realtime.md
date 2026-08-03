# websocket validation realtime

> 84 nodes

## Key Concepts

- **test_websocket_handler_validation_errors.py** (39 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **is_client_disconnected_exception()** (6 connections) — `server/realtime/websocket_helpers.py`
- **_send_invalid_command_empty()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_broadcast_command_room_if_needed()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **test_handle_game_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_empty_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_whitespace_only()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_single_word_no_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_with_provided_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_resolve_connection_manager_from_app()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_game_command_exception_handling()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_game_command_runtime_error_handling()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_validate_message_validation_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_validate_message_restores_csrf_from_message_jwt_when_metadata_token_missing()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_chat_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_with_broadcast()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_player()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_with_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_websocket_message_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_process_websocket_command_player_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **WebSocket** (2 connections)
- **test_handle_game_command_empty_sends_invalid_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- *... and 59 more nodes in this community*

## Relationships

- [websocket handler realtime](websocket_handler_realtime.md) (11 shared connections)
- [room look commands](room_look_commands.md) (9 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (6 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (4 shared connections)
- [realtime message validator](realtime_message_validator.md) (4 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (3 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_commands.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 189 (87%)
- INFERRED: 28 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*