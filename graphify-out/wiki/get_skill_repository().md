# get skill repository()

> 52 nodes

## Key Concepts

- **SkillService** (35 connections) — `server/game/skill_service.py`
- **Skill** (27 connections) — `server/models/skill.py`
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
- **sample_skills()** (3 connections) — `server/tests/unit/api/test_skills.py`
- *... and 27 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (35 shared connections)
- [Any](Any.md) (12 shared connections)
- [. init ()](_init_%28%29.md) (7 shared connections)
- [Connection Manager](Connection_Manager.md) (7 shared connections)
- [Base](Base.md) (5 shared connections)
- [character creation](character_creation.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [test skill service](test_skill_service.md) (4 shared connections)
- [skills commands](skills_commands.md) (3 shared connections)
- [SkillService with mocks.](SkillService_with_mocks.md) (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/game/skill_service.py`
- `server/models/skill.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 233 (90%)
- INFERRED: 25 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*