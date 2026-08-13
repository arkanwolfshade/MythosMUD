# event_types.py

> 361 nodes

## Key Concepts

- **event_types.py** (74 connections) — `server/events/event_types.py`
- **BaseEvent** (71 connections) — `server/events/event_types.py`
- **NATSError** (60 connections) — `server/services/nats_exceptions.py`
- **NPCLeftRoom** (40 connections) — `server/events/event_types.py`
- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **models/room.py** (31 connections) — `server/models/room.py`
- **NATSPublishError** (30 connections) — `server/services/nats_exceptions.py`
- **nats_exceptions.py** (30 connections) — `server/services/nats_exceptions.py`
- **event_reaction_system.py** (27 connections) — `server/npc/event_reaction_system.py`
- **NATSSubscribeError** (25 connections) — `server/services/nats_exceptions.py`
- **combat_integration.py** (25 connections) — `server/npc/combat_integration.py`
- **lifecycle_death.py** (23 connections) — `server/npc/lifecycle_death.py`
- **nats_service.py** (23 connections) — `server/services/nats_service.py`
- **NPCDied** (22 connections) — `server/events/event_types.py`
- **combat_event_publisher.py** (22 connections) — `server/services/combat_event_publisher.py`
- **combat_death_handler.py** (21 connections) — `server/services/combat_death_handler.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (18 connections) — `server/events/combat_events.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **CombatEventHandler** (17 connections) — `server/services/combat_event_handler.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **combat_event_handler.py** (17 connections) — `server/services/combat_event_handler.py`
- **NATSEventBusBridge** (16 connections) — `server/events/nats_event_bridge.py`
- **_LifecycleManagerForDeath** (16 connections) — `server/npc/lifecycle_death.py`
- **_SpawnTrackedNPC** (16 connections) — `server/npc/lifecycle_manager.py`
- *... and 336 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (102 shared connections)
- [CombatService](CombatService.md) (59 shared connections)
- [get_logger](get_logger.md) (49 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (32 shared connections)
- [CombatEventPublisher](CombatEventPublisher.md) (21 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (19 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (15 shared connections)
- [NATSService](NATSService.md) (15 shared connections)
- [.__post_init__](__post_init__.md) (13 shared connections)
- [build_event](build_event.md) (12 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (8 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (8 shared connections)

## Source Files

- `server/events/__init__.py`
- `server/events/combat_events.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/models/room.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/realtime/message_formatters.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`

## Audit Trail

- EXTRACTED: 1035 (90%)
- INFERRED: 118 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*