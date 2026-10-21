# combat_assist.py

> 99 nodes · cohesion 0.03

## Key Concepts

- **DistributedEventBus** (21 connections) — `server/events/distributed_event_bus.py`
- **event_serialization.py** (19 connections) — `server/events/event_serialization.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **test_distributed_event_bus.py** (15 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (14 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (14 connections) — `server/tests/unit/events/test_event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **distributed_event_bus.py** (11 connections) — `server/events/distributed_event_bus.py`
- **test_nats_event_bridge.py** (9 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **asyncio** (6 connections)
- **_convert_value_from_json()** (5 connections) — `server/events/event_serialization.py`
- **_register_event_types()** (5 connections) — `server/events/event_serialization.py`
- **_register_module_events()** (5 connections) — `server/events/event_serialization.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **SampleEvent** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_publish_with_nats_bridge_publishes_to_nats()** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_publish_without_nats_delegates_to_parent()** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_handle_nats_message_injects_remote_origin()** (5 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **test_publish_adds_origin_and_calls_nats()** (5 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **.set_nats_service()** (4 connections) — `server/events/distributed_event_bus.py`
- *... and 74 more nodes in this community*

## Relationships

- [get_username_from_user](get_username_from_user.md) (20 shared connections)
- [BaseEvent](BaseEvent.md) (8 shared connections)
- [Room](Room.md) (4 shared connections)
- [CombatInstance](CombatInstance.md) (4 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (3 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [TestRoomDataFixer](TestRoomDataFixer.md) (1 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_serialization.py`
- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_distributed_event_bus.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 182 (88%)
- INFERRED: 25 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*