# test_npc_spawn_rules_api.py

> 28 nodes

## Key Concepts

- **test_npc_spawn_rules_api.py** (16 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **create_npc_spawn_rule()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **get_npc_spawn_rules()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **delete_npc_spawn_rule()** (12 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **NPCSpawnRuleResponse** (7 connections) — `server/api/admin/npc_schemas.py`
- **asyncio** (7 connections)
- **.from_orm()** (6 connections) — `server/api/admin/npc_schemas.py`
- **test_create_npc_spawn_rule_rolls_back()** (4 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_delete_npc_spawn_rule_not_found()** (4 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_get_npc_spawn_rules_generic_error()** (4 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_create_npc_spawn_rule_success()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_delete_npc_spawn_rule_success()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_get_npc_spawn_rules_http_exception_propagates()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_get_npc_spawn_rules_success()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **AsyncSession** (3 connections)
- **Request** (3 connections)
- **mock_session()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **mock_user()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **fixture** (2 connections)
- **delete** (1 connections)
- **get** (1 connections)
- **post** (1 connections)
- **Model for NPC spawn rule responses.** (1 connections) — `server/api/admin/npc_schemas.py`
- **Create response from ORM object.** (1 connections) — `server/api/admin/npc_schemas.py`
- **Get all NPC spawn rules.** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`
- *... and 3 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [DatabaseError](DatabaseError.md) (6 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (6 shared connections)
- [npc_definitions_api.py](npc_definitions_api.py.md) (4 shared connections)
- [User](User.md) (3 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (1 shared connections)

## Source Files

- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/tests/unit/api/test_npc_spawn_rules_api.py`

## Audit Trail

- EXTRACTED: 69 (92%)
- INFERRED: 6 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*