# test_skill_service.py

> 39 nodes

## Key Concepts

- **test_skill_service.py** (37 connections) — `server/tests/unit/game/test_skill_service.py`
- **asyncio** (23 connections)
- **test_set_player_skills_cthulhu_mythos_in_personal_rejected()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_duplicate_personal_skill_ids_raises()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_overlap_occupation_and_personal_raises()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_personal_interest_not_four_raises()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_wrong_occupation_count_raises()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
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
- **Personal interest with Cthulhu Mythos raises ValueError.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **occupation_slots not length 9 raises ValueError.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **personal_interest must have exactly 4 entries.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- *... and 14 more nodes in this community*

## Relationships

- [_occupation_slots_9](_occupation_slots_9.md) (17 shared connections)
- [fixture](fixture.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [SkillService](SkillService.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 83 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*