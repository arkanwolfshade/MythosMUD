# websocket_handler.py

> 62 nodes

## Key Concepts

- **websocket_handler.py** (65 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (27 connections) — `server/realtime/websocket_handler_message_loop.py`
- **websocket_handler_connection.py** (18 connections) — `server/realtime/websocket_handler_connection.py`
- **handle_websocket_message()** (11 connections) — `server/realtime/websocket_handler.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- **cleanup_websocket_connection()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (5 connections)
- **AsyncPersistenceRoomLookup** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **PlayerDisconnectService** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_disconnect.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_websocket_handler_helpers.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- *... and 37 more nodes in this community*

## Relationships

- [ErrorType](ErrorType.md) (16 shared connections)
- [test_websocket_handler_coverage_gaps.py](test_websocket_handler_coverage_gaps.py.md) (10 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (5 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (5 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (4 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (4 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (3 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`

## Audit Trail

- EXTRACTED: 174 (91%)
- INFERRED: 18 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*