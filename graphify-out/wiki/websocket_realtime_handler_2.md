# websocket realtime handler

> 63 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (25 connections) — `server/realtime/websocket_handler_message_loop.py`
- **websocket_handler_connection.py** (17 connections) — `server/realtime/websocket_handler_connection.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **cleanup_websocket_connection()** (7 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (7 connections) — `server/realtime/websocket_handler_connection.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **PlayerDisconnectService** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **AsyncPersistenceRoomLookup** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **handle_websocket_runtime_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_websocket_disconnect_message()** (6 connections) — `server/realtime/websocket_helpers.py`
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- **UUID** (5 connections)
- **process_websocket_inbound_message()** (5 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_disconnect.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_websocket_handler_helpers.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **test_websocket_handler_json_error.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- *... and 38 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (14 shared connections)
- [Room Broadcast](Room_Broadcast.md) (8 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (7 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (6 shared connections)
- [command inventory factories](command_inventory_factories.md) (6 shared connections)
- [realtime message validator](realtime_message_validator.md) (5 shared connections)
- [combat services messaging](combat_services_messaging.md) (5 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (5 shared connections)
- [room look commands](room_look_commands.md) (4 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (3 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (3 shared connections)
- [combat commands handler](combat_commands_handler.md) (2 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_json_error.py`

## Audit Trail

- EXTRACTED: 279 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*