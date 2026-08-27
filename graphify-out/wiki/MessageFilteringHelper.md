# MessageFilteringHelper

> 29 nodes

## Key Concepts

- **test_skill_service.py** (37 connections) — `server/tests/unit/game/test_skill_service.py`
- **asyncio** (23 connections)
- **test_get_player_skills_non_owner_returns_none()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_player_skills_owner_returns_list()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_skills_catalog_returns_list()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_skills_used_this_level_returns_repo_result()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_record_successful_skill_use_calls_repo()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_failure_does_not_record()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_success_records_use_and_returns_true()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_unknown_skill_returns_false()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_high_skill_gains_one()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_improvement_applied_when_roll_exceeds_value()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_no_skills_used_no_updates()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_previous_level_under_1_no_op()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_roll_under_current_no_change()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **Unit tests for SkillService (get_skills_catalog, set_player_skills,…** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_skills_catalog returns list of skill dicts.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_player_skills for owned player returns list of skill dicts.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_player_skills for another user's player returns None.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **record_successful_skill_use delegates to repo.record_use with correct args.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_skills_used_this_level returns distinct skill_ids from repo.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **run_improvement_rolls with new_level 1 does nothing (previous level 0).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **run_improvement_rolls when no skills used at previous level does not update.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When roll > current value, update_value called with new value (gain 1 or 1d10).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When current >= 90, successful improvement adds 1 (cap 99).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- *... and 4 more nodes in this community*

## Relationships

- [Appendices](Appendices.md) (11 shared connections)
- [Implementation Phases](Implementation_Phases.md) (11 shared connections)
- [main](main.md) (6 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 73 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*