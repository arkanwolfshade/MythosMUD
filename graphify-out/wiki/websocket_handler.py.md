# websocket_handler.py

> 113 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_helpers.py** (42 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **ErrorMessages** (32 connections) — `server/error_types.py`
- **websocket_handler_message_loop.py** (27 connections) — `server/realtime/websocket_handler_message_loop.py`
- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_error_handling.py** (10 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (9 connections)
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **load_player_mute_data()** (8 connections) — `server/realtime/websocket_helpers.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- **test_send_error_response_disconnected()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **test_send_error_response_success()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_check_shutdown_and_reject_not_shutting_down()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- *... and 88 more nodes in this community*

## Relationships

- [websocket_handler_commands.py](websocket_handler_commands.py.md) (15 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (15 shared connections)
- [ErrorType](ErrorType.md) (14 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (13 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (11 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (8 shared connections)
- [test_websocket_handler_helpers_extended.py](test_websocket_handler_helpers_extended.py.md) (7 shared connections)
- [build_event](build_event.md) (6 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (3 shared connections)
- [players/__init__.py](players-__init__.py.md) (3 shared connections)

## Source Files

- `server/error_types.py`
- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 271 (90%)
- INFERRED: 31 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*