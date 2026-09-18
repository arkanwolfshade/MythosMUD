# Community 304

> 53 nodes

## Key Concepts

- **NPCSpawnRule** (42 connections) — `server/models/npc.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
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
- **CreateNPCDefinitionInput** (4 connections) — `server/services/npc_service_models.py`
- **NPCDefinitionCreateParams** (4 connections) — `server/services/npc_service_models.py`
- **.check_spawn_conditions()** (4 connections) — `server/models/npc.py`
- **.delete_spawn_rule()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._validate_spawn_rule_inputs()** (4 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **._check_list_condition()** (3 connections) — `server/models/npc.py`
- **._check_missing_key_condition()** (3 connections) — `server/models/npc.py`
- **._check_simple_condition()** (3 connections) — `server/models/npc.py`
- **._game_value_above_bound()** (3 connections) — `server/models/npc.py`
- **._game_value_below_bound()** (3 connections) — `server/models/npc.py`
- **.load_spawn_rules()** (3 connections) — `server/npc/population_control.py`
- **TypedDict** (3 connections)
- *... and 28 more nodes in this community*

## Relationships

- [Community 131](Community_131.md) (10 shared connections)
- [Community 241](Community_241.md) (9 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (7 shared connections)
- [Admin NPC Management API](Admin_NPC_Management_API.md) (5 shared connections)
- [Community 563](Community_563.md) (4 shared connections)
- [Community 829](Community_829.md) (4 shared connections)
- [Community 128](Community_128.md) (2 shared connections)
- [Community 33](Community_33.md) (2 shared connections)
- [Community 91](Community_91.md) (1 shared connections)
- [Community 41](Community_41.md) (1 shared connections)
- [NPC Population Control](NPC_Population_Control.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 126 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*