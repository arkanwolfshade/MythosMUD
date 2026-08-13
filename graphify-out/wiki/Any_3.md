# Any

> 28 nodes

## Key Concepts

- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **Any** (9 connections)
- **UUID** (7 connections)
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **._validate_no_overlap()** (5 connections) — `server/game/skill_service.py`
- **.get_player_skills()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_used_this_level()** (4 connections) — `server/game/skill_service.py`
- **.record_successful_skill_use()** (4 connections) — `server/game/skill_service.py`
- **.roll_skill_check()** (4 connections) — `server/game/skill_service.py`
- **.run_improvement_rolls()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_catalog()** (3 connections) — `server/game/skill_service.py`
- **Raise ValueError if any skill_id appears in both occupation and personal…** (1 connections) — `server/game/skill_service.py`
- **Build skill_key -> total modifier from profession skill_modifiers (supports…** (1 connections) — `server/game/skill_service.py`
- **Compute final skill_id -> value: base + profession mod, then occupation…** (1 connections) — `server/game/skill_service.py`
- **Validate skills allocation without persisting. Raises ValueError if invalid.…** (1 connections) — `server/game/skill_service.py`
- **Set all skills for a character at creation. Validates occupation_slots (9…** (1 connections) — `server/game/skill_service.py`
- **Return list of {skill_id, skill_key, skill_name, value} for the player. If the…** (1 connections) — `server/game/skill_service.py`
- **Record one successful use of a skill at the character's current level. Used for…** (1 connections) — `server/game/skill_service.py`
- **Return distinct skill_ids that the player successfully used at the given level.…** (1 connections) — `server/game/skill_service.py`
- **For each skill the player used during the previous level, roll d100. If roll >…** (1 connections) — `server/game/skill_service.py`
- **Roll d100 against the character's skill value; on success record use and return…** (1 connections) — `server/game/skill_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [api/character_creation.py](api-character_creation.py.md) (13 shared connections)
- [log_and_raise](log_and_raise.md) (4 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/game/skill_service.py`

## Audit Trail

- EXTRACTED: 56 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*