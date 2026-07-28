# Player Respawn Service

> 45 nodes · cohesion 0.09

## Key Concepts

- **npc_definitions_api.py** (29 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_schemas.py** (21 connections) — `server/api/admin/npc_schemas.py`
- **_update_npc_definition_internal()** (13 connections) — `server/api/admin/npc_definitions_api.py`
- **create_npc_definition()** (11 connections) — `server/api/admin/npc_definitions_api.py`
- **BaseModel** (11 connections)
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **get_npc_definition()** (10 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_definitions()** (10 connections) — `server/api/admin/npc_definitions_api.py`
- **NPCDefinitionResponse** (10 connections) — `server/api/admin/npc_schemas.py`
- **.from_orm()** (10 connections) — `server/api/admin/npc_schemas.py`
- **delete_npc_definition()** (8 connections) — `server/api/admin/npc_definitions_api.py`
- **update_npc_definition()** (8 connections) — `server/api/admin/npc_definitions_api.py`
- **NPCDefinitionUpdate** (7 connections) — `server/api/admin/npc_schemas.py`
- **Request** (6 connections)
- **build_update_params_from_model()** (6 connections) — `server/api/admin/npc_schemas.py`
- **AsyncSession** (5 connections)
- **NPCDefinitionCreate** (5 connections) — `server/api/admin/npc_schemas.py`
- **NPCMoveRequest** (5 connections) — `server/api/admin/npc_schemas.py`
- **NPCSpawnRuleCreate** (5 connections) — `server/api/admin/npc_schemas.py`
- **NPCAIIntegrationModel** (4 connections) — `server/api/admin/npc_schemas.py`
- **NPCBaseStatsModel** (4 connections) — `server/api/admin/npc_schemas.py`
- **NPCBehaviorConfigModel** (4 connections) — `server/api/admin/npc_schemas.py`
- **NPCSpawnConditionsModel** (4 connections) — `server/api/admin/npc_schemas.py`
- **NPCSpawnRequest** (4 connections) — `server/api/admin/npc_schemas.py`
- **NPC definition admin endpoints for MythosMUD.  Split out from server.api.admin.n** (1 connections) — `server/api/admin/npc_definitions_api.py`
- *... and 20 more nodes in this community*

## Relationships

- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (18 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (9 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (9 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (6 shared connections)
- [Api Admin Npc](Api_Admin_Npc.md) (6 shared connections)
- [WebSocket Handler Helpers](WebSocket_Handler_Helpers.md) (5 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (3 shared connections)
- [Admin Auth Service Tests](Admin_Auth_Service_Tests.md) (2 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (1 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (1 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (1 shared connections)

## Source Files

- `server/api/admin/npc_definitions_api.py`
- `server/api/admin/npc_schemas.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 232 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*