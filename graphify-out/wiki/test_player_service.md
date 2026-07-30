# test player service

> 60 nodes

## Key Concepts

- **test_skill_service.py** (36 connections) — `server/tests/unit/game/test_skill_service.py`
- **_occupation_slots_9()** (11 connections) — `server/tests/unit/game/test_skill_service.py`
- **_personal_interest_4()** (8 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_valid_creates_rows()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_own_language_not_allocated_equals_edu()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_cthulhu_mythos_in_occupation_rejected()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_wrong_occupation_values_raises()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_duplicate_occupation_skill_ids_raises()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_cthulhu_mythos_in_personal_rejected()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_wrong_occupation_count_raises()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_personal_interest_not_four_raises()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_duplicate_personal_skill_ids_raises()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_overlap_occupation_and_personal_raises()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_skill_repo()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_player_skill_repo()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_skill_use_log_repo()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_skills_catalog_returns_list()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_player_skills_owner_returns_list()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_player_skills_non_owner_returns_none()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_record_successful_skill_use_calls_repo()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_skills_used_this_level_returns_repo_result()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_previous_level_under_1_no_op()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_no_skills_used_no_updates()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_improvement_applied_when_roll_exceeds_value()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- *... and 35 more nodes in this community*

## Relationships

- [emit close container event()](emit_close_container_event%28%29.md) (2 shared connections)
- [test quest definition repository](test_quest_definition_repository.md) (2 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [AppState](AppState.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 154 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*