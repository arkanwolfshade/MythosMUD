# UUID

> 9 nodes

## Key Concepts

- **UUID** (7 connections)
- **.get_skills_used_this_level()** (4 connections) — `server/game/skill_service.py`
- **.record_successful_skill_use()** (4 connections) — `server/game/skill_service.py`
- **.roll_skill_check()** (4 connections) — `server/game/skill_service.py`
- **.run_improvement_rolls()** (4 connections) — `server/game/skill_service.py`
- **Record one successful use of a skill at the character's current level. Used for…** (1 connections) — `server/game/skill_service.py`
- **Return distinct skill_ids that the player successfully used at the given level.…** (1 connections) — `server/game/skill_service.py`
- **For each skill the player used during the previous level, roll d100. If roll >…** (1 connections) — `server/game/skill_service.py`
- **Roll d100 against the character's skill value; on success record use and return…** (1 connections) — `server/game/skill_service.py`

## Relationships

- [SkillService](SkillService.md) (6 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/game/skill_service.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*