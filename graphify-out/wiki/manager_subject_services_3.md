# manager subject services

> 50 nodes

## Key Concepts

- **test_message_handlers.py** (24 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **message_handlers.py** (14 connections) — `server/realtime/message_handlers.py`
- **handle_follow_response_message()** (14 connections) — `server/realtime/message_handlers.py`
- **handle_party_invite_response_message()** (13 connections) — `server/realtime/message_handlers.py`
- **handle_command_message()** (11 connections) — `server/realtime/message_handlers.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_ping_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_client_error_report_message()** (8 connections) — `server/realtime/message_handlers.py`
- **WebSocket** (6 connections)
- **Any** (6 connections)
- **test_handle_command_message()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_command_message_no_command()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_command_message_no_args()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_chat_message()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_chat_message_no_message()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_ping_message()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_ping_message_with_data()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_client_error_report_message()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_invalid_request_id()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_no_container()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_invalid()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_accept()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_decline()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_accept_success()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_decline()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- *... and 25 more nodes in this community*

## Relationships

- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (12 shared connections)
- [room look commands](room_look_commands.md) (4 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (2 shared connections)
- [command commands handler](command_commands_handler.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 187 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*