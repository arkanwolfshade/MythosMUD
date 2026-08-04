# skill service game

> 11 nodes

## Key Concepts

- **UUID** (8 connections)
- **.get_player_skills()** (4 connections) — `server/game/skill_service.py`
- **.record_successful_skill_use()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_used_this_level()** (4 connections) — `server/game/skill_service.py`
- **.run_improvement_rolls()** (4 connections) — `server/game/skill_service.py`
- **.roll_skill_check()** (4 connections) — `server/game/skill_service.py`
- **Return list of {skill_id, skill_key, skill_name, value} for the player.** (1 connections) — `server/game/skill_service.py`
- **Record one successful use of a skill at the character's current level.** (1 connections) — `server/game/skill_service.py`
- **Return distinct skill_ids that the player successfully used at the given level.** (1 connections) — `server/game/skill_service.py`
- **For each skill the player used during the previous level, roll d100.          If** (1 connections) — `server/game/skill_service.py`
- **Roll d100 against the character's skill value; on success record use and return** (1 connections) — `server/game/skill_service.py`

## Relationships

- [status game spell](status_game_spell.md) (7 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/game/skill_service.py`

## Audit Trail

- EXTRACTED: 32 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*