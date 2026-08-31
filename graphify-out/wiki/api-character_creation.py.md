# api/character_creation.py

> 129 nodes

## Key Concepts

- **api/character_creation.py** (67 connections) — `server/api/character_creation.py`
- **SkillService** (38 connections) — `server/game/skill_service.py`
- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **CreateCharacterRequest** (25 connections) — `server/schemas/players/player_requests.py`
- **test_character_creation.py** (24 connections) — `server/tests/unit/api/test_character_creation.py`
- **RollStatsRequest** (23 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (23 connections) — `server/api/character_creation.py`
- **ProfessionService** (21 connections) — `server/game/profession_service.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- **asyncio** (14 connections)
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **RollStatsResponse** (12 connections) — `server/schemas/players/character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **players/character_creation.py** (11 connections) — `server/schemas/players/character_creation.py`
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- **get_profession_service()** (10 connections) — `server/dependencies.py`
- **CreateCharacterResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **TestCreateCharacterWithStats** (8 connections) — `server/tests/unit/api/test_character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_prepare_create_character_request()** (8 connections) — `server/api/character_creation.py`
- **_raise_roll_stats_error()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_with_class()** (8 connections) — `server/api/character_creation.py`
- *... and 104 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (62 shared connections)
- [players/__init__.py](players-__init__.py.md) (23 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [pytest.md](pytest.md.md) (16 shared connections)
- [Any](Any.md) (13 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (12 shared connections)
- [PlayerService](PlayerService.md) (12 shared connections)
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (7 shared connections)
- [skills_commands.py](skills_commands.py.md) (4 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (3 shared connections)
- [BaseCommand](BaseCommand.md) (3 shared connections)
- [test_profession_service.py](test_profession_service.py.md) (2 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/commands/admin_shutdown_command.py`
- `server/dependencies.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 426 (97%)
- INFERRED: 14 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*