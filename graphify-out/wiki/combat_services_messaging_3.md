# combat services messaging

> 24 nodes

## Key Concepts

- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **_make_session_context()** (11 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **_row_for_quest_definition()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_id_success()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_id_database_error()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_name_success()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_name_database_error()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_list_quest_ids_offered_by_database_error()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_id_not_found()** (3 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_name_not_found()** (3 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_list_quest_ids_offered_by_success()** (3 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_list_quest_ids_offered_by_empty()** (3 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Unit tests for QuestDefinitionRepository.  Tests get_by_id, get_by_name, and lis** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Return context manager that yields mock_session for async with.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Build a procedure result row (mappings().first() return value) for QuestDefiniti** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test get_by_id returns definition when found (procedure returns row, repo maps t** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test get_by_id returns None when not found.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test get_by_id raises DatabaseError on DB failure.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test get_by_name returns definition when found by common name.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test get_by_name returns None when not found.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test get_by_name raises DatabaseError on DB failure.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test list_quest_ids_offered_by returns quest IDs for entity (procedure returns r** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test list_quest_ids_offered_by returns empty list when no offers.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test list_quest_ids_offered_by raises DatabaseError on DB failure.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (6 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (4 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_quest_definition_repository.py`

## Audit Trail

- EXTRACTED: 76 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*