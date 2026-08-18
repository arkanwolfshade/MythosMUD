# server realtime message handler factory

> 76 nodes

## Key Concepts

- **message_handler_factory.py** (24 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handler_factory.py** (22 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **MessageHandlerFactory** (18 connections) — `server/realtime/message_handler_factory.py`
- **MessageHandler** (14 connections) — `server/realtime/message_handler_factory.py`
- **CommandMessageHandler** (9 connections) — `server/realtime/message_handler_factory.py`
- **.__init__()** (8 connections) — `server/realtime/message_handler_factory.py`
- **Any** (8 connections)
- **WebSocket** (8 connections)
- **ChatMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **ClientErrorReportMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **PingMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **asyncio** (7 connections)
- **.handle_message()** (6 connections) — `server/realtime/message_handler_factory.py`
- **FollowResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **PartyInviteResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.get_handler()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (4 connections) — `server/realtime/message_handler_factory.py`
- **test_chat_message_handler_handle()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_client_error_report_handler_logs()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- *... and 51 more nodes in this community*

## Relationships

- [server container main get container](server_container_main_get_container.md) (12 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server infrastructure init](server_infrastructure_init.md) (1 shared connections)
- [server infrastructure message broker](server_infrastructure_message_broker.md) (1 shared connections)
- [server npc combat integration base](server_npc_combat_integration_base.md) (1 shared connections)
- [server error types errormessages](server_error_types_errormessages.md) (1 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 145 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*