# message_handler_factory.py

> 36 nodes

## Key Concepts

- **message_handler_factory.py** (24 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handler_factory.py** (22 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **MessageHandler** (12 connections) — `server/realtime/message_handler_factory.py`
- **CommandMessageHandler** (9 connections) — `server/realtime/message_handler_factory.py`
- **.__init__()** (8 connections) — `server/realtime/message_handler_factory.py`
- **ChatMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **ClientErrorReportMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **PingMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **asyncio** (7 connections)
- **FollowResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **PartyInviteResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **test_chat_message_handler_handle()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_client_error_report_handler_logs()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_command_message_handler_handle()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_no_type()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_success()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_unknown_type()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_ping_message_handler_handle()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **ABC** (2 connections)
- **Message Handler Factory for WebSocket message routing. This module implements a…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Initialize the factory with registered handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Abstract base class for message handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for command messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for chat messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for ping messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- *... and 11 more nodes in this community*

## Relationships

- [MessageHandlerFactory](MessageHandlerFactory.md) (17 shared connections)
- [Any](Any.md) (7 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (6 shared connections)
- [ErrorType](ErrorType.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (1 shared connections)
- [User](User.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 90 (91%)
- INFERRED: 9 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*