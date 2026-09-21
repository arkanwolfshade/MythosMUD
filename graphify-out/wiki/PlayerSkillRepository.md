# PlayerSkillRepository

> 44 nodes

## Key Concepts

- **PlayerSkillRepository** (24 connections) — `server/persistence/repositories/player_skill_repository.py`
- **player_skill_repository.py** (19 connections) — `server/persistence/repositories/player_skill_repository.py`
- **SkillUseLogRepository** (15 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **skill_use_log_repository.py** (14 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **test_player_skill_repository.py** (12 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **test_skill_use_log_repository.py** (10 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **.get_by_player_id()** (7 connections) — `server/persistence/repositories/player_skill_repository.py`
- **asyncio** (6 connections)
- **.__init__()** (5 connections) — `server/game/skill_service.py`
- **.delete_for_player()** (5 connections) — `server/persistence/repositories/player_skill_repository.py`
- **.insert_many()** (5 connections) — `server/persistence/repositories/player_skill_repository.py`
- **.update_value()** (5 connections) — `server/persistence/repositories/player_skill_repository.py`
- **.get_skill_ids_used_at_level()** (5 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **.record_use()** (5 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **UUID** (5 connections)
- **test_delete_for_player_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **test_delete_for_player_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **test_get_by_player_id_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **test_insert_many_empty()** (3 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **test_insert_many_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **test_update_value_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **_mock_session()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **test_get_skill_ids_used_at_level()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- *... and 19 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (16 shared connections)
- [SkillRepository](SkillRepository.md) (13 shared connections)
- [get_session_maker](get_session_maker.md) (8 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (6 shared connections)
- [repositories/__init__.py](repositories-__init__.py.md) (4 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (3 shared connections)
- [item_catalog_repository.py](item_catalog_repository.py.md) (2 shared connections)
- [bundles/game.py](bundles-game.py.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)

## Source Files

- `server/game/skill_service.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`

## Audit Trail

- EXTRACTED: 117 (88%)
- INFERRED: 16 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*