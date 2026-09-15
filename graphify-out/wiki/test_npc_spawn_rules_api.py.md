# test_npc_spawn_rules_api.py

> 37 nodes

## Key Concepts

- **test_npc_spawn_rules_api.py** (21 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **create_npc_spawn_rule()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **get_npc_spawn_rules()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **delete_npc_spawn_rule()** (12 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **NPCSpawnRuleCreate** (7 connections) — `server/api/admin/npc_schemas.py`
- **NPCSpawnRuleResponse** (7 connections) — `server/api/admin/npc_schemas.py`
- **asyncio** (7 connections)
- **NPCSpawnConditionsModel** (6 connections) — `server/api/admin/npc_schemas.py`
- **.from_orm()** (6 connections) — `server/api/admin/npc_schemas.py`
- **test_create_npc_spawn_rule_rolls_back()** (4 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_delete_npc_spawn_rule_not_found()** (4 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_get_npc_spawn_rules_generic_error()** (4 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_create_npc_spawn_rule_success()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_delete_npc_spawn_rule_success()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_get_npc_spawn_rules_http_exception_propagates()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_get_npc_spawn_rules_success()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_npc_spawn_conditions_model_still_allows_extra_field()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_npc_spawn_rule_create_rejects_unknown_field()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **AsyncSession** (3 connections)
- **Request** (3 connections)
- **mock_session()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **mock_user()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **BaseModel** (2 connections)
- **fixture** (2 connections)
- **delete** (1 connections)
- *... and 12 more nodes in this community*

## Relationships

- [test_admin_auth_service.py](test_admin_auth_service.py.md) (11 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [User](User.md) (3 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/tests/unit/api/test_npc_spawn_rules_api.py`

## Audit Trail

- EXTRACTED: 84 (91%)
- INFERRED: 8 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*