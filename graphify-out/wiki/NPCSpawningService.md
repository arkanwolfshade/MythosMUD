# NPCSpawningService

> 104 nodes

## Key Concepts

- **NPCSpawningService** (69 connections) — `server/npc/spawning_service.py`
- **test_spawning_modules.py** (47 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_service.py** (40 connections) — `server/npc/spawning_service.py`
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **SimpleNPCDefinition** (19 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **spawning_models.py** (14 connections) — `server/npc/spawning_models.py`
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_spawn_success()** (8 connections) — `server/npc/spawning_request_execution.py`
- **._evaluate_spawn_requirements()** (8 connections) — `server/npc/spawning_service.py`
- **.__init__()** (8 connections) — `server/npc/spawning_service.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **_room_from_persistence()** (6 connections) — `server/npc/spawning_request_execution.py`
- **._calculate_spawn_priority()** (6 connections) — `server/npc/spawning_service.py`
- **._maybe_add_required_npc_request()** (6 connections) — `server/npc/spawning_service.py`
- **._spawn_npc_from_request()** (6 connections) — `server/npc/spawning_service.py`
- **._check_spawn_requirements_for_room()** (5 connections) — `server/npc/spawning_service.py`
- **._generate_npc_id()** (5 connections) — `server/npc/spawning_service.py`
- **.get_spawn_statistics()** (5 connections) — `server/npc/spawning_service.py`
- **test_spawning_service_threads_event_reaction_system_to_created_npcs()** (5 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **NPCSpawnRequest** (5 connections)
- **NPCSpawnStatistics** (4 connections) — `server/npc/spawning_service.py`
- **.__init__()** (4 connections) — `server/npc/spawning_models.py`
- *... and 79 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (39 shared connections)
- [NPCBase](NPCBase.md) (32 shared connections)
- [EventBus](EventBus.md) (24 shared connections)
- [NPCDefinition](NPCDefinition.md) (14 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (9 shared connections)
- [PopulationStats](PopulationStats.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (3 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (3 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)

## Source Files

- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 300 (90%)
- INFERRED: 35 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*