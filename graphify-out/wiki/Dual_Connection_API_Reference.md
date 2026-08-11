# Dual Connection API Reference

> 54 nodes

## Key Concepts

- **NATSEventBusBridge** (16 connections) — `server/events/nats_event_bridge.py`
- **event_serialization.py** (15 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **serialize_event()** (14 connections) — `server/events/event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **Any** (6 connections)
- **_register_event_types()** (6 connections) — `server/events/event_serialization.py`
- **_register_module_events()** (5 connections) — `server/events/event_serialization.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **.set_nats_service()** (4 connections) — `server/events/distributed_event_bus.py`
- **_extract_event_fields()** (4 connections) — `server/events/event_serialization.py`
- **_convert_value_for_json()** (4 connections) — `server/events/event_serialization.py`
- **_convert_value_from_json()** (4 connections) — `server/events/event_serialization.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **._subject_for_event()** (4 connections) — `server/events/nats_event_bridge.py`
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **.__init__()** (3 connections) — `server/events/distributed_event_bus.py`
- **_register_event_class()** (3 connections) — `server/events/event_serialization.py`
- **Any** (3 connections)
- **test_deserialize_unknown_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_deserialize_missing_event_type_raises()** (3 connections) — `server/tests/unit/events/test_event_serialization.py`
- *... and 29 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (21 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (6 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_serialization.py`
- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 192 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*