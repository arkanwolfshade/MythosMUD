# Community 482

> 37 nodes

## Key Concepts

- **npc_spawn_rules_api.py** (24 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **test_npc_spawn_rules_api.py** (21 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **create_npc_spawn_rule()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **get_npc_spawn_rules()** (15 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **delete_npc_spawn_rule()** (12 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **NPCSpawnRuleCreate** (7 connections) — `server/api/admin/npc_schemas.py`
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
- **test_npc_spawn_conditions_model_still_allows_extra_field()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **test_npc_spawn_rule_create_rejects_unknown_field()** (3 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **AsyncSession** (3 connections)
- **Request** (3 connections)
- **mock_session()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **mock_user()** (2 connections) — `server/tests/unit/api/test_npc_spawn_rules_api.py`
- **BaseModel** (2 connections)
- **fixture** (2 connections)
- **Create response from ORM object.** (2 connections) — `server/api/admin/npc_schemas.py`
- *... and 12 more nodes in this community*

## Relationships

- [Community 193](Community_193.md) (20 shared connections)
- [Container API Models](Container_API_Models.md) (8 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (6 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (4 shared connections)
- [Admin Auth Service](Admin_Auth_Service.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [NPC Definition JSON](NPC_Definition_JSON.md) (1 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (1 shared connections)

## Source Files

- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/tests/unit/api/test_npc_spawn_rules_api.py`

## Audit Trail

- EXTRACTED: 100 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*