# Server Realtime (59)

> 31 nodes

## Key Concepts

- **message_handlers.py** (14 connections) — `server/realtime/message_handlers.py`
- **test_message_handlers.py** (12 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **handle_command_message()** (11 connections) — `server/realtime/message_handlers.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_ping_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_follow_response_message()** (9 connections) — `server/realtime/message_handlers.py`
- **handle_party_invite_response_message()** (8 connections) — `server/realtime/message_handlers.py`
- **handle_client_error_report_message()** (6 connections) — `server/realtime/message_handlers.py`
- **WebSocket** (6 connections)
- **Any** (6 connections)
- **test_handle_command_message()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_command_message_no_command()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_command_message_no_args()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_chat_message()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_chat_message_no_message()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_ping_message()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_ping_message_with_data()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **Test handle_command_message() handles missing command.** (2 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **Message handler implementations for WebSocket message routing.  This module cont** (1 connections) — `server/realtime/message_handlers.py`
- **Handle client_error_report: log client-reported errors to errors.log (via ERROR-** (1 connections) — `server/realtime/message_handlers.py`
- **Handle command message type.** (1 connections) — `server/realtime/message_handlers.py`
- **Handle chat message type.** (1 connections) — `server/realtime/message_handlers.py`
- **Handle ping message type.** (1 connections) — `server/realtime/message_handlers.py`
- **Handle follow_response message (accept/decline follow request).** (1 connections) — `server/realtime/message_handlers.py`
- **Handle party_invite_response message (accept/decline party invite).** (1 connections) — `server/realtime/message_handlers.py`
- *... and 6 more nodes in this community*

## Relationships

- [Server Realtime (71)](Server_Realtime_%2871%29.md) (6 shared connections)
- [Server Realtime (76)](Server_Realtime_%2876%29.md) (6 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (4 shared connections)
- [Server App](Server_App.md) (3 shared connections)
- [Server Realtime (48)](Server_Realtime_%2848%29.md) (2 shared connections)
- [Server Realtime (36)](Server_Realtime_%2836%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Realtime (17)](Server_Realtime_%2817%29.md) (1 shared connections)

## Source Files

- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 127 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*