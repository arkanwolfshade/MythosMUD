# WebSocket Message Handlers

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

- [WebSocket Command Handler](WebSocket_Command_Handler.md) (9 shared connections)
- [Database Manager Tests](Database_Manager_Tests.md) (9 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (8 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (7 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (5 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Npc Event Reaction](Npc_Event_Reaction.md) (4 shared connections)
- [Async Room Cache Tests](Async_Room_Cache_Tests.md) (3 shared connections)
- [WebSocket Player Helpers](WebSocket_Player_Helpers.md) (3 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (2 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (1 shared connections)

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