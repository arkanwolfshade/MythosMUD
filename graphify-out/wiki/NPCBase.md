# NPCBase

> 180 nodes

## Key Concepts

- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **NPCSpawningService** (66 connections) — `server/npc/spawning_service.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **SimpleNPCDefinition** (16 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **spawning_models.py** (13 connections) — `server/npc/spawning_models.py`
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_build_aggressive()** (8 connections) — `server/npc/spawning_instance_factory.py`
- **_spawn_success()** (8 connections) — `server/npc/spawning_request_execution.py`
- **._evaluate_spawn_requirements()** (8 connections) — `server/npc/spawning_service.py`
- **.__init__()** (7 connections) — `server/npc/spawning_service.py`
- **_build_passive()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_build_shopkeeper()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_room_from_persistence()** (6 connections) — `server/npc/spawning_request_execution.py`
- **._create_npc_instance()** (6 connections) — `server/npc/spawning_service.py`
- **._maybe_add_required_npc_request()** (6 connections) — `server/npc/spawning_service.py`
- **._spawn_npc_from_request()** (6 connections) — `server/npc/spawning_service.py`
- *... and 155 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (54 shared connections)
- [EventBus](EventBus.md) (28 shared connections)
- [NPCDefinition](NPCDefinition.md) (17 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (9 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (8 shared connections)
- [npc_config_parsing.py](npc_config_parsing.py.md) (7 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (7 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (5 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (4 shared connections)
- [PopulationStats](PopulationStats.md) (4 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (3 shared connections)

## Source Files

- `server/npc/behaviors.py`
- `server/npc/npc_base.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 442 (89%)
- INFERRED: 57 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*