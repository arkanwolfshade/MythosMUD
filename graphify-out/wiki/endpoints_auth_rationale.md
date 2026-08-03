# endpoints auth rationale

> 105 nodes

## Key Concepts

- **SkillService** (37 connections) — `server/game/skill_service.py`
- **test_skill_service.py** (36 connections) — `server/tests/unit/game/test_skill_service.py`
- **skill_service.py** (21 connections) — `server/game/skill_service.py`
- **test_skills_commands.py** (11 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **_occupation_slots_9()** (11 connections) — `server/tests/unit/game/test_skill_service.py`
- **Any** (10 connections)
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **UUID** (8 connections)
- **_personal_interest_4()** (8 connections) — `server/tests/unit/game/test_skill_service.py`
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **._validate_no_overlap()** (5 connections) — `server/game/skill_service.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **.get_player_skills()** (4 connections) — `server/game/skill_service.py`
- **.record_successful_skill_use()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_used_this_level()** (4 connections) — `server/game/skill_service.py`
- **.run_improvement_rolls()** (4 connections) — `server/game/skill_service.py`
- **.roll_skill_check()** (4 connections) — `server/game/skill_service.py`
- **skill_service()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_valid_creates_rows()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_own_language_not_allocated_equals_edu()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_cthulhu_mythos_in_occupation_rejected()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_wrong_occupation_values_raises()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- *... and 80 more nodes in this community*

## Relationships

- [world models rationale](world_models_rationale.md) (10 shared connections)
- [Database Config](Database_Config.md) (10 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [npc threading rationale](npc_threading_rationale.md) (5 shared connections)
- [profession game service](profession_game_service.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [holiday service services](holiday_service_services.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/game/skill_service.py`
- `server/tests/unit/commands/test_skills_commands.py`
- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 328 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*