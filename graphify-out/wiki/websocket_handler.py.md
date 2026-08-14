# websocket_handler.py

> 57 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (26 connections) — `server/realtime/websocket_handler_message_loop.py`
- **websocket_handler_connection.py** (17 connections) — `server/realtime/websocket_handler_connection.py`
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
- **AsyncPersistenceRoomLookup** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **PlayerDisconnectService** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **cleanup_websocket_connection()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (5 connections)
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_disconnect.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_websocket_handler_helpers.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **Exception** (3 connections)
- **.get_room_by_id()** (2 connections) — `server/realtime/websocket_handler_connection.py`
- *... and 32 more nodes in this community*

## Relationships

- [.state](state.md) (11 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (9 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [ErrorType](ErrorType.md) (8 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (7 shared connections)
- [ConnectionManager](ConnectionManager.md) (5 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (5 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (4 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`

## Audit Trail

- EXTRACTED: 158 (88%)
- INFERRED: 21 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*