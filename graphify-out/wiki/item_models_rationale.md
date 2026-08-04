# item models rationale

> 124 nodes

## Key Concepts

- **BaseEvent** (75 connections) — `server/events/event_types.py`
- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **DistributedEventBus** (22 connections) — `server/events/distributed_event_bus.py`
- **PlayerDiedEvent** (19 connections) — `server/events/event_types.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **test_distributed_event_bus.py** (14 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **event_serialization.py** (12 connections) — `server/events/event_serialization.py`
- **distributed_event_bus.py** (11 connections) — `server/events/distributed_event_bus.py`
- **test_nats_event_bridge.py** (9 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **_register_event_types()** (6 connections) — `server/events/event_serialization.py`
- **Any** (6 connections)
- **._handle_event()** (6 connections) — `server/npc/event_reaction_system.py`
- **SampleEvent** (6 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **.should_trigger()** (5 connections) — `server/npc/event_reaction_system.py`
- **.execute()** (5 connections) — `server/npc/event_reaction_system.py`
- **test_serialize_deserialize_player_entered_room()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_died_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **.set_nats_service()** (4 connections) — `server/events/distributed_event_bus.py`
- *... and 99 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (44 shared connections)
- [Error Conversion](Error_Conversion.md) (16 shared connections)
- [NPC Combat](NPC_Combat.md) (16 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (10 shared connections)
- [nats services service](nats_services_service.md) (6 shared connections)
- [message handler factory](message_handler_factory.md) (6 shared connections)
- [room look commands](room_look_commands.md) (5 shared connections)
- [command service commands](command_service_commands.md) (3 shared connections)
- [room service sync](room_service_sync.md) (3 shared connections)
- [combat validator validators](combat_validator_validators.md) (3 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (3 shared connections)
- [feature services flag](feature_services_flag.md) (3 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/npc/event_reaction_system.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/events/test_distributed_event_bus.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 467 (90%)
- INFERRED: 50 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*