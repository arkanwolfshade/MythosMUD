# create_npc_spawn_rule

> 19 nodes

## Key Concepts

- **create_npc_spawn_rule()** (12 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **get_npc_spawn_rules()** (11 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **delete_npc_spawn_rule()** (9 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **NPCSpawnRuleResponse** (7 connections) — `server/api/admin/npc_schemas.py`
- **.from_orm()** (6 connections) — `server/api/admin/npc_schemas.py`
- **NPCSpawnRuleCreate** (5 connections) — `server/api/admin/npc_schemas.py`
- **NPCSpawnConditionsModel** (4 connections) — `server/api/admin/npc_schemas.py`
- **AsyncSession** (3 connections)
- **Request** (3 connections)
- **delete** (1 connections)
- **get** (1 connections)
- **post** (1 connections)
- **Model for creating NPC spawn rules.** (1 connections) — `server/api/admin/npc_schemas.py`
- **Model for NPC spawn rule responses.** (1 connections) — `server/api/admin/npc_schemas.py`
- **Create response from ORM object.** (1 connections) — `server/api/admin/npc_schemas.py`
- **Model for NPC spawn conditions.** (1 connections) — `server/api/admin/npc_schemas.py`
- **Get all NPC spawn rules.** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **Create a new NPC spawn rule.** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **Delete an NPC spawn rule.** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`

## Relationships

- [get_admin_auth_service](get_admin_auth_service.md) (12 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [User](User.md) (3 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*