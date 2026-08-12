# .validate_timestamp

> 7 nodes

## Key Concepts

- **.validate_timestamp()** (3 connections) — `server/schemas/realtime/nats_messages.py`
- **.validate_channel()** (3 connections) — `server/schemas/realtime/nats_messages.py`
- **.validate_event_type()** (3 connections) — `server/schemas/realtime/nats_messages.py`
- **field_validator** (3 connections)
- **Validate timestamp is valid ISO format.** (1 connections) — `server/schemas/realtime/nats_messages.py`
- **Validate channel is a known chat channel.** (1 connections) — `server/schemas/realtime/nats_messages.py`
- **Validate event type is not empty.** (1 connections) — `server/schemas/realtime/nats_messages.py`

## Relationships

- [test_nats_messages.py](test_nats_messages.py.md) (3 shared connections)

## Source Files

- `server/schemas/realtime/nats_messages.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*