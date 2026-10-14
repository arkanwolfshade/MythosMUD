# .set_player_skills

> 33 nodes

## Key Concepts

- **.set_player_skills()** (10 connections) — `server/game/skill_service.py`
- **Any** (9 connections)
- **UUID** (8 connections)
- **grade_d100()** (7 connections) — `server/game/skill_service.py`
- **._validate_occupation_slots()** (7 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (7 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (7 connections) — `server/game/skill_service.py`
- **.roll_best_skill_check()** (6 connections) — `server/game/skill_service.py`
- **._validate_no_overlap()** (6 connections) — `server/game/skill_service.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **.record_successful_skill_use()** (5 connections) — `server/game/skill_service.py`
- **.roll_skill_check()** (5 connections) — `server/game/skill_service.py`
- **.get_player_skills()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_used_this_level()** (4 connections) — `server/game/skill_service.py`
- **.run_improvement_rolls()** (4 connections) — `server/game/skill_service.py`
- **Skill** (4 connections)
- **.get_skills_catalog()** (3 connections) — `server/game/skill_service.py`
- **Raise ValueError if occupation_slots are not exactly one 70, two 60, three 50,…** (1 connections) — `server/game/skill_service.py`
- **Require exactly 4 skill_ids; Cthulhu Mythos not allowed; all skill_ids unique.** (1 connections) — `server/game/skill_service.py`
- **Raise ValueError if any skill_id appears in both occupation and personal…** (1 connections) — `server/game/skill_service.py`
- **Build skill_key -> total modifier from profession skill_modifiers (supports…** (1 connections) — `server/game/skill_service.py`
- **Compute final skill_id -> value: base + profession mod, then occupation…** (1 connections) — `server/game/skill_service.py`
- **Validate skills allocation without persisting. Raises ValueError if invalid.…** (1 connections) — `server/game/skill_service.py`
- **Set all skills for a character at creation. Validates occupation_slots (9…** (1 connections) — `server/game/skill_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (14 shared connections)
- [ValueError](ValueError.md) (5 shared connections)
- [test_skill_service_graded.py](test_skill_service_graded.py.md) (2 shared connections)
- [SuccessLevel](SuccessLevel.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/game/skill_service.py`

## Audit Trail

- EXTRACTED: 68 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*