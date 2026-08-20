# NPCSpawningService

> 116 nodes

## Key Concepts

- **NPCSpawningService** (66 connections) — `server/npc/spawning_service.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **SimpleNPCDefinition** (16 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **spawning_models.py** (13 connections) — `server/npc/spawning_models.py`
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_build_aggressive()** (8 connections) — `server/npc/spawning_instance_factory.py`
- **_spawn_success()** (8 connections) — `server/npc/spawning_request_execution.py`
- **._evaluate_spawn_requirements()** (8 connections) — `server/npc/spawning_service.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **.__init__()** (7 connections) — `server/npc/spawning_service.py`
- **_build_passive()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_build_shopkeeper()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_room_from_persistence()** (6 connections) — `server/npc/spawning_request_execution.py`
- **._calculate_spawn_priority()** (6 connections) — `server/npc/spawning_service.py`
- **._create_npc_instance()** (6 connections) — `server/npc/spawning_service.py`
- **._maybe_add_required_npc_request()** (6 connections) — `server/npc/spawning_service.py`
- *... and 91 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (32 shared connections)
- [NPCDefinition](NPCDefinition.md) (24 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (14 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [NPCEnteredRoom](NPCEnteredRoom.md) (10 shared connections)
- [NPCBase](NPCBase.md) (10 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (8 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (7 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (7 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (7 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (6 shared connections)
- [PopulationStats](PopulationStats.md) (5 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 357 (88%)
- INFERRED: 48 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*