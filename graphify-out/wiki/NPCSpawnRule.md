# NPCSpawnRule

> 93 nodes

## Key Concepts

- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **test_spawn_validator.py** (25 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- **._execute_create_spawn_rule()** (8 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.create_spawn_rule()** (7 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._check_dict_condition()** (6 connections) — `server/models/npc.py`
- **._spawn_value_allows_spawn()** (6 connections) — `server/models/npc.py`
- **_spawn_rule_passes()** (6 connections) — `server/npc/spawn_validator.py`
- **.get_spawn_rule()** (6 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.get_spawn_rules()** (6 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **AsyncSession** (6 connections)
- **._single_spawn_condition_ok()** (5 connections) — `server/models/npc.py`
- **_population_allows_spawn()** (5 connections) — `server/npc/spawn_validator.py`
- **.check_spawn_conditions()** (4 connections) — `server/models/npc.py`
- **.__init__()** (4 connections) — `server/npc/spawning_models.py`
- **.delete_spawn_rule()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._validate_spawn_rule_inputs()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **mock_zone_config()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **._check_list_condition()** (3 connections) — `server/models/npc.py`
- **._check_missing_key_condition()** (3 connections) — `server/models/npc.py`
- **._check_simple_condition()** (3 connections) — `server/models/npc.py`
- *... and 68 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (24 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (8 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (7 shared connections)
- [population_control.py](population_control.py.md) (3 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [test_population_control.py](test_population_control.py.md) (1 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_models.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/npc/test_spawn_validator.py`

## Audit Trail

- EXTRACTED: 194 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*