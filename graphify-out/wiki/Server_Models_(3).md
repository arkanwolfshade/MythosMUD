# Server Models (3)

> 164 nodes

## Key Concepts

- **NPCSpawnRule** (55 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (22 connections) — `server/npc/spawn_validator.py`
- **spawn_validator.py** (11 connections) — `server/npc/spawn_validator.py`
- **spawn_rule_crud.py** (11 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_JSONDict** (10 connections)
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **._execute_create_spawn_rule()** (8 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **.create_spawn_rule()** (7 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **Base** (6 connections) — `server/models/npc.py`
- **.get_base_stats()** (6 connections) — `server/models/npc.py`
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
- *... and 139 more nodes in this community*

## Relationships

- [Server Npc](Server_Npc.md) (42 shared connections)
- [Server Events](Server_Events.md) (4 shared connections)
- [Server Npc (9)](Server_Npc_%289%29.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (4 shared connections)
- [Server Admin](Server_Admin.md) (3 shared connections)
- [Server Npc (4)](Server_Npc_%284%29.md) (3 shared connections)
- [Server Persistence](Server_Persistence.md) (3 shared connections)
- [Server Models (14)](Server_Models_%2814%29.md) (2 shared connections)
- [Server Services (64)](Server_Services_%2864%29.md) (2 shared connections)
- [Server Npc (15)](Server_Npc_%2815%29.md) (2 shared connections)
- [Server Services (4)](Server_Services_%284%29.md) (1 shared connections)
- [Server Services (6)](Server_Services_%286%29.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/npc/test_spawn_validator.py`

## Audit Trail

- EXTRACTED: 515 (96%)
- INFERRED: 22 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*