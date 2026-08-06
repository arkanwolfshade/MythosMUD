# player preferences services

> 38 nodes

## Key Concepts

- **dialogue_definitions_api.py** (27 connections) — `server/api/admin/dialogue_definitions_api.py`
- **test_dialogue_definitions_api.py** (26 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **list_dialogue_definitions()** (13 connections) — `server/api/admin/dialogue_definitions_api.py`
- **upsert_dialogue_definition()** (13 connections) — `server/api/admin/dialogue_definitions_api.py`
- **create_dialogue_definition()** (13 connections) — `server/api/admin/dialogue_definitions_api.py`
- **get_dialogue_definition()** (12 connections) — `server/api/admin/dialogue_definitions_api.py`
- **delete_dialogue_definition()** (11 connections) — `server/api/admin/dialogue_definitions_api.py`
- **to_response()** (10 connections) — `server/api/admin/dialogue_definitions_api.py`
- **DialogueDefinitionResponse** (9 connections) — `server/api/admin/dialogue_schemas.py`
- **dialogue_schemas.py** (7 connections) — `server/api/admin/dialogue_schemas.py`
- **DialogueDefinitionCreate** (7 connections) — `server/api/admin/dialogue_schemas.py`
- **DialogueDefinitionUpdate** (7 connections) — `server/api/admin/dialogue_schemas.py`
- **Request** (5 connections)
- **test_create_dialogue_definition_upserts()** (5 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_upsert_dialogue_definition()** (5 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **_dialogue_row()** (4 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **BaseModel** (3 connections)
- **test_to_response_maps_row()** (3 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_list_dialogue_definitions_returns_rows()** (3 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_list_dialogue_definitions_db_error()** (3 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_get_dialogue_definition_found()** (3 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_get_dialogue_definition_not_found()** (3 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_delete_dialogue_definition_not_found()** (3 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_delete_dialogue_definition_success()** (2 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **Admin CRUD for dialogue_definitions (#583).** (1 connections) — `server/api/admin/dialogue_definitions_api.py`
- *... and 13 more nodes in this community*

## Relationships

- [persistence container rationale](persistence_container_rationale.md) (16 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (10 shared connections)
- [player requests schemas](player_requests_schemas.md) (6 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (6 shared connections)
- [dialogue service game](dialogue_service_game.md) (6 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [auth users rationale](auth_users_rationale.md) (1 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (1 shared connections)

## Source Files

- `server/api/admin/dialogue_definitions_api.py`
- `server/api/admin/dialogue_schemas.py`
- `server/tests/unit/api/test_dialogue_definitions_api.py`

## Audit Trail

- EXTRACTED: 207 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*