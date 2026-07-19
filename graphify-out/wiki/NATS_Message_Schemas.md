# NATS Message Schemas

> 51 nodes · cohesion 0.06

## Key Concepts

- **test_nats_messages.py** (21 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **validate_message()** (14 connections) — `server/schemas/realtime/nats_messages.py`
- **BaseMessageSchema** (11 connections) — `server/schemas/realtime/nats_messages.py`
- **ChatMessageSchema** (10 connections) — `server/schemas/realtime/nats_messages.py`
- **EventMessageSchema** (9 connections) — `server/schemas/realtime/nats_messages.py`
- **nats_messages.py** (8 connections) — `server/schemas/realtime/nats_messages.py`
- **validate_chat_message()** (7 connections) — `server/schemas/realtime/nats_messages.py`
- **validate_event_message()** (7 connections) — `server/schemas/realtime/nats_messages.py`
- **test_base_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_base_message_schema_invalid_timestamp()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_base_message_schema_validate_timestamp()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_content_validation()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_invalid_channel()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_validate_channel()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_event_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_event_message_schema_empty_event_type()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_event_message_schema_validate_event_type()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_chat_message()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_event_message()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_message_chat()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_message_event()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **Any** (3 connections) — `server/schemas/realtime/nats_messages.py`
- **.validate_timestamp()** (2 connections) — `server/schemas/realtime/nats_messages.py`
- **.validate_channel()** (2 connections) — `server/schemas/realtime/nats_messages.py`
- *... and 26 more nodes in this community*

## Relationships

- [[Realtime Schemas Presence]] (2 shared connections)
- [[Message Broker Errors]] (2 shared connections)
- [[Admin NPC Schemas]] (1 shared connections)
- [[WebSocket Message Schemas]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[NATS Chat Broadcasting]] (1 shared connections)

## Source Files

- `server/schemas/realtime/nats_messages.py`
- `server/tests/unit/schemas/test_nats_messages.py`

## Audit Trail

- EXTRACTED: 164 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
