# websocket_handler.py

> 36 nodes · cohesion 0.07

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (25 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_runtime_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **is_websocket_disconnect_message()** (6 connections) — `server/realtime/websocket_helpers.py`
- **process_websocket_inbound_message()** (5 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_disconnect.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_websocket_handler_helpers.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **test_websocket_handler_json_error.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- **Exception** (3 connections)
- **test_handle_websocket_disconnect()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_handle_websocket_disconnect_no_connection_id()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_is_websocket_disconnected_false()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **test_is_websocket_disconnected_true()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **mock_websocket()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- **test_handle_json_decode_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- **WebSocket message loop, per-message processing, and loop exception handling.  Ex** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- *... and 11 more nodes in this community*

## Relationships

- [websocket_handler_commands.py](websocket_handler_commands.py.md) (9 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (9 shared connections)
- [error_types.py](error_types.py.md) (8 shared connections)
- [ConnectionManager](ConnectionManager.md) (7 shared connections)
- [MythosMUDError](MythosMUDError.md) (5 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (4 shared connections)
- [cleanup_websocket_connection](cleanup_websocket_connection.md) (3 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [real_time.py](real_time.py.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_json_error.py`

## Audit Trail

- EXTRACTED: 203 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*