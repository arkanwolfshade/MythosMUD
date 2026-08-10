# Database Error Handling

> 109 nodes

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
- **_resolve_npc_combat_service_raw()** (5 connections) — `server/npc/combat_integration_base.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- *... and 84 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (5 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (2 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (2 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (1 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [Infrastructure Message Broker](Infrastructure_Message_Broker.md) (1 shared connections)
- [Services Combat Persistence](Services_Combat_Persistence.md) (1 shared connections)
- [Logout and Quit Commands](Logout_and_Quit_Commands.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/realtime/message_handler_factory.py`
- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 398 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*