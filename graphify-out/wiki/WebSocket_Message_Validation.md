# WebSocket Message Validation

> 32 nodes · cohesion 0.13

## Key Concepts

- **websocket_handler.py** (59 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (25 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **message_validator.py** (9 connections) — `server/realtime/message_validator.py`
- **WebSocket** (9 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **get_message_validator()** (6 connections) — `server/realtime/message_validator.py`
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_runtime_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_websocket_disconnect_message()** (6 connections) — `server/realtime/websocket_helpers.py`
- **process_websocket_inbound_message()** (5 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Exception** (5 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **ErrorType** (3 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket message validation for MythosMUD.  This module provides comprehensiv** (1 connections) — `server/realtime/message_validator.py`
- **Get the global message validator instance.** (1 connections) — `server/realtime/message_validator.py`
- **WebSocket message loop, per-message processing, and loop exception handling.** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Process a single WebSocket message.      Returns:         True to continue lo** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Handle exception in message loop.      Returns:         Tuple of (should_brea** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Process exception in message loop and return (should_break, should_raise).** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- **Handle the main WebSocket message loop.** (1 connections) — `server/realtime/websocket_handler_message_loop.py`
- *... and 7 more nodes in this community*

## Relationships

- [[WebSocket Message Validator]] (12 shared connections)
- [[Pydantic Error Handlers]] (9 shared connections)
- [[Room Occupant Events]] (8 shared connections)
- [[NPC Admin API]] (7 shared connections)
- [[WebSocket Message Handlers]] (5 shared connections)
- [[WebSocket Command Handler]] (5 shared connections)
- [[Standardized Error Responses]] (4 shared connections)
- [[WebSocket Player Helpers]] (4 shared connections)
- [[WebSocket Initial State]] (4 shared connections)
- [[Realtime WebSocket Auth]] (2 shared connections)
- [[Combat Player Broadcasts]] (2 shared connections)
- [[Help and WebSocket Core]] (2 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`

## Audit Trail

- EXTRACTED: 192 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
