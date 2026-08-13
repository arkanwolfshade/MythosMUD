# event_types.py

> 274 nodes

## Key Concepts

- **event_types.py** (74 connections) — `server/events/event_types.py`
- **BaseEvent** (71 connections) — `server/events/event_types.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PlayerLeftRoom** (40 connections) — `server/events/event_types.py`
- **PlayerDPUpdated** (37 connections) — `server/events/event_types.py`
- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **PlayerXPAwardEvent** (32 connections) — `server/services/player_combat_service.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **combat_event_publisher.py** (22 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (18 connections) — `server/events/combat_events.py`
- **CombatEventHandler** (17 connections) — `server/services/combat_event_handler.py`
- **PlayerDiedEvent** (16 connections) — `server/events/event_types.py`
- **PlayerRespawnedEvent** (16 connections) — `server/events/event_types.py`
- **npc_event_handlers.py** (16 connections) — `server/realtime/npc_event_handlers.py`
- **room_sync_service.py** (16 connections) — `server/services/room_sync_service.py`
- **CombatStartedEvent** (15 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (15 connections) — `server/events/combat_events.py`
- **event_serialization.py** (15 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **asyncio** (15 connections)
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (14 connections) — `server/events/event_serialization.py`
- *... and 249 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (94 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (70 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (45 shared connections)
- [NATSService](NATSService.md) (21 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (19 shared connections)
- [.__post_init__](__post_init__.md) (14 shared connections)
- [test_player_event_handlers_state.py](test_player_event_handlers_state.py.md) (14 shared connections)
- [Any](Any.md) (10 shared connections)
- [test_player_event_handlers.py](test_player_event_handlers.py.md) (10 shared connections)
- [NATSEventBusBridge](NATSEventBusBridge.md) (9 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (8 shared connections)
- [test_player_event_handlers_room_left.py](test_player_event_handlers_room_left.py.md) (7 shared connections)

## Source Files

- `server/events/__init__.py`
- `server/events/combat_events.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/npc/communication_integration.py`
- `server/npc/npc_base.py`
- `server/npc/spawning_service.py`
- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`

## Audit Trail

- EXTRACTED: 843 (95%)
- INFERRED: 42 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*