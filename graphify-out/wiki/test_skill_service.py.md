# test_skill_service.py

> 12 nodes

## Key Concepts

- **test_skill_service.py** (36 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_success_records_use_and_returns_true()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_high_skill_gains_one()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_no_skills_used_no_updates()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_previous_level_under_1_no_op()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_roll_under_current_no_change()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **Unit tests for SkillService (get_skills_catalog, set_player_skills,…** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **run_improvement_rolls with new_level 1 does nothing (previous level 0).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **run_improvement_rolls when no skills used at previous level does not update.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When current >= 90, successful improvement adds 1 (cap 99).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When roll <= current value, no update_value call.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When roll <= skill value, record_use is called and returns True.** (1 connections) — `server/tests/unit/game/test_skill_service.py`

## Relationships

- [asyncio](asyncio.md) (13 shared connections)
- [fixture](fixture.md) (6 shared connections)
- [_occupation_slots_9](_occupation_slots_9.md) (6 shared connections)
- [_personal_interest_4](_personal_interest_4.md) (6 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*