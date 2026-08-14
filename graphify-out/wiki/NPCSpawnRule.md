# NPCSpawnRule

> 76 nodes

## Key Concepts

- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_JSONDict** (10 connections)
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- **._execute_create_spawn_rule()** (8 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **.create_spawn_rule()** (7 connections) — `server/services/npc_service/spawn_rule_crud.py`
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
- **.delete_spawn_rule()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._validate_spawn_rule_inputs()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.set_ai_integration_stub()** (3 connections) — `server/models/npc.py`
- **.set_base_stats()** (3 connections) — `server/models/npc.py`
- **.set_behavior_config()** (3 connections) — `server/models/npc.py`
- **._check_list_condition()** (3 connections) — `server/models/npc.py`
- **._check_missing_key_condition()** (3 connections) — `server/models/npc.py`
- **._check_simple_condition()** (3 connections) — `server/models/npc.py`
- *... and 51 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (20 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (5 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [population_control.py](population_control.py.md) (1 shared connections)
- [test_population_control.py](test_population_control.py.md) (1 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`

## Audit Trail

- EXTRACTED: 147 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*