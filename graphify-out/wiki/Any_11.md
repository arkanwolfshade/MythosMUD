# Any

> 357 nodes

## Key Concepts

- **event_types.py** (78 connections) — `server/events/event_types.py`
- **BaseEvent** (73 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (71 connections) — `server/events/event_types.py`
- **PlayerLeftRoom** (53 connections) — `server/events/event_types.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **RealTimeEventHandler** (36 connections) — `server/realtime/event_handler.py`
- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **event_handler.py** (34 connections) — `server/realtime/event_handler.py`
- **test_player_event_handlers.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **event_bus.py** (29 connections) — `server/events/event_bus.py`
- **event_reaction_system.py** (29 connections) — `server/npc/event_reaction_system.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **MessageBuilder** (22 connections) — `server/realtime/message_builders.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **PlayerDiedEvent** (19 connections) — `server/events/event_types.py`
- **PlayerRespawnedEvent** (19 connections) — `server/events/event_types.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **PlayerDPDecayEvent** (16 connections) — `server/events/event_types.py`
- **NATSEventBusBridge** (16 connections) — `server/events/nats_event_bridge.py`
- **npc_event_handlers.py** (16 connections) — `server/realtime/npc_event_handlers.py`
- **NPCSpoke** (15 connections) — `server/events/event_types.py`
- **PlayerDeliriumRespawnedEvent** (15 connections) — `server/events/event_types.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- *... and 332 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (76 shared connections)
- [main()](main%28%29.md) (45 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (29 shared connections)
- [. init ()](_init_%28%29.md) (27 shared connections)
- [. repr ()](_repr_%28%29.md) (25 shared connections)
- [UUID](UUID.md) (24 shared connections)
- [. post init ()](_post_init_%28%29.md) (17 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (17 shared connections)
- [.set player combat service()](set_player_combat_service%28%29.md) (16 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (16 shared connections)
- [Any](Any.md) (15 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (13 shared connections)

## Source Files

- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/models/room.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_default_reactions.py`
- `server/realtime/event_handler.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/room_occupant_manager.py`
- `server/services/combat_hp_sync.py`
- `server/services/player_combat_service.py`
- `server/services/room_sync_service.py`

## Audit Trail

- EXTRACTED: 1572 (90%)
- INFERRED: 169 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*