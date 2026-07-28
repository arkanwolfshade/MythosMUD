# NPC Definition CRUD

> 53 nodes · cohesion 0.06

## Key Concepts

- **NPCSpawnRule** (55 connections) — `server/models/npc.py`
- **spawn_rule_crud.py** (11 connections) — `server/services/npc_service/spawn_rule_crud.py`
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
- **.delete_spawn_rule()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._validate_spawn_rule_inputs()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._check_list_condition()** (3 connections) — `server/models/npc.py`
- **._check_missing_key_condition()** (3 connections) — `server/models/npc.py`
- **._check_simple_condition()** (3 connections) — `server/models/npc.py`
- **._game_value_above_bound()** (3 connections) — `server/models/npc.py`
- **._game_value_below_bound()** (3 connections) — `server/models/npc.py`
- **.set_spawn_conditions()** (3 connections) — `server/models/npc.py`
- **.load_spawn_rules()** (3 connections) — `server/npc/population_control.py`
- **test_load_spawn_rules()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **sample_spawn_rule()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **.can_spawn_with_population()** (2 connections) — `server/models/npc.py`
- *... and 28 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (16 shared connections)
- [NPC Spawn Validator](NPC_Spawn_Validator.md) (10 shared connections)
- [Follow Service Tests](Follow_Service_Tests.md) (9 shared connections)
- [Logout Session Chrome Hooks](Logout_Session_Chrome_Hooks.md) (4 shared connections)
- [WebSocket Handler Helpers](WebSocket_Handler_Helpers.md) (4 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (3 shared connections)
- [Command Input Validator](Command_Input_Validator.md) (2 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (1 shared connections)
- [Api Admin Npc](Api_Admin_Npc.md) (1 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (1 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 193 (94%)
- INFERRED: 13 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*