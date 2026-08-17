# event_serialization.py

> 42 nodes

## Key Concepts

- **event_serialization.py** (20 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (16 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **_convert_value_from_json()** (5 connections) — `server/events/event_serialization.py`
- **_register_event_types()** (5 connections) — `server/events/event_serialization.py`
- **_register_module_events()** (5 connections) — `server/events/event_serialization.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **_extract_event_fields()** (4 connections) — `server/events/event_serialization.py`
- **_init_kwargs_from_event_data()** (4 connections) — `server/events/event_serialization.py`
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **_convert_value_for_json()** (3 connections) — `server/events/event_serialization.py`
- **_copy_public_event_attrs()** (3 connections) — `server/events/event_serialization.py`
- **_event_class_from_payload()** (3 connections) — `server/events/event_serialization.py`
- **_register_event_class()** (3 connections) — `server/events/event_serialization.py`
- **test_deserialize_missing_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_deserialize_unknown_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_non_base_event_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **Any** (3 connections)
- **_parse_typed_json_value()** (2 connections) — `server/events/event_serialization.py`
- **_unwrap_optional_type()** (2 connections) — `server/events/event_serialization.py`
- *... and 17 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (25 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/events/event_serialization.py`
- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_event_serialization.py`

## Audit Trail

- EXTRACTED: 83 (88%)
- INFERRED: 11 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*