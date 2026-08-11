# Database Error Handling

> 45 nodes

## Key Concepts

- **MessageHandler** (14 connections) — `server/realtime/message_handler_factory.py`
- **WebSocket** (8 connections)
- **Any** (8 connections)
- **.__init__()** (8 connections) — `server/realtime/message_handler_factory.py`
- **ChatMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **PingMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **ClientErrorReportMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **.handle_message()** (7 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (6 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **FollowResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **PartyInviteResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.get_handler()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (4 connections) — `server/realtime/message_handler_factory.py`
- **.subscribe()** (3 connections) — `server/infrastructure/message_broker.py`
- **.register_handler()** (3 connections) — `server/realtime/message_handler_factory.py`
- **test_chat_message_handler_handle()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_ping_message_handler_handle()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_client_error_report_handler_logs()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **ABC** (2 connections)
- **Subscribe to a subject/topic with a message handler.          Args:** (1 connections) — `server/infrastructure/message_broker.py`
- *... and 20 more nodes in this community*

## Relationships

- [Subzone Schema Definition](Subzone_Schema_Definition.md) (13 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (8 shared connections)
- [WebSocket Request Context](WebSocket_Request_Context.md) (6 shared connections)
- [Infrastructure Message Broker](Infrastructure_Message_Broker.md) (1 shared connections)
- [Realtime Event Delegation](Realtime_Event_Delegation.md) (1 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 153 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*