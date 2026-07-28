# Rate Limiter Service

> 46 nodes · cohesion 0.07

## Key Concepts

- **NATSEventBusBridge** (16 connections) — `server/events/nats_event_bridge.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **event_serialization.py** (12 connections) — `server/events/event_serialization.py`
- **_register_event_types()** (6 connections) — `server/events/event_serialization.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **_convert_value_for_json()** (4 connections) — `server/events/event_serialization.py`
- **_convert_value_from_json()** (4 connections) — `server/events/event_serialization.py`
- **Any** (4 connections)
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **._subject_for_event()** (4 connections) — `server/events/nats_event_bridge.py`
- **Any** (3 connections)
- **test_deserialize_missing_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_deserialize_unknown_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_non_base_event_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_handle_nats_message_skips_own_origin()** (3 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **.start()** (2 connections) — `server/events/nats_event_bridge.py`
- **.stop()** (2 connections) — `server/events/nats_event_bridge.py`
- **Event serialization for distributed EventBus over NATS.  Serializes and deserial** (1 connections) — `server/events/event_serialization.py`
- *... and 21 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (26 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (2 shared connections)

## Source Files

- `server/events/event_serialization.py`
- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 162 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*