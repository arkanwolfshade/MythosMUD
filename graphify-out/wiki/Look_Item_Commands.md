# Look Item Commands

> 25 nodes

## Key Concepts

- **websocket_handler_message_loop.py** (25 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **handle_websocket_runtime_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_websocket_disconnect_message()** (6 connections) — `server/realtime/websocket_helpers.py`
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
- **Check if error message indicates WebSocket disconnection or send-after-close.** (1 connections) — `server/realtime/websocket_helpers.py`

## Relationships

- [Player Combat XP](Player_Combat_XP.md) (11 shared connections)
- [Database Helper Tests](Database_Helper_Tests.md) (4 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (3 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (3 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (1 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (1 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`

## Audit Trail

- EXTRACTED: 114 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*