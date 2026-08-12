# BaseEvent

> 116 nodes

## Key Concepts

- **BaseEvent** (71 connections) — `server/events/event_types.py`
- **PlayerDiedEvent** (16 connections) — `server/events/event_types.py`
- **NATSEventBusBridge** (16 connections) — `server/events/nats_event_bridge.py`
- **event_serialization.py** (15 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (14 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **distributed_event_bus.py** (10 connections) — `server/events/distributed_event_bus.py`
- **Any** (10 connections)
- **._handle_event_async()** (8 connections) — `server/events/event_bus.py`
- **test_nats_event_bridge.py** (7 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **._create_async_subscriber_tasks()** (6 connections) — `server/events/event_bus.py`
- **._ensure_async_processing()** (6 connections) — `server/events/event_bus.py`
- **Any** (6 connections)
- **._process_sync_subscribers()** (5 connections) — `server/events/event_bus.py`
- **._separate_subscribers()** (5 connections) — `server/events/event_bus.py`
- **.unsubscribe()** (5 connections) — `server/events/event_bus.py`
- **._wait_for_async_subscribers()** (5 connections) — `server/events/event_bus.py`
- **_register_event_types()** (5 connections) — `server/events/event_serialization.py`
- **_register_module_events()** (5 connections) — `server/events/event_serialization.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- *... and 91 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (31 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (22 shared connections)
- [combat_service.py](combat_service.py.md) (10 shared connections)
- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [.__post_init__](__post_init__.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (3 shared connections)
- [player_combat_service.py](player_combat_service.py.md) (2 shared connections)
- [test_event_bus.py](test_event_bus.py.md) (2 shared connections)
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

- EXTRACTED: 268 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*