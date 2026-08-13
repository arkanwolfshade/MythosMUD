# api/character_creation.py

> 117 nodes

## Key Concepts

- **api/character_creation.py** (54 connections) — `server/api/character_creation.py`
- **SkillService** (37 connections) — `server/game/skill_service.py`
- **StatsGenerator** (34 connections) — `server/game/stats_generator.py`
- **RollStatsRequest** (22 connections) — `server/schemas/players/player_requests.py`
- **roll_character_stats()** (22 connections) — `server/api/character_creation.py`
- **CreateCharacterRequest** (21 connections) — `server/schemas/players/player_requests.py`
- **ProfessionService** (19 connections) — `server/game/profession_service.py`
- **create_character_with_stats()** (18 connections) — `server/api/character_creation.py`
- **_execute_create_character()** (15 connections) — `server/api/character_creation.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **validate_character_stats()** (14 connections) — `server/api/character_creation.py`
- **asyncio** (14 connections)
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **CreateCharacterResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **RollStatsResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **RolledStats** (10 connections) — `server/schemas/players/stat_values.py`
- **TestCreateCharacterWithStats** (10 connections) — `server/tests/unit/api/test_character_creation.py`
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- **Any** (10 connections)
- **players/character_creation.py** (10 connections) — `server/schemas/players/character_creation.py`
- **ValidateStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **TestValidateCharacterStats** (9 connections) — `server/tests/unit/api/test_character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (9 connections) — `server/api/character_creation.py`
- **StatSummary** (8 connections) — `server/schemas/players/character_creation.py`
- *... and 92 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (24 shared connections)
- [Stats](Stats.md) (22 shared connections)
- [User](User.md) (19 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (18 shared connections)
- [players/__init__.py](players-__init__.py.md) (18 shared connections)
- [PlayerService](PlayerService.md) (13 shared connections)
- [Any](Any.md) (13 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (7 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (7 shared connections)
- [PlayerRead](PlayerRead.md) (6 shared connections)
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (4 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (3 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/commands/admin_shutdown_command.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/game/stats_generator.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 388 (92%)
- INFERRED: 32 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*