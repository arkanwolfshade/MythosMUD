# api/character_creation.py

> 159 nodes

## Key Concepts

- **api/character_creation.py** (67 connections) — `server/api/character_creation.py`
- **PlayerRead** (46 connections) — `server/schemas/players/player.py`
- **SkillService** (38 connections) — `server/game/skill_service.py`
- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (24 connections) — `server/tests/unit/api/test_character_creation.py`
- **RollStatsRequest** (23 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (23 connections) — `server/api/character_creation.py`
- **ProfessionService** (21 connections) — `server/game/profession_service.py`
- **CreateCharacterRequest** (21 connections) — `server/schemas/players/player_requests.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **asyncio** (14 connections)
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **RollStatsResponse** (12 connections) — `server/schemas/players/character_creation.py`
- **TestRollCharacterStats** (12 connections) — `server/tests/unit/api/test_character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **get_stats_generator()** (11 connections) — `server/dependencies.py`
- **players/character_creation.py** (11 connections) — `server/schemas/players/character_creation.py`
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- **CreateCharacterResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **TestCreateCharacterWithStats** (8 connections) — `server/tests/unit/api/test_character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_prepare_create_character_request()** (8 connections) — `server/api/character_creation.py`
- *... and 134 more nodes in this community*

## Relationships

- [User](User.md) (27 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (27 shared connections)
- [players/__init__.py](players-__init__.py.md) (20 shared connections)
- [PlayerService](PlayerService.md) (19 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (16 shared connections)
- [Stats](Stats.md) (16 shared connections)
- [Any](Any.md) (13 shared connections)
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (11 shared connections)
- [DatabaseError](DatabaseError.md) (9 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/commands/admin_shutdown_command.py`
- `server/dependencies.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 501 (97%)
- INFERRED: 17 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*