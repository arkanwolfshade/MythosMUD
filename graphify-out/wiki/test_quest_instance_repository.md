# test quest instance repository

> 30 nodes

## Key Concepts

- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **_row_for_quest_instance()** (6 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_create_success()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_create_database_error()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_success()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_active_by_player_success()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_completed_by_player_success()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_completed_by_player_database_error()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **mock_quest_instance()** (3 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_not_found()** (3 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_accepts_uuid()** (3 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_update_state_and_progress_success()** (3 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_update_state_and_progress_no_op()** (3 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_active_by_player_empty()** (3 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Unit tests for QuestInstanceRepository.  Tests create, get_by_player_and_quest,** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Create a mock QuestInstance.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Return context manager that yields mock_session for async with.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Build a procedure result row (mappings().first() return value) for QuestInstance** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test create calls procedure, commits, and returns mapped instance.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test create raises DatabaseError on DB failure.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test get_by_player_and_quest returns mapped instance when found.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test get_by_player_and_quest returns None when not found.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test get_by_player_and_quest accepts UUID for player_id.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test update_state_and_progress updates and commits.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- *... and 5 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (5 shared connections)
- [QuestCompleted](QuestCompleted.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [Base](Base.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 95 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*