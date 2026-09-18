# Community 100

> 96 nodes

## Key Concepts

- **DialogueDefinitionRepository** (30 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **dialogue_definitions_api.py** (27 connections) — `server/api/admin/dialogue_definitions_api.py`
- **test_dialogue_definitions_api.py** (26 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_dialogue_definition_repository.py** (20 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **create_dialogue_definition()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **list_dialogue_definitions()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **upsert_dialogue_definition()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **get_dialogue_definition()** (13 connections) — `server/api/admin/dialogue_definitions_api.py`
- **delete_dialogue_definition()** (12 connections) — `server/api/admin/dialogue_definitions_api.py`
- **DialogueDefinition** (11 connections) — `server/models/dialogue.py`
- **_row_to_dialogue()** (11 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **dialogue_schemas.py** (11 connections) — `server/api/admin/dialogue_schemas.py`
- **to_response()** (10 connections) — `server/api/admin/dialogue_definitions_api.py`
- **DialogueDefinitionResponse** (9 connections) — `server/api/admin/dialogue_schemas.py`
- **DialogueDefinitionCreate** (8 connections) — `server/api/admin/dialogue_schemas.py`
- **DialogueDefinitionUpdate** (8 connections) — `server/api/admin/dialogue_schemas.py`
- **asyncio** (8 connections)
- **asyncio** (8 connections)
- **_as_dialogue_row()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.get_by_id()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.get_by_npc_definition_id()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.list_all()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.upsert()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_dialogue_schemas.py** (7 connections) — `server/tests/unit/api/admin/test_dialogue_schemas.py`
- **_definition_dict()** (6 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- *... and 71 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (25 shared connections)
- [Admin NPC Management API](Admin_NPC_Management_API.md) (13 shared connections)
- [Player Effects (Corruption/Fear/Lucidity)](Player_Effects_Corruption-Fear-Lucidity.md) (10 shared connections)
- [User Manager & Character Info](User_Manager_&_Character_Info.md) (10 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (9 shared connections)
- [Invite Codes & Session Maker (E2E)](Invite_Codes_&_Session_Maker_E2E.md) (5 shared connections)
- [Community 424](Community_424.md) (3 shared connections)
- [Community 45](Community_45.md) (2 shared connections)
- [Community 135](Community_135.md) (1 shared connections)
- [Community 28](Community_28.md) (1 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (1 shared connections)

## Source Files

- `server/api/admin/__init__.py`
- `server/api/admin/dialogue_definitions_api.py`
- `server/api/admin/dialogue_schemas.py`
- `server/models/dialogue.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/tests/unit/api/admin/test_dialogue_schemas.py`
- `server/tests/unit/api/test_dialogue_definitions_api.py`
- `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`

## Audit Trail

- EXTRACTED: 244 (91%)
- INFERRED: 25 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*