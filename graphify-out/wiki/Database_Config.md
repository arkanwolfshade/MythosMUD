# Database Config

> 34 nodes

## Key Concepts

- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
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
- **Event serialization for distributed EventBus over NATS.  Serializes and deserial** (1 connections) — `server/events/event_serialization.py`
- **Populate the event class registry. Lazy import to avoid circular deps.** (1 connections) — `server/events/event_serialization.py`
- **Convert a value to JSON-serializable form.** (1 connections) — `server/events/event_serialization.py`
- **Convert a JSON value back to the expected Python type.** (1 connections) — `server/events/event_serialization.py`
- **Serialize a BaseEvent to a JSON-compatible dict.      Args:         event: Domai** (1 connections) — `server/events/event_serialization.py`
- **Deserialize a dict back to a BaseEvent instance.      Args:         data: Dict f** (1 connections) — `server/events/event_serialization.py`
- **Initialize the NATS EventBus bridge.          Args:             event_bus: Local** (1 connections) — `server/events/nats_event_bridge.py`
- *... and 9 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (14 shared connections)
- [profession models rationale](profession_models_rationale.md) (6 shared connections)
- [party service game](party_service_game.md) (2 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [combat validator validators](combat_validator_validators.md) (1 shared connections)

## Source Files

- `server/events/event_serialization.py`
- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_event_serialization.py`

## Audit Trail

- EXTRACTED: 126 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*