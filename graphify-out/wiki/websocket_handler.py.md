# websocket_handler.py

> 51 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (27 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **test_websocket_handler_json_error.py** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_disconnect.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_websocket_handler_helpers.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **mock_websocket()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- **test_handle_json_decode_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- **Exception** (3 connections)
- **test_handle_websocket_disconnect()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_handle_websocket_disconnect_no_connection_id()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_is_websocket_disconnected_false()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **test_is_websocket_disconnected_true()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- *... and 26 more nodes in this community*

## Relationships

- [ErrorType](ErrorType.md) (12 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (11 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (9 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [build_event](build_event.md) (6 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (5 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (4 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (4 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (2 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_json_error.py`

## Audit Trail

- EXTRACTED: 141 (89%)
- INFERRED: 18 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*