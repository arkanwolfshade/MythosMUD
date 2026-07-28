# Server Realtime (71)

> 23 nodes

## Key Concepts

- **message_handler_factory.py** (23 connections) — `server/realtime/message_handler_factory.py`
- **MessageHandler** (14 connections) — `server/realtime/message_handler_factory.py`
- **CommandMessageHandler** (9 connections) — `server/realtime/message_handler_factory.py`
- **.__init__()** (8 connections) — `server/realtime/message_handler_factory.py`
- **ChatMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **PingMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **ClientErrorReportMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **FollowResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **PartyInviteResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **.register_handler()** (3 connections) — `server/realtime/message_handler_factory.py`
- **test_client_error_report_handler_logs()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **ABC** (2 connections)
- **Message Handler Factory for WebSocket message routing.  This module implements a** (1 connections) — `server/realtime/message_handler_factory.py`
- **Abstract base class for message handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for command messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for chat messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for ping messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for follow_response messages (accept/decline follow request).** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for party_invite_response messages (accept/decline party invite).** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for client_error_report messages (client-reported errors for server logg** (1 connections) — `server/realtime/message_handler_factory.py`
- **Initialize the factory with registered handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Register a new message handler.          Args:             message_type: The mes** (1 connections) — `server/realtime/message_handler_factory.py`
- **Test ClientErrorReportMessageHandler logs via logger.error.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`

## Relationships

- [Server Realtime (57)](Server_Realtime_%2857%29.md) (14 shared connections)
- [Server Realtime (76)](Server_Realtime_%2876%29.md) (8 shared connections)
- [Server Realtime (59)](Server_Realtime_%2859%29.md) (6 shared connections)
- [Server Error Handlers (2)](Server_Error_Handlers_%282%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Error Handlers](Server_Error_Handlers.md) (1 shared connections)
- [Server Api (2)](Server_Api_%282%29.md) (1 shared connections)
- [Server Infrastructure (15)](Server_Infrastructure_%2815%29.md) (1 shared connections)
- [Server Infrastructure (3)](Server_Infrastructure_%283%29.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 102 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*