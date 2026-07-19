# WebSocket Message Handlers

> 124 nodes · cohesion 0.03

## Key Concepts

- **message_handler_factory.py** (22 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handler_factory.py** (20 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **MessageHandlerFactory** (17 connections) — `server/realtime/message_handler_factory.py`
- **websocket_handler_connection.py** (17 connections) — `server/realtime/websocket_handler_connection.py`
- **get_container()** (16 connections) — `server/container/main.py`
- **message_handlers.py** (13 connections) — `server/realtime/message_handlers.py`
- **MessageHandler** (12 connections) — `server/realtime/message_handler_factory.py`
- **handle_command_message()** (11 connections) — `server/realtime/message_handlers.py`
- **test_message_handlers.py** (11 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_ping_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_follow_response_message()** (9 connections) — `server/realtime/message_handlers.py`
- **.__init__()** (8 connections) — `server/realtime/message_handler_factory.py`
- **handle_party_invite_response_message()** (8 connections) — `server/realtime/message_handlers.py`
- **Any** (8 connections) — `server/realtime/message_handler_factory.py`
- **WebSocket** (8 connections) — `server/realtime/message_handler_factory.py`
- **ChatMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **ClientErrorReportMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **CommandMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **.handle_message()** (7 connections) — `server/realtime/message_handler_factory.py`
- **PingMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (6 connections) — `server/realtime/message_handler_factory.py`
- **handle_client_error_report_message()** (6 connections) — `server/realtime/message_handlers.py`
- **cleanup_websocket_connection()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- *... and 99 more nodes in this community*

## Relationships

- [[Combat Player Broadcasts]] (9 shared connections)
- [[Application DI Bundles]] (8 shared connections)
- [[NPC Admin API]] (6 shared connections)
- [[Room Occupant Events]] (6 shared connections)
- [[WebSocket Message Validation]] (5 shared connections)
- [[Pydantic Error Handlers]] (3 shared connections)
- [[Game Mechanics Service]] (3 shared connections)
- [[WebSocket Message Validator]] (3 shared connections)
- [[Standardized Error Responses]] (2 shared connections)
- [[Player Combat XP]] (2 shared connections)
- [[Game Service Bundle]] (1 shared connections)
- [[WebSocket Command Handler]] (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/realtime/message_handler_factory.py`
- `server/realtime/message_handlers.py`
- `server/realtime/websocket_handler_connection.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handlers.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`

## Audit Trail

- EXTRACTED: 468 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
