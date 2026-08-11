# Whisper Remediation Plan

> 49 nodes

## Key Concepts

- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **__init__.py** (15 connections) — `server/services/npc_service/__init__.py`
- **definition_crud.py** (15 connections) — `server/services/npc_service/definition_crud.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **spawn_rule_crud.py** (11 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (8 connections)
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definitions()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **._build_npc_update_data()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **CreateNPCDefinitionInput** (6 connections) — `server/services/npc_service_models.py`
- **NPCDefinitionCreateParams** (6 connections) — `server/services/npc_service_models.py`
- **.get_npc_definition_by_name()** (5 connections) — `server/services/npc_service/definition_crud.py`
- **._log_npc_definition_created()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._add_simple_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **Any** (4 connections)
- **._add_json_field()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **.delete_npc_definition()** (4 connections) — `server/services/npc_service/definition_crud.py`
- **._validate_create_npc_definition_params()** (3 connections) — `server/services/npc_service/definition_crud.py`
- **._validate_npc_update_params()** (3 connections) — `server/services/npc_service/definition_crud.py`
- *... and 24 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (17 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (7 shared connections)
- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (5 shared connections)
- [Cursor Plans Best](Cursor_Plans_Best.md) (5 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (3 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (1 shared connections)

## Source Files

- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 225 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*