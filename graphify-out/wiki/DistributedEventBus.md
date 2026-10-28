# DistributedEventBus

> 55 nodes · cohesion 0.06

## Key Concepts

- **test_nats_messages.py** (23 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **ChatMessageSchema** (13 connections) — `server/schemas/realtime/nats_messages.py`
- **validate_message()** (13 connections) — `server/schemas/realtime/nats_messages.py`
- **BaseMessageSchema** (11 connections) — `server/schemas/realtime/nats_messages.py`
- **EventMessageSchema** (11 connections) — `server/schemas/realtime/nats_messages.py`
- **nats_messages.py** (9 connections) — `server/schemas/realtime/nats_messages.py`
- **validate_chat_message()** (7 connections) — `server/schemas/realtime/nats_messages.py`
- **validate_event_message()** (7 connections) — `server/schemas/realtime/nats_messages.py`
- **.validate_timestamp()** (4 connections) — `server/schemas/realtime/nats_messages.py`
- **.validate_channel()** (4 connections) — `server/schemas/realtime/nats_messages.py`
- **.validate_event_type()** (4 connections) — `server/schemas/realtime/nats_messages.py`
- **test_validate_chat_message()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_event_message()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_message_chat()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_message_event()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **Any** (3 connections)
- **field_validator** (3 connections)
- **test_base_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_base_message_schema_invalid_timestamp()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_base_message_schema_validate_timestamp()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_accepts_speaker_kind_and_party_id()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_content_validation()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_invalid_channel()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_validate_channel()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- *... and 30 more nodes in this community*

## Relationships

- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (4 shared connections)
- [NATSService](NATSService.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)

## Source Files

- `server/schemas/realtime/nats_messages.py`
- `server/tests/unit/schemas/test_nats_messages.py`

## Audit Trail

- EXTRACTED: 90 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*