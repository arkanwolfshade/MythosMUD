# EventBus

> 467 nodes

## Key Concepts

- **EventBus** (127 connections) — `server/events/event_bus.py`
- **NPCDefinition** (108 connections) — `server/models/npc.py`
- **NPCBase** (81 connections) — `server/npc/npc_base.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **npc_base.py** (41 connections) — `server/npc/npc_base.py`
- **models/npc.py** (37 connections) — `server/models/npc.py`
- **spawning_service.py** (37 connections) — `server/npc/spawning_service.py`
- **AggressiveMobNPC** (32 connections) — `server/npc/aggressive_mob_npc.py`
- **PassiveMobNPC** (29 connections) — `server/npc/passive_mob_npc.py`
- **event_bus.py** (29 connections) — `server/events/event_bus.py`
- **event_reaction_system.py** (27 connections) — `server/npc/event_reaction_system.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **spawning_instance_factory.py** (24 connections) — `server/npc/spawning_instance_factory.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **NPCEventReactionSystem** (21 connections) — `server/npc/event_reaction_system.py`
- **spawning_request_execution.py** (19 connections) — `server/npc/spawning_request_execution.py`
- **aggressive_mob_npc.py** (18 connections) — `server/npc/aggressive_mob_npc.py`
- **passive_mob_npc.py** (18 connections) — `server/npc/passive_mob_npc.py`
- **ShopkeeperNPC** (17 connections) — `server/npc/shopkeeper_npc.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **NPCSpawnStatistics** (16 connections) — `server/npc/spawning_service.py`
- **SimpleNPCDefinition** (15 connections) — `server/npc/spawning_models.py`
- **NPCSpawnResult** (14 connections) — `server/npc/spawning_models.py`
- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- *... and 442 more nodes in this community*

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (130 shared connections)
- [get_logger](get_logger.md) (39 shared connections)
- [BaseEvent](BaseEvent.md) (31 shared connections)
- [test_npc_models.py](test_npc_models.py.md) (24 shared connections)
- [threading.py](threading.py.md) (19 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (14 shared connections)
- [test_population_control.py](test_population_control.py.md) (14 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (14 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (13 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (12 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (12 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (10 shared connections)

## Source Files

- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/models/npc.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behavior_engine.py`
- `server/npc/behaviors.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/npc_combat_schedule.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/npc_protocols.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_instance_factory.py`

## Audit Trail

- EXTRACTED: 1200 (95%)
- INFERRED: 64 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*