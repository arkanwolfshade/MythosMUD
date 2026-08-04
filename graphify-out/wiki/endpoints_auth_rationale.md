# endpoints auth rationale

> 126 nodes

## Key Concepts

- **SkillService** (37 connections) — `server/game/skill_service.py`
- **test_skill_service.py** (36 connections) — `server/tests/unit/game/test_skill_service.py`
- **Skill** (27 connections) — `server/models/skill.py`
- **skill_service.py** (21 connections) — `server/game/skill_service.py`
- **SkillUseLogRepository** (15 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **skill.py** (12 connections) — `server/models/skill.py`
- **test_skills_commands.py** (11 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **_occupation_slots_9()** (11 connections) — `server/tests/unit/game/test_skill_service.py`
- **Any** (10 connections)
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **UUID** (8 connections)
- **_personal_interest_4()** (8 connections) — `server/tests/unit/game/test_skill_service.py`
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **.__init__()** (5 connections) — `server/game/skill_service.py`
- **._validate_no_overlap()** (5 connections) — `server/game/skill_service.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **.get_player_skills()** (4 connections) — `server/game/skill_service.py`
- **.record_successful_skill_use()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_used_this_level()** (4 connections) — `server/game/skill_service.py`
- **.run_improvement_rolls()** (4 connections) — `server/game/skill_service.py`
- **.roll_skill_check()** (4 connections) — `server/game/skill_service.py`
- *... and 101 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (26 shared connections)
- [Player Stats](Player_Stats.md) (8 shared connections)
- [world models rationale](world_models_rationale.md) (7 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (6 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (5 shared connections)
- [npc threading rationale](npc_threading_rationale.md) (5 shared connections)
- [profession game service](profession_game_service.md) (4 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [npc population stats](npc_population_stats.md) (2 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (1 shared connections)

## Source Files

- `server/game/skill_service.py`
- `server/models/skill.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/tests/unit/api/test_skills.py`
- `server/tests/unit/commands/test_skills_commands.py`
- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 417 (96%)
- INFERRED: 19 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*