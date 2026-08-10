# Spell Effect Protocols

> 112 nodes

## Key Concepts

- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **spawning_service.py** (37 connections) — `server/npc/spawning_service.py`
- **spawning_instance_factory.py** (24 connections) — `server/npc/spawning_instance_factory.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **spawning_request_execution.py** (19 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnStatistics** (16 connections) — `server/npc/spawning_service.py`
- **SimpleNPCDefinition** (15 connections) — `server/npc/spawning_models.py`
- **NPCSpawnResult** (14 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (13 connections) — `server/npc/spawning_instance_factory.py`
- **spawning_models.py** (12 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (12 connections) — `server/npc/spawning_request_execution.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_build_aggressive()** (9 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnRequest** (9 connections) — `server/npc/spawning_models.py`
- **generate_npc_id()** (8 connections) — `server/npc/spawning_instance_factory.py`
- **population_stats.py** (7 connections) — `server/npc/population_stats.py`
- **_build_shopkeeper()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_build_passive()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **._spawn_npc_from_request()** (6 connections) — `server/npc/spawning_service.py`
- **._create_npc_instance()** (6 connections) — `server/npc/spawning_service.py`
- **_coerce_simple_definition()** (5 connections) — `server/npc/spawning_instance_factory.py`
- **_spawn_success()** (5 connections) — `server/npc/spawning_request_execution.py`
- **._generate_npc_id()** (5 connections) — `server/npc/spawning_service.py`
- **.get_spawn_statistics()** (5 connections) — `server/npc/spawning_service.py`
- **.get_population_stats()** (4 connections) — `server/npc/population_control.py`
- *... and 87 more nodes in this community*

## Relationships

- [Level and XP Curve](Level_and_XP_Curve.md) (44 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (24 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (23 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (11 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (7 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (7 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (1 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (1 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)

## Source Files

- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_population_stats.py`

## Audit Trail

- EXTRACTED: 443 (94%)
- INFERRED: 30 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*