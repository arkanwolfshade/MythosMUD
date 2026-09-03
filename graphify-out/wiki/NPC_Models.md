# NPC Models

> 210 nodes

## Key Concepts

- **NPCDefinition** (92 connections) — `server/models/npc.py`
- **NPCSpawnRule** (45 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **npc_service/__init__.py** (22 connections) — `server/services/npc_service/__init__.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **definition_crud.py** (16 connections) — `server/services/npc_service/definition_crud.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **queries.py** (12 connections) — `server/services/npc_service/queries.py`
- **spawn_rule_crud.py** (12 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_JSONDict** (10 connections)
- **NPCDefinitionType** (9 connections) — `server/models/npc.py`
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **NPCDefinitionUpdateParams** (9 connections) — `server/services/npc_service_models.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- **._execute_create_spawn_rule()** (8 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **AsyncSession** (8 connections)
- **NPCQueryMixin** (7 connections) — `server/services/npc_service/queries.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- *... and 185 more nodes in this community*

## Relationships

- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (23 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (12 shared connections)
- [Test Zone Config Loader](Test_Zone_Config_Loader.md) (11 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (9 shared connections)
- [Npc Base](Npc_Base.md) (8 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (7 shared connections)
- [Migrate Combat Data](Migrate_Combat_Data.md) (7 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (7 shared connections)
- [Test Npc Service](Test_Npc_Service.md) (5 shared connections)
- [Spawning Service](Spawning_Service.md) (5 shared connections)
- [Threading](Threading.md) (4 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (3 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_types.py`
- `server/npc/population_control.py`
- `server/npc/spawning_models.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`

## Audit Trail

- EXTRACTED: 467 (100%)
- INFERRED: 2 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*