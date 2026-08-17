# PlayerSkillRepository

> 23 nodes

## Key Concepts

- **PlayerSkillRepository** (24 connections) — `server/persistence/repositories/player_skill_repository.py`
- **test_player_skill_repository.py** (13 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **.get_by_player_id()** (7 connections) — `server/persistence/repositories/player_skill_repository.py`
- **asyncio** (6 connections)
- **.delete_for_player()** (5 connections) — `server/persistence/repositories/player_skill_repository.py`
- **.insert_many()** (5 connections) — `server/persistence/repositories/player_skill_repository.py`
- **.update_value()** (5 connections) — `server/persistence/repositories/player_skill_repository.py`
- **UUID** (5 connections)
- **test_delete_for_player_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **test_delete_for_player_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **test_get_by_player_id_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **test_insert_many_empty()** (3 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **test_insert_many_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **test_update_value_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **.__init__()** (2 connections) — `server/persistence/repositories/player_skill_repository.py`
- **fixture** (1 connections)
- **Get all PlayerSkill rows for the player with skill loaded (join). Returns list…** (1 connections) — `server/persistence/repositories/player_skill_repository.py`
- **Update a single player_skill row (e.g. after improvement roll). Clamps value…** (1 connections) — `server/persistence/repositories/player_skill_repository.py`
- **Repository for player_skills table. Used by SkillService for set_player_skills…** (1 connections) — `server/persistence/repositories/player_skill_repository.py`
- **Delete all player_skills for the given player_id.** (1 connections) — `server/persistence/repositories/player_skill_repository.py`
- **Insert multiple (skill_id, value) rows for one player. skill_values: list of…** (1 connections) — `server/persistence/repositories/player_skill_repository.py`
- **Unit tests for PlayerSkillRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`

## Relationships

- [get_session_maker](get_session_maker.md) (10 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [log_and_raise](log_and_raise.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [._init_player_quest_layer](_init_player_quest_layer.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [SkillUseLogRepository](SkillUseLogRepository.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_player_skill_repository.py`

## Audit Trail

- EXTRACTED: 52 (81%)
- INFERRED: 12 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*