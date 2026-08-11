# Multiplayer Browser Helpers

> 20 nodes

## Key Concepts

- **WebSocket** (8 connections)
- **Any** (8 connections)
- **.handle_message()** (7 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (6 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.get_handler()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (4 connections) — `server/realtime/message_handler_factory.py`
- **Handle a specific message type.          Args:             websocket: The WebSoc** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle command message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle chat message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle ping message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle follow_response message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle party_invite_response message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle client_error_report message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Get a handler for the specified message type.          Args:             message** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle a WebSocket message using the appropriate handler.          Args:** (1 connections) — `server/realtime/message_handler_factory.py`

## Relationships

- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (8 shared connections)
- [Game State Provider Tests](Game_State_Provider_Tests.md) (6 shared connections)
- [Database Error Handling](Database_Error_Handling.md) (2 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (1 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`

## Audit Trail

- EXTRACTED: 71 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*