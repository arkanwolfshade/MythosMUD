# MetricsCollector

> 47 nodes

## Key Concepts

- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- **._execute_create_spawn_rule()** (8 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.create_spawn_rule()** (7 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._check_dict_condition()** (6 connections) — `server/models/npc.py`
- **._spawn_value_allows_spawn()** (6 connections) — `server/models/npc.py`
- **.get_spawn_rule()** (6 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.get_spawn_rules()** (6 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **AsyncSession** (6 connections)
- **._single_spawn_condition_ok()** (5 connections) — `server/models/npc.py`
- **.check_spawn_conditions()** (4 connections) — `server/models/npc.py`
- **.__init__()** (4 connections) — `server/npc/spawning_models.py`
- **.delete_spawn_rule()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._validate_spawn_rule_inputs()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._check_list_condition()** (3 connections) — `server/models/npc.py`
- **._check_missing_key_condition()** (3 connections) — `server/models/npc.py`
- **._check_simple_condition()** (3 connections) — `server/models/npc.py`
- **._game_value_above_bound()** (3 connections) — `server/models/npc.py`
- **._game_value_below_bound()** (3 connections) — `server/models/npc.py`
- **.load_spawn_rules()** (3 connections) — `server/npc/population_control.py`
- **.can_spawn_with_population()** (2 connections) — `server/models/npc.py`
- **.__repr__()** (2 connections) — `server/models/npc.py`
- **Any** (2 connections)
- **Any** (2 connections)
- *... and 22 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (15 shared connections)
- [test_security_headers.py](test_security_headers.py.md) (8 shared connections)
- [test_magic_healing_events.py](test_magic_healing_events.py.md) (4 shared connections)
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (2 shared connections)
- [Invite](Invite.md) (2 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)
- [item_instance_persistence_async.py](item_instance_persistence_async.py.md) (1 shared connections)
- [Recommended Test Additions](Recommended_Test_Additions.md) (1 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/npc/spawning_models.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 110 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*