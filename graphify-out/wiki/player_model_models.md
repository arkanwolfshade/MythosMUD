# player model models

> 45 nodes

## Key Concepts

- **SkillService** (35 connections) — `server/game/skill_service.py`
- **skill_service.py** (20 connections) — `server/game/skill_service.py`
- **SkillRepository** (19 connections) — `server/persistence/repositories/skill_repository.py`
- **PlayerSkillRepository** (17 connections) — `server/persistence/repositories/player_skill_repository.py`
- **SkillUseLogRepository** (13 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **Any** (10 connections)
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **UUID** (8 connections)
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
- **get_skill_repository()** (3 connections) — `server/dependencies.py`
- **.get_skills_catalog()** (3 connections) — `server/game/skill_service.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/skill_repository.py`
- **.__init__()** (2 connections) — `server/persistence/repositories/player_skill_repository.py`
- **.__init__()** (2 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- *... and 20 more nodes in this community*

## Relationships

- [npc populate databases](npc_populate_databases.md) (13 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (12 shared connections)
- [NATS Messaging](NATS_Messaging.md) (11 shared connections)
- [world models rationale](world_models_rationale.md) (10 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (5 shared connections)
- [Player Stats](Player_Stats.md) (5 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (5 shared connections)
- [character creation validate](character_creation_validate.md) (3 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (3 shared connections)
- [skill service game](skill_service_game.md) (3 shared connections)
- [dialogue definitions admin](dialogue_definitions_admin.md) (3 shared connections)
- [auth users rationale](auth_users_rationale.md) (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/game/skill_service.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`

## Audit Trail

- EXTRACTED: 202 (91%)
- INFERRED: 20 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*