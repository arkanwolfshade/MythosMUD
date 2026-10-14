# asyncio

> 17 nodes

## Key Concepts

- **asyncio** (23 connections)
- **test_get_player_skills_non_owner_returns_none()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_player_skills_owner_returns_list()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_skills_catalog_returns_list()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_skills_used_this_level_returns_repo_result()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_record_successful_skill_use_calls_repo()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_failure_does_not_record()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_unknown_skill_returns_false()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_improvement_applied_when_roll_exceeds_value()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_skills_catalog returns list of skill dicts.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_player_skills for owned player returns list of skill dicts.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_player_skills for another user's player returns None.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **record_successful_skill_use delegates to repo.record_use with correct args.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_skills_used_this_level returns distinct skill_ids from repo.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When roll > current value, update_value called with new value (gain 1 or 1d10).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **roll_skill_check when player has no value for skill_id returns False.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When roll > skill value, record_use is not called and returns False.** (1 connections) — `server/tests/unit/game/test_skill_service.py`

## Relationships

- [test_skill_service.py](test_skill_service.py.md) (13 shared connections)
- [_personal_interest_4](_personal_interest_4.md) (5 shared connections)
- [_occupation_slots_9](_occupation_slots_9.md) (5 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*