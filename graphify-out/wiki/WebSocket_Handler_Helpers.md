# WebSocket Handler Helpers

> 43 nodes · cohesion 0.08

## Key Concepts

- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **definition_crud.py** (15 connections) — `server/services/npc_service/definition_crud.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (8 connections)
- **._build_npc_update_data()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definitions()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **CreateNPCDefinitionInput** (6 connections) — `server/services/npc_service_models.py`
- **NPCDefinitionCreateParams** (6 connections) — `server/services/npc_service_models.py`
- **.get_npc_definition_by_name()** (5 connections) — `server/services/npc_service/definition_crud.py`
- **._add_json_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._add_simple_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **.delete_npc_definition()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._log_npc_definition_created()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **Any** (4 connections)
- **._validate_create_npc_definition_params()** (3 connections) — `server/services/npc_service/definition_crud.py`
- **._validate_npc_update_params()** (3 connections) — `server/services/npc_service/definition_crud.py`
- **TypedDict** (3 connections)
- **NPC definition CRUD operations for NPCService.** (1 connections) — `server/services/npc_service/definition_crud.py`
- **Execute create_npc_definition stored procedure and return the created definition** (1 connections) — `server/services/npc_service/definition_crud.py`
- *... and 18 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (25 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (5 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (4 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (4 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (1 shared connections)

## Source Files

- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 185 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*