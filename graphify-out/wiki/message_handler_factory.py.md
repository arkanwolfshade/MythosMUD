# message_handler_factory.py

> 25 nodes

## Key Concepts

- **message_handler_factory.py** (23 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handler_factory.py** (21 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **MessageHandler** (14 connections) — `server/realtime/message_handler_factory.py`
- **CommandMessageHandler** (9 connections) — `server/realtime/message_handler_factory.py`
- **.__init__()** (8 connections) — `server/realtime/message_handler_factory.py`
- **ChatMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **ClientErrorReportMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **PingMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **FollowResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **PartyInviteResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handler_factory_game_command_alias()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_get_handler_found()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **ABC** (2 connections)
- **Message Handler Factory for WebSocket message routing. This module implements a…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Initialize the factory with registered handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Abstract base class for message handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for command messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for chat messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for ping messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for follow_response messages (accept/decline follow request).** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for party_invite_response messages (accept/decline party invite).** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for client_error_report messages (client-reported errors for server…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Unit tests for message handler factory. Tests the message_handler_factory…** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory handles game_command as alias for command.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.get_handler() returns handler when found.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`

## Relationships

- [MessageHandlerFactory](MessageHandlerFactory.md) (12 shared connections)
- [asyncio](asyncio.md) (11 shared connections)
- [Any](Any.md) (7 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (5 shared connections)
- [MythosMUDError](MythosMUDError.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [MessageBroker](MessageBroker.md) (1 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (1 shared connections)
- [handle_ping_message](handle_ping_message.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 78 (91%)
- INFERRED: 8 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*