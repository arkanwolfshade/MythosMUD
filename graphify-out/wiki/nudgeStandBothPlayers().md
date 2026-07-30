# nudgeStandBothPlayers()

> 30 nodes

## Key Concepts

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
- **Handle client_error_report: log client-reported errors to errors.log (via ERROR-** (1 connections) — `server/realtime/message_handlers.py`
- **Handle command message type.** (1 connections) — `server/realtime/message_handlers.py`
- **Handle chat message type.** (1 connections) — `server/realtime/message_handlers.py`
- **Handle ping message type.** (1 connections) — `server/realtime/message_handlers.py`
- **Handle follow_response message (accept/decline follow request).** (1 connections) — `server/realtime/message_handlers.py`
- **Handle party_invite_response message (accept/decline party invite).** (1 connections) — `server/realtime/message_handlers.py`
- **Unit tests for message handlers.  Tests the message_handlers module functions.** (1 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **Test handle_command_message() delegates to handle_game_command.** (1 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **Test handle_command_message() handles missing command.** (1 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- *... and 5 more nodes in this community*

## Relationships

- [world](world.md) (7 shared connections)
- [convert pydantic error()](convert_pydantic_error%28%29.md) (6 shared connections)
- [processing](processing.md) (6 shared connections)
- [circuit breaker](circuit_breaker.md) (3 shared connections)
- [test command parser](test_command_parser.md) (2 shared connections)
- [.is required()](is_required%28%29.md) (1 shared connections)
- [.model dump()](model_dump%28%29.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 112 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*