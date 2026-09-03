# Message Handler Factory

> 18 nodes

## Key Concepts

- **WebSocket** (8 connections)
- **WebSocketInboundMessage** (8 connections)
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle_message()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (4 connections) — `server/realtime/message_handler_factory.py`
- **Handle follow_response message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle party_invite_response message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle client_error_report message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle a validated WebSocket message using the appropriate handler.…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle a specific message type. Args: websocket: The WebSocket connection…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle command message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle chat message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle ping message type.** (1 connections) — `server/realtime/message_handler_factory.py`

## Relationships

- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (15 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*