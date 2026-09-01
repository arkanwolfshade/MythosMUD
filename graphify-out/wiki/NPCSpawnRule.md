# NPCSpawnRule

> 85 nodes

## Key Concepts

- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **npc_service/__init__.py** (22 connections) — `server/services/npc_service/__init__.py`
- **definition_crud.py** (16 connections) — `server/services/npc_service/definition_crud.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **queries.py** (12 connections) — `server/services/npc_service/queries.py`
- **spawn_rule_crud.py** (12 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- **._execute_create_spawn_rule()** (8 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCQueryMixin** (7 connections) — `server/services/npc_service/queries.py`
- **.create_spawn_rule()** (7 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **Base** (6 connections) — `server/models/npc.py`
- **CreateNPCDefinitionInput** (6 connections) — `server/services/npc_service_models.py`
- **NPCDefinitionCreateParams** (6 connections) — `server/services/npc_service_models.py`
- **._check_dict_condition()** (6 connections) — `server/models/npc.py`
- **._spawn_value_allows_spawn()** (6 connections) — `server/models/npc.py`
- **.get_spawn_rule()** (6 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.get_spawn_rules()** (6 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **AsyncSession** (6 connections)
- **._single_spawn_condition_ok()** (5 connections) — `server/models/npc.py`
- **.get_npc_definitions_by_sub_zone()** (5 connections) — `server/services/npc_service/queries.py`
- *... and 60 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (22 shared connections)
- [get_logger](get_logger.md) (22 shared connections)
- [EventBus](EventBus.md) (15 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (11 shared connections)
- [test_spawn_validator.py](test_spawn_validator.py.md) (7 shared connections)
- [test_npc_definitions_api.py](test_npc_definitions_api.py.md) (7 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (7 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (5 shared connections)
- [_JSONDict](_JSONDict.md) (5 shared connections)
- [Player](Player.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [test_population_control.py](test_population_control.py.md) (2 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/npc_metadata.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 259 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*