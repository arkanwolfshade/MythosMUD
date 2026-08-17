# server container main get container

> 129 nodes

## Key Concepts

- **test_message_handlers.py** (26 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **message_handler_factory.py** (24 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handler_factory.py** (22 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **MessageHandlerFactory** (18 connections) — `server/realtime/message_handler_factory.py`
- **asyncio** (16 connections)
- **message_handlers.py** (15 connections) — `server/realtime/message_handlers.py`
- **MessageHandler** (14 connections) — `server/realtime/message_handler_factory.py`
- **handle_follow_response_message()** (14 connections) — `server/realtime/message_handlers.py`
- **handle_party_invite_response_message()** (13 connections) — `server/realtime/message_handlers.py`
- **handle_command_message()** (11 connections) — `server/realtime/message_handlers.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_ping_message()** (10 connections) — `server/realtime/message_handlers.py`
- **CommandMessageHandler** (9 connections) — `server/realtime/message_handler_factory.py`
- **.__init__()** (8 connections) — `server/realtime/message_handler_factory.py`
- **handle_client_error_report_message()** (8 connections) — `server/realtime/message_handlers.py`
- **Any** (8 connections)
- **WebSocket** (8 connections)
- **ChatMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **ClientErrorReportMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **PingMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **asyncio** (7 connections)
- **.handle_message()** (6 connections) — `server/realtime/message_handler_factory.py`
- **Any** (6 connections)
- **WebSocket** (6 connections)
- *... and 104 more nodes in this community*

## Relationships

- [server realtime envelope build event](server_realtime_envelope_build_event.md) (7 shared connections)
- [server container main applicationcontainer reset](server_container_main_applicationcontainer_reset.md) (6 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (3 shared connections)
- [aliasrecord](aliasrecord.md) (2 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (2 shared connections)
- [followtargetvalue](followtargetvalue.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)
- [server infrastructure init](server_infrastructure_init.md) (1 shared connections)
- [server infrastructure message broker](server_infrastructure_message_broker.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/realtime/message_handler_factory.py`
- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 268 (94%)
- INFERRED: 18 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*