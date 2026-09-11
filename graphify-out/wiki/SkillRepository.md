# SkillRepository

> 90 nodes

## Key Concepts

- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **Skill** (26 connections) — `server/models/skill.py`
- **PlayerSkillRepository** (24 connections) — `server/persistence/repositories/player_skill_repository.py`
- **skill_service.py** (22 connections) — `server/game/skill_service.py`
- **player_skill_repository.py** (19 connections) — `server/persistence/repositories/player_skill_repository.py`
- **test_skill_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **PlayerSkill** (14 connections) — `server/models/player_skill.py`
- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **get_skills_catalog()** (12 connections) — `server/api/skills.py`
- **models/skill.py** (12 connections) — `server/models/skill.py`
- **test_player_skill_repository.py** (12 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **player_skill.py** (10 connections) — `server/models/player_skill.py`
- **_row_to_skill()** (9 connections) — `server/persistence/repositories/skill_repository.py`
- **asyncio** (8 connections)
- **.get_by_player_id()** (7 connections) — `server/persistence/repositories/player_skill_repository.py`
- **_row_to_player_skill_with_skill()** (6 connections) — `server/persistence/repositories/player_skill_repository.py`
- **.get_all_skills()** (6 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_id()** (6 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_key()** (6 connections) — `server/persistence/repositories/skill_repository.py`
- **asyncio** (6 connections)
- **.delete_for_player()** (5 connections) — `server/persistence/repositories/player_skill_repository.py`
- **.insert_many()** (5 connections) — `server/persistence/repositories/player_skill_repository.py`
- **.update_value()** (5 connections) — `server/persistence/repositories/player_skill_repository.py`
- **test_get_skills_catalog_unauthorized()** (5 connections) — `server/tests/unit/api/test_skills.py`
- **UUID** (5 connections)
- *... and 65 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (41 shared connections)
- [GameBundle](GameBundle.md) (18 shared connections)
- [Player](Player.md) (14 shared connections)
- [get_session_maker](get_session_maker.md) (8 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [test_skill_service.py](test_skill_service.py.md) (3 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [User](User.md) (3 shared connections)
- [fixture](fixture.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/api/skills.py`
- `server/game/skill_service.py`
- `server/models/player_skill.py`
- `server/models/skill.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/tests/unit/api/test_skills.py`
- `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_repository.py`

## Audit Trail

- EXTRACTED: 223 (86%)
- INFERRED: 35 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*