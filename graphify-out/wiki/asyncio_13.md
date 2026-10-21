# asyncio

> 21 nodes · cohesion 0.17

## Key Concepts

- **test_skill_service_graded.py** (16 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **_service()** (10 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **grade_d100()** (7 connections) — `server/game/skill_service.py`
- **asyncio** (6 connections)
- **test_roll_skill_check_shares_the_graded_rule_a_roll_of_one_always_succeeds()** (6 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **test_best_skill_check_grades_the_roll_and_records_only_successes()** (5 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **test_best_skill_check_ignores_skills_that_were_not_asked_for()** (4 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **test_best_skill_check_uses_the_higher_of_the_two_skills()** (4 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **test_grade_d100()** (4 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **_Row** (3 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **test_best_skill_check_defaults_to_the_players_current_level()** (3 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **test_best_skill_check_falls_back_to_level_one_when_the_player_is_missing()** (3 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **parametrize** (2 connections)
- **_Skill** (2 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **test_only_regular_hard_and_extreme_count_as_success()** (2 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **Grade a d100 roll against a skill value. Extreme is at most a fifth of the…** (1 connections) — `server/game/skill_service.py`
- **Unit tests for graded d100 skill checks (#833): SuccessLevel, grade_d100 and…** (1 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **Dodge 90 is not in the key list, so it neither helps the roll nor gets a use…** (1 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **roll_skill_check delegates to grade_d100, so 01 succeeds even against a skill…** (1 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **A SkillService over fakes; returns (service, record_use mock, get_player_by_id…** (1 connections) — `server/tests/unit/game/test_skill_service_graded.py`
- **A 40 fails on Intimidate (30) alone but is a Regular success on Fighting (55):…** (1 connections) — `server/tests/unit/game/test_skill_service_graded.py`

## Relationships

- [Reporter](Reporter.md) (7 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)

## Source Files

- `server/game/skill_service.py`
- `server/tests/unit/game/test_skill_service_graded.py`

## Audit Trail

- EXTRACTED: 44 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*