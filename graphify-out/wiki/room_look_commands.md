# room look commands

> 23 nodes

## Key Concepts

- **websocket_handler_message_loop.py** (26 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (5 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Exception** (3 connections)
- **WebSocket message loop, per-message processing, and loop exception handling.  Ex** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Send error response to client.      Returns:         True if sent successfully,** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Handle JSON decode error.** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Handle WebSocket disconnect.      Returns:         True to break the loop** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Handle RuntimeError.      Returns:         Tuple of (should_break, should_raise)** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Handle generic exception.      Returns:         True to break the loop** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Process a single WebSocket message.      Returns:         True to continue loop,** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Handle exception in message loop.      Returns:         Tuple of (should_break,** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Process exception in message loop and return (should_break, should_raise).** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Handle the main WebSocket message loop.** (1 connections) — `server/realtime/websocket_handler_message_loop.py`

## Relationships

- [combat schemas schema](combat_schemas_schema.md) (10 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (6 shared connections)
- [room websocket updates](room_websocket_updates.md) (6 shared connections)
- [realtime message validator](realtime_message_validator.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (1 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_message_loop.py`

## Audit Trail

- EXTRACTED: 110 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*