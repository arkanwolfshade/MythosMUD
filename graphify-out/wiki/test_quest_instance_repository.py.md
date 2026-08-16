# test_quest_instance_repository.py

> 59 nodes

## Key Concepts

- **test_quest_instance_repository.py** (23 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **quest_instance_repository.py** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **asyncio** (11 connections)
- **.create()** (10 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.get_by_player_and_quest()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_row_to_quest_instance()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.update_state_and_progress()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_str_player_id()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **UUID** (7 connections)
- **_row_for_quest_instance()** (6 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_create_database_error()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_create_success()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_success()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_active_by_player_success()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_completed_by_player_database_error()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_list_completed_by_player_success()** (5 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **._fetch_created_quest_row()** (4 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **mock_quest_instance()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **quest_instance_repository()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_get_by_player_and_quest_accepts_uuid()** (4 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- *... and 34 more nodes in this community*

## Relationships

- [Player](Player.md) (9 shared connections)
- [log_and_raise](log_and_raise.md) (8 shared connections)
- [QuestService](QuestService.md) (7 shared connections)
- [get_session_maker](get_session_maker.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [persistence/repositories/__init__.py](persistence-repositories-__init__.py.md) (2 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [SkillService](SkillService.md) (1 shared connections)
- [database.py](database.py.md) (1 shared connections)

## Source Files

- `server/models/quest.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 150 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*