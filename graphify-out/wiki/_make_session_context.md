# _make_session_context

> 23 nodes

## Key Concepts

- **_make_session_context()** (11 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **asyncio** (9 connections)
- **test_get_by_id_database_error()** (5 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_id_success()** (5 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_name_database_error()** (5 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_name_success()** (5 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_list_quest_ids_offered_by_database_error()** (5 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **_row_for_quest_definition()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_id_not_found()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_name_not_found()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_list_quest_ids_offered_by_empty()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_list_quest_ids_offered_by_success()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test get_by_id raises DatabaseError on DB failure.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test get_by_name returns definition when found by common name.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test get_by_name returns None when not found.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test get_by_name raises DatabaseError on DB failure.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test list_quest_ids_offered_by returns quest IDs for entity (procedure returns…** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test list_quest_ids_offered_by returns empty list when no offers.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test list_quest_ids_offered_by raises DatabaseError on DB failure.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Return context manager that yields mock_session for async with.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Build a procedure result row (mappings().first() return value) for…** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test get_by_id returns definition when found (procedure returns row, repo maps…** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Test get_by_id returns None when not found.** (1 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`

## Relationships

- [get_logger](get_logger.md) (14 shared connections)

## Source Files

- `server/tests/unit/persistence/test_quest_definition_repository.py`

## Audit Trail

- EXTRACTED: 42 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*