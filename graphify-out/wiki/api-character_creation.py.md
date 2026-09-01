# api/character_creation.py

> 165 nodes

## Key Concepts

- **api/character_creation.py** (67 connections) — `server/api/character_creation.py`
- **player_service.py** (49 connections) — `server/game/player_service.py`
- **PlayerRead** (47 connections) — `server/schemas/players/player.py`
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
- **TestRollCharacterStats** (12 connections) — `server/tests/unit/api/test_character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **players/character_creation.py** (11 connections) — `server/schemas/players/character_creation.py`
- **PlayerSearchService** (10 connections) — `server/game/player_search_service.py`
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- **get_profession_service()** (10 connections) — `server/dependencies.py`
- **CreateCharacterResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **player_search_service.py** (9 connections) — `server/game/player_search_service.py`
- **TestCreateCharacterWithStats** (8 connections) — `server/tests/unit/api/test_character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- *... and 140 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (43 shared connections)
- [players/__init__.py](players-__init__.py.md) (27 shared connections)
- [User](User.md) (24 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (16 shared connections)
- [Stats](Stats.md) (12 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (9 shared connections)
- [ValidationError](ValidationError.md) (9 shared connections)
- [test_player_schemas.py](test_player_schemas.py.md) (6 shared connections)
- [PlayerStateService](PlayerStateService.md) (5 shared connections)
- [SkillService](SkillService.md) (5 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (4 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/commands/admin_shutdown_command.py`
- `server/dependencies.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/profession_service.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 528 (98%)
- INFERRED: 11 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*