# Server Events

> 435 nodes

## Key Concepts

- **EventBus** (123 connections) — `server/events/event_bus.py`
- **event_types.py** (78 connections) — `server/events/event_types.py`
- **BaseEvent** (73 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (71 connections) — `server/events/event_types.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **PlayerLeftRoom** (53 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (51 connections) — `server/events/event_types.py`
- **NPCLeftRoom** (46 connections) — `server/events/event_types.py`
- **npc_base.py** (44 connections) — `server/npc/npc_base.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **test_follow_service.py** (38 connections) — `server/tests/unit/game/test_follow_service.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **event_bus.py** (29 connections) — `server/events/event_bus.py`
- **room.py** (28 connections) — `server/models/room.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **NPCDied** (25 connections) — `server/events/event_types.py`
- **event_reaction_system.py** (25 connections) — `server/npc/event_reaction_system.py`
- **NPCEventReactionSystem** (25 connections) — `server/npc/event_reaction_system.py`
- **follow_service.py** (24 connections) — `server/game/follow_service.py`
- **lifecycle_death.py** (23 connections) — `server/npc/lifecycle_death.py`
- **__init__.py** (22 connections) — `server/npc/__init__.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- *... and 410 more nodes in this community*

## Relationships

- [Server Npc](Server_Npc.md) (83 shared connections)
- [Server Commands](Server_Commands.md) (61 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (60 shared connections)
- [Server Npc (3)](Server_Npc_%283%29.md) (31 shared connections)
- [Server Npc (4)](Server_Npc_%284%29.md) (30 shared connections)
- [Server Realtime (6)](Server_Realtime_%286%29.md) (24 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (21 shared connections)
- [Server Events (3)](Server_Events_%283%29.md) (19 shared connections)
- [Server Realtime (19)](Server_Realtime_%2819%29.md) (18 shared connections)
- [Server Events (4)](Server_Events_%284%29.md) (18 shared connections)
- [Server Game (20)](Server_Game_%2820%29.md) (17 shared connections)
- [Server Services (6)](Server_Services_%286%29.md) (16 shared connections)

## Source Files

- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/game/follow_service.py`
- `server/models/room.py`
- `server/npc/__init__.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/population_control.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/spawning_service.py`
- `server/npc/zone_config_loader.py`
- `server/realtime/event_handler.py`

## Audit Trail

- EXTRACTED: 2100 (89%)
- INFERRED: 271 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*