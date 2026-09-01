# EventBus

> 477 nodes

## Key Concepts

- **EventBus** (212 connections) — `server/events/event_bus.py`
- **BaseEvent** (99 connections) — `server/events/event_types.py`
- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **NPCSpawningService** (66 connections) — `server/npc/spawning_service.py`
- **NPCPopulationController** (60 connections) — `server/npc/population_control.py`
- **test_event_bus.py** (60 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_npc_instance_service.py** (54 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCEnteredRoom** (49 connections) — `server/events/event_types.py`
- **npc_base.py** (45 connections) — `server/npc/npc_base.py`
- **threading.py** (45 connections) — `server/npc/threading.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **movement_service.py** (36 connections) — `server/game/movement_service.py`
- **models/room.py** (36 connections) — `server/models/room.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **event_reaction_system.py** (30 connections) — `server/npc/event_reaction_system.py`
- **asyncio** (28 connections)
- **server/events/__init__.py** (26 connections) — `server/events/__init__.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **NPCEventReactionSystem** (24 connections) — `server/npc/event_reaction_system.py`
- **NPCInstanceService** (23 connections) — `server/services/npc_instance_service.py`
- **asyncio** (23 connections)
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **movement_integration.py** (20 connections) — `server/npc/movement_integration.py`
- *... and 452 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (123 shared connections)
- [get_logger](get_logger.md) (50 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (45 shared connections)
- [NPCDefinition](NPCDefinition.md) (30 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (21 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (18 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (17 shared connections)
- [PlayerXPAwardEvent](PlayerXPAwardEvent.md) (17 shared connections)
- [npc_config_parsing.py](npc_config_parsing.py.md) (16 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (15 shared connections)
- [FollowService](FollowService.md) (14 shared connections)
- [._bind_event_type](_bind_event_type.md) (13 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/events/__init__.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/game/instance_manager.py`
- `server/game/movement_service.py`
- `server/models/room.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behavior_engine.py`
- `server/npc/behaviors.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/population_control.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/spawning_instance_factory.py`

## Audit Trail

- EXTRACTED: 1424 (87%)
- INFERRED: 208 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*