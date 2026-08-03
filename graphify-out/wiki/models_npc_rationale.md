# models npc rationale

> 103 nodes

## Key Concepts

- **NPCSpawnRule** (55 connections) — `server/models/npc.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (22 connections) — `server/npc/spawn_validator.py`
- **_JSONDict** (10 connections)
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._execute_create_spawn_rule()** (8 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **.create_spawn_rule()** (7 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._check_dict_condition()** (6 connections) — `server/models/npc.py`
- **._spawn_value_allows_spawn()** (6 connections) — `server/models/npc.py`
- **.get_spawn_rules()** (6 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **AsyncSession** (6 connections)
- **.get_spawn_rule()** (6 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.get_spawn_conditions()** (5 connections) — `server/models/npc.py`
- **._single_spawn_condition_ok()** (5 connections) — `server/models/npc.py`
- **.get_behavior_config()** (4 connections) — `server/models/npc.py`
- **.get_ai_integration_stub()** (4 connections) — `server/models/npc.py`
- **.check_spawn_conditions()** (4 connections) — `server/models/npc.py`
- **._validate_spawn_rule_inputs()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **.delete_spawn_rule()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **test_should_spawn_npc_spawn_rule_passes()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_population()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_conditions()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_should_spawn_npc_spawn_rule_fails_probability()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- *... and 78 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (21 shared connections)
- [combat commands handler](combat_commands_handler.md) (9 shared connections)
- [command inventory factories](command_inventory_factories.md) (6 shared connections)
- [spell game magic](spell_game_magic.md) (4 shared connections)
- [command input commands](command_input_commands.md) (2 shared connections)
- [admin auth service](admin_auth_service.md) (2 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (2 shared connections)
- [npc service services](npc_service_services.md) (2 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 337 (94%)
- INFERRED: 23 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*