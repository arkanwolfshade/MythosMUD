# test_websocket_helpers.py

> 88 nodes

## Key Concepts

- **test_websocket_helpers.py** (42 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **websocket_handler_message_loop.py** (27 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (9 connections)
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_check_shutdown_and_reject_not_shutting_down()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_shutting_down()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_websocket_disconnect()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_empty()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_filters_uuid()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_none()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_load_player_mute_data_import_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- *... and 63 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (26 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (14 shared connections)
- [build_event](build_event.md) (11 shared connections)
- [ErrorType](ErrorType.md) (6 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (1 shared connections)
- [handle_game_command](handle_game_command.md) (1 shared connections)
- [.send_message](send_message.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 179 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*