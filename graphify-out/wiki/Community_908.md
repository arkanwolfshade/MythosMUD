# Community 908

> 17 nodes

## Key Concepts

- **asyncio** (23 connections)
- **test_get_player_skills_non_owner_returns_none()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_player_skills_owner_returns_list()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_skills_catalog_returns_list()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_skills_used_this_level_returns_repo_result()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_failure_does_not_record()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_high_skill_gains_one()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_improvement_applied_when_roll_exceeds_value()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_roll_under_current_no_change()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_skills_catalog returns list of skill dicts.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_player_skills for owned player returns list of skill dicts.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_player_skills for another user's player returns None.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_skills_used_this_level returns distinct skill_ids from repo.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When roll > current value, update_value called with new value (gain 1 or 1d10).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When current >= 90, successful improvement adds 1 (cap 99).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When roll <= current value, no update_value call.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When roll > skill value, record_use is not called and returns False.** (1 connections) — `server/tests/unit/game/test_skill_service.py`

## Relationships

- [Community 1116](Community_1116.md) (13 shared connections)
- [Community 1118](Community_1118.md) (5 shared connections)
- [Community 1117](Community_1117.md) (5 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*