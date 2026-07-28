# Services Service Room

> 105 nodes · cohesion 0.03

## Key Concepts

- **message_handler_factory.py** (23 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handler_factory.py** (21 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **MessageHandlerFactory** (18 connections) — `server/realtime/message_handler_factory.py`
- **MessageHandler** (14 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handlers.py** (12 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **handle_command_message()** (11 connections) — `server/realtime/message_handlers.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_ping_message()** (10 connections) — `server/realtime/message_handlers.py`
- **CommandMessageHandler** (9 connections) — `server/realtime/message_handler_factory.py`
- **handle_follow_response_message()** (9 connections) — `server/realtime/message_handlers.py`
- **.__init__()** (8 connections) — `server/realtime/message_handler_factory.py`
- **Any** (8 connections)
- **WebSocket** (8 connections)
- **handle_party_invite_response_message()** (8 connections) — `server/realtime/message_handlers.py`
- **ChatMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **ClientErrorReportMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **.handle_message()** (7 connections) — `server/realtime/message_handler_factory.py`
- **PingMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (6 connections) — `server/realtime/message_handler_factory.py`
- **handle_client_error_report_message()** (6 connections) — `server/realtime/message_handlers.py`
- **Any** (6 connections)
- **WebSocket** (6 connections)
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **FollowResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- *... and 80 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (9 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (3 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (3 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (2 shared connections)
- [Infrastructure Message Broker](Infrastructure_Message_Broker.md) (1 shared connections)
- [Archive Planning E 2 E](Archive_Planning_E_2_E.md) (1 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (1 shared connections)
- [Database Manager Tests](Database_Manager_Tests.md) (1 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (1 shared connections)
- [NPC Combat Handler Tests](NPC_Combat_Handler_Tests.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 379 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*