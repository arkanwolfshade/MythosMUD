# message broadcaster realtime

> 21 nodes

## Key Concepts

- **DialogueDefinitionRepository** (32 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_dialogue_definition_repository.py** (20 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **_definition_dict()** (6 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_mock_session_with_rows()** (6 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_list_all_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_list_all_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_get_by_id_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_get_by_id_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_get_by_npc_definition_id_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_upsert_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **.__init__()** (2 connections) — `server/game/dialogue/dialogue_service.py`
- **.__init__()** (2 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_definition_dict_non_dict()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_definition_dict_coerces_keys()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_row_to_dialogue()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **repo()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_delete_true()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_delete_not_found()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **Coerce JSONB definition cell to a plain string-keyed dict.** (1 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **Repository for dialogue_definitions via stored procedures.** (1 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **Unit tests for DialogueDefinitionRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (17 shared connections)
- [player preferences services](player_preferences_services.md) (6 shared connections)
- [dialogue service game](dialogue_service_game.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/game/dialogue/dialogue_service.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`

## Audit Trail

- EXTRACTED: 95 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*