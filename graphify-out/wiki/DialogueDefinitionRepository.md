# DialogueDefinitionRepository

> 70 nodes

## Key Concepts

- **DialogueDefinitionRepository** (32 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **dialogue_definitions_api.py** (27 connections) — `server/api/admin/dialogue_definitions_api.py`
- **test_dialogue_definitions_api.py** (26 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_dialogue_definition_repository.py** (20 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **create_dialogue_definition()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **list_dialogue_definitions()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **upsert_dialogue_definition()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **get_dialogue_definition()** (13 connections) — `server/api/admin/dialogue_definitions_api.py`
- **delete_dialogue_definition()** (12 connections) — `server/api/admin/dialogue_definitions_api.py`
- **to_response()** (10 connections) — `server/api/admin/dialogue_definitions_api.py`
- **DialogueDefinitionResponse** (9 connections) — `server/api/admin/dialogue_schemas.py`
- **asyncio** (8 connections)
- **asyncio** (8 connections)
- **DialogueDefinitionCreate** (7 connections) — `server/api/admin/dialogue_schemas.py`
- **DialogueDefinitionUpdate** (7 connections) — `server/api/admin/dialogue_schemas.py`
- **dialogue_schemas.py** (7 connections) — `server/api/admin/dialogue_schemas.py`
- **_definition_dict()** (6 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_mock_session_with_rows()** (6 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_create_dialogue_definition_upserts()** (5 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_upsert_dialogue_definition()** (5 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **Request** (5 connections)
- **_dialogue_row()** (4 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_get_dialogue_definition_found()** (4 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_list_dialogue_definitions_returns_rows()** (4 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_get_by_id_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- *... and 45 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (28 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (11 shared connections)
- [talk_command.py](talk_command.py.md) (7 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [User](User.md) (6 shared connections)
- [quest_commands.py](quest_commands.py.md) (1 shared connections)

## Source Files

- `server/api/admin/dialogue_definitions_api.py`
- `server/api/admin/dialogue_schemas.py`
- `server/game/dialogue/dialogue_service.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/tests/unit/api/test_dialogue_definitions_api.py`
- `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`

## Audit Trail

- EXTRACTED: 202 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*