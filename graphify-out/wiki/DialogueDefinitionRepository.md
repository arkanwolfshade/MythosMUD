# DialogueDefinitionRepository

> 22 nodes

## Key Concepts

- **DialogueDefinitionRepository** (30 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_dialogue_definition_repository.py** (20 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **asyncio** (8 connections)
- **_definition_dict()** (6 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_mock_session_with_rows()** (6 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_get_by_id_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_get_by_id_not_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_get_by_npc_definition_id_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_list_all_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_list_all_success()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_upsert_success()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_delete_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_delete_true()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **.__init__()** (2 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_definition_dict_coerces_keys()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_definition_dict_non_dict()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_row_to_dialogue()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **fixture** (1 connections)
- **Coerce JSONB definition cell to a plain string-keyed dict.** (1 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **Repository for dialogue_definitions via stored procedures.** (1 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **Unit tests for DialogueDefinitionRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`

## Relationships

- [DatabaseError](DatabaseError.md) (17 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (6 shared connections)
- [talk_command.py](talk_command.py.md) (3 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`

## Audit Trail

- EXTRACTED: 58 (82%)
- INFERRED: 13 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*