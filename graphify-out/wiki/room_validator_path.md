# room validator path

> 23 nodes

## Key Concepts

- **test_npc_spawn_rules_api.py** (16 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **get_npc_spawn_rules()** (14 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **create_npc_spawn_rule()** (14 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **delete_npc_spawn_rule()** (11 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **NPCSpawnRuleResponse** (7 connections) — `server/api/admin/npc_schemas.py`
- **.from_orm()** (6 connections) — `server/api/admin/npc_schemas.py`
- **Request** (3 connections)
- **AsyncSession** (3 connections)
- **test_get_npc_spawn_rules_generic_error()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_create_npc_spawn_rule_rolls_back()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_delete_npc_spawn_rule_not_found()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_get_npc_spawn_rules_success()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_get_npc_spawn_rules_http_exception_propagates()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_create_npc_spawn_rule_success()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_delete_npc_spawn_rule_success()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **Model for NPC spawn rule responses.** (1 connections) — `server/api/admin/npc_schemas.py`
- **Create response from ORM object.** (1 connections) — `server/api/admin/npc_schemas.py`
- **Get all NPC spawn rules.** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **Create a new NPC spawn rule.** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **Delete an NPC spawn rule.** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **mock_user()** (1 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **mock_session()** (1 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **Unit tests for NPC spawn rules admin API.** (1 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`

## Relationships

- [admin auth service](admin_auth_service.md) (15 shared connections)
- [Exception Containers](Exception_Containers.md) (10 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/tests/unit/api/test_npc_spawn_rules_api.py`

## Audit Trail

- EXTRACTED: 96 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*