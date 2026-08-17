# DialogueDefinitionRepository

> 59 nodes

## Key Concepts

- **DialogueDefinitionRepository** (30 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_dialogue_definition_repository.py** (21 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **dialogue_service.py** (17 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service.py** (14 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **DialogueDefinition** (12 connections) — `server/models/dialogue.py`
- **_row_to_dialogue()** (11 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **asyncio** (8 connections)
- **_as_dialogue_row()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.get_by_id()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.get_by_npc_definition_id()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.list_all()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.upsert()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **reset_dialogue_service_for_tests()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **_definition_dict()** (6 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_mock_session_with_rows()** (6 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **_DialogueRow** (5 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_dialogue_service_start_and_choose()** (5 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **.delete()** (4 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_dialogue_service_choose_without_cursor()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_get_by_id_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_get_by_id_not_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_get_by_npc_definition_id_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_list_all_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_list_all_success()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_upsert_success()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- *... and 34 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (21 shared connections)
- [talk_command.py](talk_command.py.md) (17 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (9 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [get_session_maker](get_session_maker.md) (5 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/game/dialogue/dialogue_service.py`
- `server/models/dialogue.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/tests/unit/game/test_dialogue_service.py`
- `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`

## Audit Trail

- EXTRACTED: 140 (89%)
- INFERRED: 17 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*