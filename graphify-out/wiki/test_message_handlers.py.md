# test_message_handlers.py

> 43 nodes

## Key Concepts

- **test_message_handlers.py** (26 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **asyncio** (16 connections)
- **handle_follow_response_message()** (14 connections) — `server/realtime/message_handlers.py`
- **handle_party_invite_response_message()** (13 connections) — `server/realtime/message_handlers.py`
- **handle_command_message()** (11 connections) — `server/realtime/message_handlers.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_client_error_report_message()** (8 connections) — `server/realtime/message_handlers.py`
- **Any** (6 connections)
- **WebSocket** (6 connections)
- **test_handle_chat_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_chat_message_no_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_client_error_report_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_command_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_command_message_no_args()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_command_message_no_command()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_accept_success()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_decline()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_invalid_request_id()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_no_container()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_accept()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_decline()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_invalid()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_no_container()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **Handle party_invite_response message (accept/decline party invite).** (1 connections) — `server/realtime/message_handlers.py`
- **Handle client_error_report: log client-reported errors to errors.log (via…** (1 connections) — `server/realtime/message_handlers.py`
- *... and 18 more nodes in this community*

## Relationships

- [handle_ping_message](handle_ping_message.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [Any](Any.md) (5 shared connections)
- [message_handler_factory.py](message_handler_factory.py.md) (5 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [bundles/game.py](bundles-game.py.md) (2 shared connections)
- [test_websocket_handler_coverage_gaps.py](test_websocket_handler_coverage_gaps.py.md) (1 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [User](User.md) (1 shared connections)

## Source Files

- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 108 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*