# test skill service

> 16 nodes

## Key Concepts

- **test_skill_service.py** (36 connections) — `server/tests/unit/game/test_skill_service.py`
- **catalog_with_own_language_and_mythos()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_skills_catalog_returns_list()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_record_successful_skill_use_calls_repo()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_previous_level_under_1_no_op()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_unknown_skill_returns_false()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_failure_does_not_record()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **Unit tests for SkillService (get_skills_catalog, set_player_skills, get_player_s** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Minimal catalog: accounting, library_use, own_language, cthulhu_mythos (for cove** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock AsyncPersistenceLayer (get_profession_by_id, get_player_by_id).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_skills_catalog returns list of skill dicts.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **record_successful_skill_use delegates to repo.record_use with correct args.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **run_improvement_rolls with new_level 1 does nothing (previous level 0).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **roll_skill_check when player has no value for skill_id returns False.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When roll > skill value, record_use is not called and returns False.** (1 connections) — `server/tests/unit/game/test_skill_service.py`

## Relationships

- [occupation slots 9()](occupation_slots_9%28%29.md) (6 shared connections)
- [personal interest 4()](personal_interest_4%28%29.md) (6 shared connections)
- [get skill repository()](get_skill_repository%28%29.md) (4 shared connections)
- [Base](Base.md) (1 shared connections)
- [mock player skill repo()](mock_player_skill_repo%28%29.md) (1 shared connections)
- [mock skill repo()](mock_skill_repo%28%29.md) (1 shared connections)
- [mock skill use log repo()](mock_skill_use_log_repo%28%29.md) (1 shared connections)
- [SkillService with mocks.](SkillService_with_mocks.md) (1 shared connections)
- [get player skills for another](get_player_skills_for_another.md) (1 shared connections)
- [get player skills for owned](get_player_skills_for_owned.md) (1 shared connections)
- [get skills used this level](get_skills_used_this_level.md) (1 shared connections)
- [When roll <= skill value,](When_roll__%3D_skill_value%2C.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*