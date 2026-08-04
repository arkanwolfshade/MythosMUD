# manager subject services

> 40 nodes

## Key Concepts

- **test_message_handlers.py** (24 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **message_handlers.py** (14 connections) — `server/realtime/message_handlers.py`
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
- **test_handle_party_invite_response_invalid()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_accept()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_decline()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_no_container()** (3 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **Message handler implementations for WebSocket message routing.  This module cont** (1 connections) — `server/realtime/message_handlers.py`
- **Handle client_error_report: log client-reported errors to errors.log (via ERROR-** (1 connections) — `server/realtime/message_handlers.py`
- **Handle command message type.** (1 connections) — `server/realtime/message_handlers.py`
- **Handle chat message type.** (1 connections) — `server/realtime/message_handlers.py`
- *... and 15 more nodes in this community*

## Relationships

- [models profession rationale](models_profession_rationale.md) (8 shared connections)
- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (5 shared connections)
- [game chat moderation](game_chat_moderation.md) (5 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (1 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 156 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*