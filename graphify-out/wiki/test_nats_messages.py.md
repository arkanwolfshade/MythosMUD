# test_nats_messages.py

> 48 nodes

## Key Concepts

- **test_nats_messages.py** (22 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **validate_message()** (14 connections) — `server/schemas/realtime/nats_messages.py`
- **BaseMessageSchema** (11 connections) — `server/schemas/realtime/nats_messages.py`
- **ChatMessageSchema** (10 connections) — `server/schemas/realtime/nats_messages.py`
- **EventMessageSchema** (9 connections) — `server/schemas/realtime/nats_messages.py`
- **schemas/realtime/__init__.py** (9 connections) — `server/schemas/realtime/__init__.py`
- **nats_messages.py** (9 connections) — `server/schemas/realtime/nats_messages.py`
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
- **Any** (3 connections)
- **BaseModel** (1 connections)
- *... and 23 more nodes in this community*

## Relationships

- [realtime/realtime.py](realtime-realtime.py.md) (5 shared connections)
- [.validate_timestamp](validate_timestamp.md) (3 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (2 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)

## Source Files

- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/nats_messages.py`
- `server/tests/unit/schemas/test_nats_messages.py`

## Audit Trail

- EXTRACTED: 90 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*