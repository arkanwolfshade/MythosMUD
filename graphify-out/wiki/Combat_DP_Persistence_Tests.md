# Combat DP Persistence Tests

> 22 nodes · cohesion 0.10

## Key Concepts

- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **_row_for_quest_instance()** (6 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_create_success()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_success()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_active_by_player_success()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_completed_by_player_success()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_accepts_uuid()** (3 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_not_found()** (3 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_active_by_player_empty()** (3 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_update_state_and_progress_no_op()** (3 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_update_state_and_progress_success()** (3 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test get_by_player_and_quest returns mapped instance when found.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test get_by_player_and_quest returns None when not found.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test get_by_player_and_quest accepts UUID for player_id.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test update_state_and_progress updates and commits.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test update_state_and_progress still calls procedure and commit when only instan** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test list_active_by_player returns list of mapped active instances.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test list_active_by_player returns empty list when none.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test list_completed_by_player returns list of mapped completed instances.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Return context manager that yields mock_session for async with.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Build a procedure result row (mappings().first() return value) for QuestInstance** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **Test create calls procedure, commits, and returns mapped instance.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`

## Relationships

- [Realtime Connection Impl](Realtime_Connection_Impl.md) (13 shared connections)

## Source Files

- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*