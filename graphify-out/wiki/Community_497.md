# Community 497

> 35 nodes

## Key Concepts

- **event_serialization.py** (18 connections) — `server/events/event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (11 connections) — `server/tests/unit/events/test_event_serialization.py`
- **BaseEvent** (7 connections)
- **_convert_value_from_json()** (5 connections) — `server/events/event_serialization.py`
- **_register_event_types()** (5 connections) — `server/events/event_serialization.py`
- **_register_module_events()** (5 connections) — `server/events/event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **_event_class_from_payload()** (4 connections) — `server/events/event_serialization.py`
- **_extract_event_fields()** (4 connections) — `server/events/event_serialization.py`
- **_init_kwargs_from_event_data()** (4 connections) — `server/events/event_serialization.py`
- **test_serialize_deserialize_player_died_event()** (4 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_entered_room()** (4 connections) — `server/tests/unit/events/test_event_serialization.py`
- **_convert_value_for_json()** (3 connections) — `server/events/event_serialization.py`
- **_copy_public_event_attrs()** (3 connections) — `server/events/event_serialization.py`
- **_register_event_class()** (3 connections) — `server/events/event_serialization.py`
- **test_deserialize_missing_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_deserialize_unknown_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_non_base_event_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **_parse_typed_json_value()** (2 connections) — `server/events/event_serialization.py`
- **_unwrap_optional_type()** (2 connections) — `server/events/event_serialization.py`
- **Test deserialize with unknown event type raises ValueError.** (2 connections) — `server/tests/unit/events/test_event_serialization.py`
- **ModuleType** (1 connections)
- **Event serialization for distributed EventBus over NATS. Serializes and…** (1 connections) — `server/events/event_serialization.py`
- *... and 10 more nodes in this community*

## Relationships

- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (5 shared connections)
- [Community 226](Community_226.md) (2 shared connections)
- [Game Event Types](Game_Event_Types.md) (2 shared connections)
- [Community 281](Community_281.md) (1 shared connections)
- [Community 65](Community_65.md) (1 shared connections)

## Source Files

- `server/events/event_serialization.py`
- `server/tests/unit/events/test_event_serialization.py`

## Audit Trail

- EXTRACTED: 72 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*