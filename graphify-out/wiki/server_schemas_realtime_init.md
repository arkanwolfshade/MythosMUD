# server schemas realtime init

> 57 nodes

## Key Concepts

- **test_nats_messages.py** (25 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **validate_message()** (14 connections) — `server/schemas/realtime/nats_messages.py`
- **ChatMessageSchema** (13 connections) — `server/schemas/realtime/nats_messages.py`
- **schemas/realtime/__init__.py** (12 connections) — `server/schemas/realtime/__init__.py`
- **BaseMessageSchema** (11 connections) — `server/schemas/realtime/nats_messages.py`
- **EventMessageSchema** (11 connections) — `server/schemas/realtime/nats_messages.py`
- **nats_messages.py** (10 connections) — `server/schemas/realtime/nats_messages.py`
- **validate_chat_message()** (7 connections) — `server/schemas/realtime/nats_messages.py`
- **validate_event_message()** (7 connections) — `server/schemas/realtime/nats_messages.py`
- **test_validate_chat_message()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_event_message()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_message_chat()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_message_event()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **.validate_timestamp()** (3 connections) — `server/schemas/realtime/nats_messages.py`
- **.validate_channel()** (3 connections) — `server/schemas/realtime/nats_messages.py`
- **.validate_event_type()** (3 connections) — `server/schemas/realtime/nats_messages.py`
- **test_base_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_base_message_schema_invalid_timestamp()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_base_message_schema_validate_timestamp()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_accepts_speaker_kind_and_party_id()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_content_validation()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_invalid_channel()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_validate_channel()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_event_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- *... and 32 more nodes in this community*

## Relationships

- [server api real time](server_api_real_time.md) (6 shared connections)
- [server infrastructure message broker](server_infrastructure_message_broker.md) (3 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (2 shared connections)
- [server realtime dead letter queue](server_realtime_dead_letter_queue.md) (1 shared connections)
- [server api players get player](server_api_players_get_player.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/nats_messages.py`
- `server/tests/unit/schemas/test_nats_messages.py`

## Audit Trail

- EXTRACTED: 94 (86%)
- INFERRED: 15 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*