# message handler factory

> 107 nodes

## Key Concepts

- **message_handler_factory.py** (23 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handler_factory.py** (21 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **MessageHandlerFactory** (18 connections) — `server/realtime/message_handler_factory.py`
- **MessageHandler** (14 connections) — `server/realtime/message_handler_factory.py`
- **message_handlers.py** (14 connections) — `server/realtime/message_handlers.py`
- **test_message_handlers.py** (12 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **handle_command_message()** (11 connections) — `server/realtime/message_handlers.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_ping_message()** (10 connections) — `server/realtime/message_handlers.py`
- **CommandMessageHandler** (9 connections) — `server/realtime/message_handler_factory.py`
- **handle_follow_response_message()** (9 connections) — `server/realtime/message_handlers.py`
- **WebSocket** (8 connections)
- **Any** (8 connections)
- **.__init__()** (8 connections) — `server/realtime/message_handler_factory.py`
- **handle_party_invite_response_message()** (8 connections) — `server/realtime/message_handlers.py`
- **ChatMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **PingMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **ClientErrorReportMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **.handle_message()** (7 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (6 connections) — `server/realtime/message_handler_factory.py`
- **handle_client_error_report_message()** (6 connections) — `server/realtime/message_handlers.py`
- **WebSocket** (6 connections)
- **Any** (6 connections)
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- *... and 82 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (5 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (3 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (3 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (2 shared connections)
- [infrastructure message broker](infrastructure_message_broker.md) (1 shared connections)
- [infrastructure nats broker](infrastructure_nats_broker.md) (1 shared connections)
- [npc combat base](npc_combat_base.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 394 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*