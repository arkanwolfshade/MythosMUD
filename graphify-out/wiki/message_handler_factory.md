# message handler factory

> 23 nodes

## Key Concepts

- **message_handler_factory.py** (23 connections) — `server/realtime/message_handler_factory.py`
- **MessageHandler** (14 connections) — `server/realtime/message_handler_factory.py`
- **CommandMessageHandler** (9 connections) — `server/realtime/message_handler_factory.py`
- **.__init__()** (8 connections) — `server/realtime/message_handler_factory.py`
- **ChatMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **PingMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **ClientErrorReportMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **FollowResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **PartyInviteResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **.register_handler()** (3 connections) — `server/realtime/message_handler_factory.py`
- **test_client_error_report_handler_logs()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **ABC** (2 connections)
- **Message Handler Factory for WebSocket message routing.  This module implements a** (1 connections) — `server/realtime/message_handler_factory.py`
- **Abstract base class for message handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for command messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for chat messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for ping messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for follow_response messages (accept/decline follow request).** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for party_invite_response messages (accept/decline party invite).** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for client_error_report messages (client-reported errors for server logg** (1 connections) — `server/realtime/message_handler_factory.py`
- **Initialize the factory with registered handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Register a new message handler.          Args:             message_type: The mes** (1 connections) — `server/realtime/message_handler_factory.py`
- **Test ClientErrorReportMessageHandler logs via logger.error.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`

## Relationships

- [MessageHandlerFactory](MessageHandlerFactory.md) (14 shared connections)
- [.handle()](handle%28%29.md) (8 shared connections)
- [message handlers](message_handlers.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [init](init.md) (1 shared connections)
- [message broker](message_broker.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 102 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*