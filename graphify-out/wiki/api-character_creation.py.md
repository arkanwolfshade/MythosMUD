# api/character_creation.py

> 249 nodes

## Key Concepts

- **api/character_creation.py** (67 connections) — `server/api/character_creation.py`
- **RateLimitError** (52 connections) — `server/exceptions.py`
- **players/__init__.py** (48 connections) — `server/schemas/players/__init__.py`
- **PlayerRead** (46 connections) — `server/schemas/players/player.py`
- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (24 connections) — `server/tests/unit/api/test_character_creation.py`
- **RollStatsRequest** (23 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (23 connections) — `server/api/character_creation.py`
- **test_player_schemas.py** (23 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **ProfessionService** (21 connections) — `server/game/profession_service.py`
- **CreateCharacterRequest** (21 connections) — `server/schemas/players/player_requests.py`
- **players/player.py** (21 connections) — `server/schemas/players/player.py`
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
- **PlayerBase** (10 connections) — `server/schemas/players/player.py`
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- **CreateCharacterResponse** (9 connections) — `server/schemas/players/character_creation.py`
- *... and 224 more nodes in this community*

## Relationships

- [User](User.md) (52 shared connections)
- [get_logger](get_logger.md) (32 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (27 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (26 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (22 shared connections)
- [Stats](Stats.md) (16 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (13 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (12 shared connections)
- [ErrorType](ErrorType.md) (11 shared connections)
- [ValidationError](ValidationError.md) (11 shared connections)
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (8 shared connections)
- [MythosMUDError](MythosMUDError.md) (7 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/character_creation.py`
- `server/commands/admin_shutdown_command.py`
- `server/exceptions.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/profession_service.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/profession.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 696 (96%)
- INFERRED: 31 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*