# Command Parser Tests

> 263 nodes

## Key Concepts

- **NPCDefinition** (126 connections) — `server/models/npc.py`
- **NPCSpawnRule** (57 connections) — `server/models/npc.py`
- **npc.py** (37 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **spawn_rule_crud.py** (11 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_JSONDict** (10 connections)
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **._evaluate_spawn_requirements()** (9 connections) — `server/npc/spawning_service.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **AsyncSession** (8 connections)
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_spawn_rule()** (8 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- *... and 238 more nodes in this community*

## Relationships

- [Level and XP Curve](Level_and_XP_Curve.md) (37 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (25 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (23 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (19 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (13 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (12 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (11 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (9 shared connections)
- [Test Refactoring Deliverables](Test_Refactoring_Deliverables.md) (9 shared connections)
- [App Lifespan Management](App_Lifespan_Management.md) (6 shared connections)
- [NPC Definition Schemas](NPC_Definition_Schemas.md) (4 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (3 shared connections)

## Source Files

- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_service.py`
- `server/npc/threading.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/npc/test_spawn_validator.py`

## Audit Trail

- EXTRACTED: 993 (96%)
- INFERRED: 41 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*