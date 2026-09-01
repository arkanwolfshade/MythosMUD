# SkillService

> 56 nodes

## Key Concepts

- **SkillService** (38 connections) — `server/game/skill_service.py`
- **skills_commands.py** (16 connections) — `server/commands/skills_commands.py`
- **handle_skills_command()** (12 connections) — `server/commands/skills_commands.py`
- **test_skills_commands.py** (12 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **Any** (9 connections)
- **_get_container_services()** (8 connections) — `server/commands/skills_commands.py`
- **UUID** (7 connections)
- **_resolve_player_id()** (6 connections) — `server/commands/skills_commands.py`
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **_format_skills_output()** (5 connections) — `server/commands/skills_commands.py`
- **_resolve_user_id()** (5 connections) — `server/commands/skills_commands.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **._validate_no_overlap()** (5 connections) — `server/game/skill_service.py`
- **skill_service()** (5 connections) — `server/tests/unit/game/test_skill_service.py`
- **Any** (5 connections)
- **.get_player_skills()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_used_this_level()** (4 connections) — `server/game/skill_service.py`
- **.record_successful_skill_use()** (4 connections) — `server/game/skill_service.py`
- **.roll_skill_check()** (4 connections) — `server/game/skill_service.py`
- **.run_improvement_rolls()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_catalog()** (3 connections) — `server/game/skill_service.py`
- *... and 31 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (17 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (5 shared connections)
- [test_skill_service.py](test_skill_service.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/skills_commands.py`
- `server/game/skill_service.py`
- `server/tests/unit/commands/test_skills_commands.py`
- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 127 (93%)
- INFERRED: 10 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*