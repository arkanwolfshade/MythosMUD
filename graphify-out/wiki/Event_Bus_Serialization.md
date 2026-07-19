# Event Bus Serialization

> 52 nodes · cohesion 0.06

## Key Concepts

- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (12 connections) — `server/tests/unit/events/test_event_serialization.py`
- **event_serialization.py** (11 connections) — `server/events/event_serialization.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_nats_event_bridge.py** (5 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **Any** (5 connections) — `server/events/event_serialization.py`
- **_convert_value_for_json()** (4 connections) — `server/events/event_serialization.py`
- **_convert_value_from_json()** (4 connections) — `server/events/event_serialization.py`
- **_register_event_types()** (4 connections) — `server/events/event_serialization.py`
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **._subject_for_event()** (4 connections) — `server/events/nats_event_bridge.py`
- **Any** (4 connections) — `server/events/nats_event_bridge.py`
- **test_deserialize_missing_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_deserialize_unknown_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_non_base_event_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_handle_nats_message_injects_remote_origin()** (3 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **test_handle_nats_message_skips_own_origin()** (3 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **BaseEvent** (3 connections) — `server/events/event_serialization.py`
- *... and 27 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (20 shared connections)
- [[Player Combat XP]] (3 shared connections)
- [[Player Death Service]] (2 shared connections)
- [[Combat Service Bundle]] (1 shared connections)

## Source Files

- `server/events/event_serialization.py`
- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 173 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
