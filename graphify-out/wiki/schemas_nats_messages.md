# schemas nats messages

> 56 nodes

## Key Concepts

- **test_nats_messages.py** (23 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **validate_message()** (14 connections) — `server/schemas/realtime/nats_messages.py`
- **ChatMessageSchema** (13 connections) — `server/schemas/realtime/nats_messages.py`
- **BaseMessageSchema** (11 connections) — `server/schemas/realtime/nats_messages.py`
- **EventMessageSchema** (11 connections) — `server/schemas/realtime/nats_messages.py`
- **__init__.py** (9 connections) — `server/schemas/realtime/__init__.py`
- **nats_messages.py** (9 connections) — `server/schemas/realtime/nats_messages.py`
- **validate_chat_message()** (7 connections) — `server/schemas/realtime/nats_messages.py`
- **validate_event_message()** (7 connections) — `server/schemas/realtime/nats_messages.py`
- **test_base_message_schema_invalid_timestamp()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_invalid_channel()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_content_validation()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_event_message_schema_empty_event_type()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_chat_message()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_event_message()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_message_chat()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_message_event()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **Any** (3 connections)
- **test_base_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_base_message_schema_validate_timestamp()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_validate_channel()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_accepts_speaker_kind_and_party_id()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_event_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_event_message_schema_validate_event_type()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- *... and 31 more nodes in this community*

## Relationships

- [auth users rationale](auth_users_rationale.md) (5 shared connections)
- [command inventory models](command_inventory_models.md) (4 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (2 shared connections)
- [profession game service](profession_game_service.md) (1 shared connections)
- [broker infrastructure nats](broker_infrastructure_nats.md) (1 shared connections)
- [infrastructure nats broker](infrastructure_nats_broker.md) (1 shared connections)

## Source Files

- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/nats_messages.py`
- `server/tests/unit/schemas/test_nats_messages.py`

## Audit Trail

- EXTRACTED: 182 (94%)
- INFERRED: 12 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*