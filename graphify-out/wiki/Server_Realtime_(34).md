# Server Realtime (34)

> 54 nodes

## Key Concepts

- **test_websocket_handler_core.py** (42 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **handle_websocket_message()** (10 connections) — `server/realtime/websocket_handler.py`
- **test_handle_generic_exception()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception_should_break()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_with_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_send_system_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_chat_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_empty_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_whitespace_only()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_single_word_no_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_chat()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test handle_websocket_message routes message.** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_send_error_response()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_json_decode_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_runtime_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_message_loop_exception_json_decode()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_message_loop_exception_disconnect()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_message()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_message_rate_limit_exceeded()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_validate_player_and_persistence_success()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_validate_player_and_persistence_not_found()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- *... and 29 more nodes in this community*

## Relationships

- [Server Realtime (17)](Server_Realtime_%2817%29.md) (11 shared connections)
- [Server Realtime (36)](Server_Realtime_%2836%29.md) (5 shared connections)
- [Server Error Handlers (2)](Server_Error_Handlers_%282%29.md) (4 shared connections)
- [Server Commands (3)](Server_Commands_%283%29.md) (3 shared connections)
- [Server Realtime (13)](Server_Realtime_%2813%29.md) (2 shared connections)
- [Server Realtime (29)](Server_Realtime_%2829%29.md) (2 shared connections)
- [Server Error Handlers](Server_Error_Handlers.md) (1 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`

## Audit Trail

- EXTRACTED: 139 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*