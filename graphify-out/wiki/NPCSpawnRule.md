# NPCSpawnRule

> 129 nodes

## Key Concepts

- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_JSONDict** (10 connections)
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- **._execute_create_spawn_rule()** (8 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **.create_spawn_rule()** (7 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **Base** (6 connections) — `server/models/npc.py`
- **.get_base_stats()** (6 connections) — `server/models/npc.py`
- **._check_dict_condition()** (6 connections) — `server/models/npc.py`
- **._spawn_value_allows_spawn()** (6 connections) — `server/models/npc.py`
- **.get_spawn_rule()** (6 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.get_spawn_rules()** (6 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **AsyncSession** (6 connections)
- **.get_spawn_conditions()** (5 connections) — `server/models/npc.py`
- **._single_spawn_condition_ok()** (5 connections) — `server/models/npc.py`
- **.get_ai_integration_stub()** (4 connections) — `server/models/npc.py`
- **.get_behavior_config()** (4 connections) — `server/models/npc.py`
- **.check_spawn_conditions()** (4 connections) — `server/models/npc.py`
- **.__init__()** (4 connections) — `server/npc/spawning_models.py`
- **.delete_spawn_rule()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._validate_spawn_rule_inputs()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.set_ai_integration_stub()** (3 connections) — `server/models/npc.py`
- *... and 104 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (33 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [npc_service/__init__.py](npc_service-__init__.py.md) (4 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (3 shared connections)
- [models/player.py](models-player.py.md) (2 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (2 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (2 shared connections)
- [test_npc_definitions_api.py](test_npc_definitions_api.py.md) (1 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (1 shared connections)
- [_NPCCombatIntegrationValidationDeps](_NPCCombatIntegrationValidationDeps.md) (1 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)
- [definition.py](definition.py.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/npc/spawning_models.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`

## Audit Trail

- EXTRACTED: 223 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*