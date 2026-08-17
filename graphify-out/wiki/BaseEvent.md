# BaseEvent

> 88 nodes

## Key Concepts

- **BaseEvent** (81 connections) — `server/events/event_types.py`
- **event_serialization.py** (20 connections) — `server/events/event_serialization.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **test_event_serialization.py** (16 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **distributed_event_bus.py** (12 connections) — `server/events/distributed_event_bus.py`
- **test_nats_event_bridge.py** (10 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **Any** (6 connections)
- **_convert_value_from_json()** (5 connections) — `server/events/event_serialization.py`
- **_register_event_types()** (5 connections) — `server/events/event_serialization.py`
- **_register_module_events()** (5 connections) — `server/events/event_serialization.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_handle_nats_message_injects_remote_origin()** (5 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **test_publish_adds_origin_and_calls_nats()** (5 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **_extract_event_fields()** (4 connections) — `server/events/event_serialization.py`
- **_init_kwargs_from_event_data()** (4 connections) — `server/events/event_serialization.py`
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **._subject_for_event()** (4 connections) — `server/events/nats_event_bridge.py`
- *... and 63 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (32 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (11 shared connections)
- [EventBus](EventBus.md) (9 shared connections)
- [CombatService](CombatService.md) (7 shared connections)
- [DistributedEventBus](DistributedEventBus.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_event_bus.py](test_event_bus.py.md) (5 shared connections)
- [.__post_init__](__post_init__.md) (3 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (3 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (2 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (2 shared connections)
- [NATSService](NATSService.md) (2 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/npc/event_reaction_system.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 205 (84%)
- INFERRED: 39 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*