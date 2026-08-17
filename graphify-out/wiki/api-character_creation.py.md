# api/character_creation.py

> 166 nodes

## Key Concepts

- **api/character_creation.py** (67 connections) — `server/api/character_creation.py`
- **SkillService** (38 connections) — `server/game/skill_service.py`
- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (24 connections) — `server/tests/unit/api/test_character_creation.py`
- **RollStatsRequest** (23 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (23 connections) — `server/api/character_creation.py`
- **ProfessionService** (21 connections) — `server/game/profession_service.py`
- **CreateCharacterRequest** (21 connections) — `server/schemas/players/player_requests.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- **asyncio** (14 connections)
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **RollStatsResponse** (12 connections) — `server/schemas/players/character_creation.py`
- **TestRollCharacterStats** (12 connections) — `server/tests/unit/api/test_character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **get_stats_generator()** (11 connections) — `server/dependencies.py`
- **players/character_creation.py** (11 connections) — `server/schemas/players/character_creation.py`
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- **get_profession_service()** (10 connections) — `server/dependencies.py`
- **CreateCharacterResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **Any** (9 connections)
- **TestCreateCharacterWithStats** (8 connections) — `server/tests/unit/api/test_character_creation.py`
- **_raise_roll_stats_error()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- *... and 141 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (32 shared connections)
- [User](User.md) (24 shared connections)
- [DatabaseError](DatabaseError.md) (13 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (13 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (12 shared connections)
- [PlayerService](PlayerService.md) (12 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (11 shared connections)
- [StatsGenerator](StatsGenerator.md) (9 shared connections)
- [test_dependencies.py](test_dependencies.py.md) (4 shared connections)
- [handle_skills_command](handle_skills_command.md) (3 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (3 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (3 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/dependencies.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 465 (96%)
- INFERRED: 18 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*