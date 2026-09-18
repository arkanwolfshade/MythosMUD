# Community 503

> 34 nodes

## Key Concepts

- **event_serialization.py** (19 connections) — `server/events/event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (14 connections) — `server/tests/unit/events/test_event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **_convert_value_from_json()** (5 connections) — `server/events/event_serialization.py`
- **_register_event_types()** (5 connections) — `server/events/event_serialization.py`
- **_register_module_events()** (5 connections) — `server/events/event_serialization.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **_extract_event_fields()** (4 connections) — `server/events/event_serialization.py`
- **_init_kwargs_from_event_data()** (4 connections) — `server/events/event_serialization.py`
- **_convert_value_for_json()** (3 connections) — `server/events/event_serialization.py`
- **_copy_public_event_attrs()** (3 connections) — `server/events/event_serialization.py`
- **_event_class_from_payload()** (3 connections) — `server/events/event_serialization.py`
- **_register_event_class()** (3 connections) — `server/events/event_serialization.py`
- **test_deserialize_missing_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_deserialize_unknown_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_non_base_event_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **_parse_typed_json_value()** (2 connections) — `server/events/event_serialization.py`
- **_unwrap_optional_type()** (2 connections) — `server/events/event_serialization.py`
- **Test deserialize with unknown event type raises ValueError.** (2 connections) — `server/tests/unit/events/test_event_serialization.py`
- **ModuleType** (1 connections)
- **Event serialization for distributed EventBus over NATS. Serializes and…** (1 connections) — `server/events/event_serialization.py`
- **Convert a JSON value back to the expected Python type.** (1 connections) — `server/events/event_serialization.py`
- *... and 9 more nodes in this community*

## Relationships

- [Event Bus](Event_Bus.md) (14 shared connections)
- [NPC Event Types](NPC_Event_Types.md) (4 shared connections)
- [Combat Events](Combat_Events.md) (3 shared connections)
- [Community 219](Community_219.md) (1 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (1 shared connections)

## Source Files

- `server/events/event_serialization.py`
- `server/tests/unit/events/test_event_serialization.py`

## Audit Trail

- EXTRACTED: 72 (90%)
- INFERRED: 8 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*