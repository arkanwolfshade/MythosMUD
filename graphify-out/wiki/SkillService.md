# SkillService

> 162 nodes

## Key Concepts

- **SkillService** (38 connections) — `server/game/skill_service.py`
- **test_skill_service.py** (37 connections) — `server/tests/unit/game/test_skill_service.py`
- **Skill** (26 connections) — `server/models/skill.py`
- **PlayerSkillRepository** (24 connections) — `server/persistence/repositories/player_skill_repository.py`
- **asyncio** (23 connections)
- **skill_service.py** (21 connections) — `server/game/skill_service.py`
- **player_skill_repository.py** (20 connections) — `server/persistence/repositories/player_skill_repository.py`
- **._init_player_quest_layer()** (16 connections) — `server/container/bundles/game.py`
- **skills_commands.py** (16 connections) — `server/commands/skills_commands.py`
- **SkillUseLogRepository** (15 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **test_player_skill_repository.py** (13 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **handle_skills_command()** (12 connections) — `server/commands/skills_commands.py`
- **test_skills_commands.py** (12 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **_occupation_slots_9()** (11 connections) — `server/tests/unit/game/test_skill_service.py`
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **Any** (9 connections)
- **_get_container_services()** (8 connections) — `server/commands/skills_commands.py`
- **_personal_interest_4()** (8 connections) — `server/tests/unit/game/test_skill_service.py`
- **._init_quest_service()** (7 connections) — `server/container/bundles/game.py`
- **.get_by_player_id()** (7 connections) — `server/persistence/repositories/player_skill_repository.py`
- **UUID** (7 connections)
- **_resolve_player_id()** (6 connections) — `server/commands/skills_commands.py`
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- *... and 137 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (18 shared connections)
- [Player](Player.md) (14 shared connections)
- [log_and_raise](log_and_raise.md) (10 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (8 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (6 shared connections)
- [get_session_maker](get_session_maker.md) (5 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [persistence/repositories/__init__.py](persistence-repositories-__init__.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)

## Source Files

- `server/commands/skills_commands.py`
- `server/container/bundles/game.py`
- `server/game/skill_service.py`
- `server/models/skill.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/tests/unit/commands/test_skills_commands.py`
- `server/tests/unit/game/test_skill_service.py`
- `server/tests/unit/persistence/repositories/test_player_skill_repository.py`

## Audit Trail

- EXTRACTED: 363 (92%)
- INFERRED: 33 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*