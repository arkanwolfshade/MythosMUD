# Community 1116

> 12 nodes

## Key Concepts

- **test_skill_service.py** (36 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_record_successful_skill_use_calls_repo()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_success_records_use_and_returns_true()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_unknown_skill_returns_false()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_no_skills_used_no_updates()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_previous_level_under_1_no_op()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **Unit tests for SkillService (get_skills_catalog, set_player_skills,…** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **record_successful_skill_use delegates to repo.record_use with correct args.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **run_improvement_rolls with new_level 1 does nothing (previous level 0).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **run_improvement_rolls when no skills used at previous level does not update.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **roll_skill_check when player has no value for skill_id returns False.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When roll <= skill value, record_use is called and returns True.** (1 connections) — `server/tests/unit/game/test_skill_service.py`

## Relationships

- [Community 908](Community_908.md) (13 shared connections)
- [Community 1077](Community_1077.md) (6 shared connections)
- [Community 1117](Community_1117.md) (6 shared connections)
- [Community 1118](Community_1118.md) (6 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Character Creation & Professions](Character_Creation_&_Professions.md) (1 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*