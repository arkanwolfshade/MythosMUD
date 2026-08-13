# test_quest_instance_repository.py

> 63 nodes

## Key Concepts

- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **asyncio** (11 connections)
- **.create()** (10 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_start_by_trigger_then_abandon()** (10 connections) — `server/tests/integration/test_quest_flow.py`
- **test_quest_start_log_abandon_flow()** (10 connections) — `server/tests/integration/test_quest_flow.py`
- **.get_by_player_and_quest()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_row_to_quest_instance()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.update_state_and_progress()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_str_player_id()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **UUID** (7 connections)
- **_row_for_quest_instance()** (6 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **_make_shared_session_factory()** (5 connections) — `server/tests/integration/test_quest_flow.py`
- **test_create_success()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_success()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_active_by_player_success()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_completed_by_player_success()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **._fetch_created_quest_row()** (4 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **quest_instance_repository()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_create_database_error()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_accepts_uuid()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_not_found()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- *... and 38 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (18 shared connections)
- [log_and_raise](log_and_raise.md) (11 shared connections)
- [QuestService](QuestService.md) (9 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (2 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/quest_instance_repository.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 147 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*