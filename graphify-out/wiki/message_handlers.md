# message handlers

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

- [UUID](UUID.md) (6 shared connections)
- [message handler factory](message_handler_factory.md) (6 shared connections)
- [.handle()](handle%28%29.md) (6 shared connections)
- [.shutdown()](shutdown%28%29.md) (3 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (2 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [websocket handler commands](websocket_handler_commands.md) (1 shared connections)

## Source Files

- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 127 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*