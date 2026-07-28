# Server Realtime (13)

> 85 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (12 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **websocket_handler_validation.py** (10 connections) — `server/realtime/websocket_handler_validation.py`
- **websocket_handler_connection.py** (8 connections) — `server/realtime/websocket_handler_connection.py`
- **WebSocket** (7 connections)
- **setup_initial_connection_state()** (7 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (6 connections)
- **is_client_disconnected_exception()** (6 connections) — `server/realtime/websocket_helpers.py`
- **cleanup_websocket_connection()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **resolve_expected_csrf_token()** (6 connections) — `server/realtime/websocket_handler_validation.py`
- **UUID** (5 connections)
- **PlayerDisconnectService** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **AsyncPersistenceRoomLookup** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **send_welcome_event()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **send_websocket_error_response()** (5 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_runtime_error()** (5 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (5 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (5 connections) — `server/realtime/websocket_handler_message_loop.py`
- **validate_message_csrf_and_restore_metadata()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **validate_websocket_message()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **WebSocket** (4 connections)
- *... and 60 more nodes in this community*

## Relationships

- [Server Realtime (17)](Server_Realtime_%2817%29.md) (7 shared connections)
- [Server Realtime (36)](Server_Realtime_%2836%29.md) (6 shared connections)
- [Server Realtime (21)](Server_Realtime_%2821%29.md) (6 shared connections)
- [Server Realtime (6)](Server_Realtime_%286%29.md) (4 shared connections)
- [Server Realtime (54)](Server_Realtime_%2854%29.md) (3 shared connections)
- [Server Realtime (9)](Server_Realtime_%289%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Error Handlers (2)](Server_Error_Handlers_%282%29.md) (2 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (2 shared connections)
- [Server Realtime (34)](Server_Realtime_%2834%29.md) (2 shared connections)
- [Server Api (9)](Server_Api_%289%29.md) (1 shared connections)
- [Server Error Handlers](Server_Error_Handlers.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_handler_validation.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_json_error.py`

## Audit Trail

- EXTRACTED: 309 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*