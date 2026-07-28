# Server Events (3)

> 35 nodes

## Key Concepts

- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **event_serialization.py** (12 connections) — `server/events/event_serialization.py`
- **_register_event_types()** (6 connections) — `server/events/event_serialization.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **_convert_value_for_json()** (4 connections) — `server/events/event_serialization.py`
- **Any** (4 connections)
- **_convert_value_from_json()** (4 connections) — `server/events/event_serialization.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **Any** (3 connections)
- **test_deserialize_unknown_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_deserialize_missing_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_non_base_event_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **Test deserialize with unknown event type raises ValueError.** (2 connections) — `server/tests/unit/events/test_event_serialization.py`
- **Event serialization for distributed EventBus over NATS.  Serializes and deserial** (1 connections) — `server/events/event_serialization.py`
- **Populate the event class registry. Lazy import to avoid circular deps.** (1 connections) — `server/events/event_serialization.py`
- **Convert a value to JSON-serializable form.** (1 connections) — `server/events/event_serialization.py`
- **Convert a JSON value back to the expected Python type.** (1 connections) — `server/events/event_serialization.py`
- **Serialize a BaseEvent to a JSON-compatible dict.      Args:         event: Domai** (1 connections) — `server/events/event_serialization.py`
- *... and 10 more nodes in this community*

## Relationships

- [Server Events](Server_Events.md) (19 shared connections)
- [Server Services (6)](Server_Services_%286%29.md) (5 shared connections)
- [Server Services (2)](Server_Services_%282%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Services (17)](Server_Services_%2817%29.md) (1 shared connections)

## Source Files

- `server/events/event_serialization.py`
- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_event_serialization.py`

## Audit Trail

- EXTRACTED: 140 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*