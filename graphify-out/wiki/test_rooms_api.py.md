# test_rooms_api.py

> 47 nodes

## Key Concepts

- **dialogue_definitions_api.py** (28 connections) — `server/api/admin/dialogue_definitions_api.py`
- **test_dialogue_definitions_api.py** (28 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **create_dialogue_definition()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **list_dialogue_definitions()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **upsert_dialogue_definition()** (14 connections) — `server/api/admin/dialogue_definitions_api.py`
- **get_dialogue_definition()** (13 connections) — `server/api/admin/dialogue_definitions_api.py`
- **delete_dialogue_definition()** (12 connections) — `server/api/admin/dialogue_definitions_api.py`
- **to_response()** (10 connections) — `server/api/admin/dialogue_definitions_api.py`
- **DialogueDefinitionResponse** (9 connections) — `server/api/admin/dialogue_schemas.py`
- **dialogue_schemas.py** (9 connections) — `server/api/admin/dialogue_schemas.py`
- **asyncio** (8 connections)
- **DialogueDefinitionCreate** (7 connections) — `server/api/admin/dialogue_schemas.py`
- **DialogueDefinitionUpdate** (7 connections) — `server/api/admin/dialogue_schemas.py`
- **test_create_dialogue_definition_upserts()** (5 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_upsert_dialogue_definition()** (5 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **Request** (5 connections)
- **_dialogue_row()** (4 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_delete_dialogue_definition_not_found()** (4 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_get_dialogue_definition_found()** (4 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_get_dialogue_definition_not_found()** (4 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_list_dialogue_definitions_db_error()** (4 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_list_dialogue_definitions_returns_rows()** (4 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_delete_dialogue_definition_success()** (3 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_to_response_maps_row()** (3 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **BaseModel** (3 connections)
- *... and 22 more nodes in this community*

## Relationships

- [maps.py](maps.py.md) (16 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (10 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (8 shared connections)
- [useGameTerminal.ts](useGameTerminal.ts.md) (6 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (6 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (3 shared connections)
- [GameTerminal.tsx](GameTerminal.tsx.md) (1 shared connections)
- [models/container.py](models-container.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/api/admin/dialogue_definitions_api.py`
- `server/api/admin/dialogue_schemas.py`
- `server/tests/unit/api/test_dialogue_definitions_api.py`

## Audit Trail

- EXTRACTED: 137 (92%)
- INFERRED: 12 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*