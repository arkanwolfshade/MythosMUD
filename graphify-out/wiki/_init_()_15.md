# . init ()

> 23 nodes

## Key Concepts

- **MessageHandler** (14 connections) — `server/realtime/message_handler_factory.py`
- **.__init__()** (8 connections) — `server/realtime/message_handler_factory.py`
- **ChatMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **PingMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **ClientErrorReportMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **FollowResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **PartyInviteResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **.register_handler()** (3 connections) — `server/realtime/message_handler_factory.py`
- **test_chat_message_handler_handle()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_ping_message_handler_handle()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_client_error_report_handler_logs()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **ABC** (2 connections)
- **Abstract base class for message handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for chat messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for ping messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for follow_response messages (accept/decline follow request).** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for party_invite_response messages (accept/decline party invite).** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for client_error_report messages (client-reported errors for server logg** (1 connections) — `server/realtime/message_handler_factory.py`
- **Initialize the factory with registered handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Register a new message handler.          Args:             message_type: The mes** (1 connections) — `server/realtime/message_handler_factory.py`
- **Test ChatMessageHandler.handle() calls handle_chat_message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test PingMessageHandler.handle() calls handle_ping_message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test ClientErrorReportMessageHandler logs via logger.error.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`

## Relationships

- [MessageHandlerFactory](MessageHandlerFactory.md) (10 shared connections)
- [Any](Any.md) (7 shared connections)
- [processing](processing.md) (6 shared connections)
- [init](init.md) (1 shared connections)
- [message broker](message_broker.md) (1 shared connections)
- [get asyncpg server settings for](get_asyncpg_server_settings_for.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 78 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*