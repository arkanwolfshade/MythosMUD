# Server Game (9)

> 87 nodes

## Key Concepts

- **SkillService** (32 connections) — `server/game/skill_service.py`
- **Skill** (27 connections) — `server/models/skill.py`
- **skill_service.py** (20 connections) — `server/game/skill_service.py`
- **SkillRepository** (16 connections) — `server/persistence/repositories/skill_repository.py`
- **PlayerSkillRepository** (14 connections) — `server/persistence/repositories/player_skill_repository.py`
- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **get_skills_catalog()** (11 connections) — `server/api/skills.py`
- **Any** (10 connections)
- **SkillUseLogRepository** (10 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **UUID** (8 connections)
- **skill.py** (8 connections) — `server/schemas/players/skill.py`
- **_row_to_skill()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_all_skills()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_id()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_key()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- **SkillListResponse** (7 connections) — `server/schemas/players/skill.py`
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **.__init__()** (5 connections) — `server/game/skill_service.py`
- **._validate_no_overlap()** (5 connections) — `server/game/skill_service.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **SkillData** (5 connections) — `server/schemas/players/skill.py`
- *... and 62 more nodes in this community*

## Relationships

- [Server Admin](Server_Admin.md) (21 shared connections)
- [Server Persistence](Server_Persistence.md) (12 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (8 shared connections)
- [Server Commands](Server_Commands.md) (8 shared connections)
- [Server Models (17)](Server_Models_%2817%29.md) (7 shared connections)
- [Server Api](Server_Api.md) (6 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (5 shared connections)
- [Server Persistence (3)](Server_Persistence_%283%29.md) (5 shared connections)
- [Server Api (4)](Server_Api_%284%29.md) (4 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (4 shared connections)
- [Server Game (36)](Server_Game_%2836%29.md) (4 shared connections)
- [Server Utils (6)](Server_Utils_%286%29.md) (1 shared connections)

## Source Files

- `server/api/skills.py`
- `server/dependencies.py`
- `server/game/skill_service.py`
- `server/models/skill.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/schemas/players/skill.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 339 (92%)
- INFERRED: 28 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*