# Api Admin Npc

> 14 nodes · cohesion 0.23

## Key Concepts

- **npc_spawn_rules_api.py** (22 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **create_npc_spawn_rule()** (11 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **get_npc_spawn_rules()** (10 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **delete_npc_spawn_rule()** (8 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **NPCSpawnRuleResponse** (7 connections) — `server/api/admin/npc_schemas.py`
- **.from_orm()** (6 connections) — `server/api/admin/npc_schemas.py`
- **AsyncSession** (3 connections)
- **Request** (3 connections)
- **Model for NPC spawn rule responses.** (1 connections) — `server/api/admin/npc_schemas.py`
- **Create response from ORM object.** (1 connections) — `server/api/admin/npc_schemas.py`
- **NPC spawn rule admin endpoints.  Split out from server.api.admin.npc to keep fil** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **Get all NPC spawn rules.** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **Create a new NPC spawn rule.** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **Delete an NPC spawn rule.** (1 connections) — `server/api/admin/npc_spawn_rules_api.py`

## Relationships

- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (10 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (6 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (6 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (4 shared connections)
- [Admin Auth Service Tests](Admin_Auth_Service_Tests.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (1 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (1 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (1 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)

## Source Files

- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`

## Audit Trail

- EXTRACTED: 76 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*