# test_nats_messages.py

> 55 nodes

## Key Concepts

- **test_nats_messages.py** (25 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **validate_message()** (14 connections) — `server/schemas/realtime/nats_messages.py`
- **ChatMessageSchema** (13 connections) — `server/schemas/realtime/nats_messages.py`
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
- **test_event_message_schema_empty_event_type()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- *... and 30 more nodes in this community*

## Relationships

- [NATSMessageBroker](NATSMessageBroker.md) (2 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [test_real_time_helpers.py](test_real_time_helpers.py.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/schemas/realtime/nats_messages.py`
- `server/tests/unit/schemas/test_nats_messages.py`

## Audit Trail

- EXTRACTED: 84 (85%)
- INFERRED: 15 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*