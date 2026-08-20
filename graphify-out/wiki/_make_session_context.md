# _make_session_context

> 25 nodes

## Key Concepts

- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **asyncio** (11 connections)
- **_row_for_quest_instance()** (6 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_create_database_error()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_create_success()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_success()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_active_by_player_success()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_completed_by_player_success()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_accepts_uuid()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_not_found()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_active_by_player_empty()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_update_state_and_progress_no_op()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_update_state_and_progress_success()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test get_by_player_and_quest returns mapped instance when found.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test get_by_player_and_quest returns None when not found.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test get_by_player_and_quest accepts UUID for player_id.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test update_state_and_progress updates and commits.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test update_state_and_progress still calls procedure and commit when only…** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test list_active_by_player returns list of mapped active instances.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test list_active_by_player returns empty list when none.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test list_completed_by_player returns list of mapped completed instances.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Return context manager that yields mock_session for async with.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Build a procedure result row (mappings().first() return value) for…** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test create calls procedure, commits, and returns mapped instance.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test create raises DatabaseError on DB failure.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`

## Relationships

- [get_logger](get_logger.md) (15 shared connections)

## Source Files

- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 50 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*