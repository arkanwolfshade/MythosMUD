# endpoints auth rationale

> 38 nodes

## Key Concepts

- **test_skill_service.py** (36 connections) — `server/tests/unit/game/test_skill_service.py`
- **catalog_with_own_language_and_mythos()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
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
- **test_run_improvement_rolls_high_skill_gains_one()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_roll_under_current_no_change()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_unknown_skill_returns_false()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_success_records_use_and_returns_true()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_failure_does_not_record()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **Unit tests for SkillService (get_skills_catalog, set_player_skills, get_player_s** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Minimal catalog: accounting, library_use, own_language, cthulhu_mythos (for cove** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock SkillRepository returning catalog.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock PlayerSkillRepository.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock AsyncPersistenceLayer (get_profession_by_id, get_player_by_id).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock SkillUseLogRepository for use logging and improvement (plan 10.4).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- *... and 13 more nodes in this community*

## Relationships

- [command parser rationale](command_parser_rationale.md) (12 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (4 shared connections)
- [zone configuration npc](zone_configuration_npc.md) (1 shared connections)
- [npc threading rationale](npc_threading_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 92 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*