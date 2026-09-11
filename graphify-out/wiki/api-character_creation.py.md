# api/character_creation.py

> 181 nodes

## Key Concepts

- **api/character_creation.py** (66 connections) — `server/api/character_creation.py`
- **error_types.py** (35 connections) — `server/error_types.py`
- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **CreateCharacterRequest** (25 connections) — `server/schemas/players/player_requests.py`
- **pydantic_error_handler.py** (24 connections) — `server/error_handlers/pydantic_error_handler.py`
- **RollStatsRequest** (23 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (23 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **ProfessionService** (21 connections) — `server/game/profession_service.py`
- **professions.py** (20 connections) — `server/api/professions.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- **asyncio** (14 connections)
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **profession_service.py** (13 connections) — `server/game/profession_service.py`
- **test_professions_endpoints.py** (13 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **RollStatsResponse** (12 connections) — `server/schemas/players/character_creation.py`
- **TestRollCharacterStats** (12 connections) — `server/tests/unit/api/test_character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **get_current_user()** (11 connections) — `docs/examples/logging/fastapi_integration.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **get_all_professions()** (11 connections) — `server/api/professions.py`
- **get_profession_by_id()** (11 connections) — `server/api/professions.py`
- **ErrorSeverity** (10 connections) — `server/error_types.py`
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- *... and 156 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (49 shared connections)
- [User](User.md) (32 shared connections)
- [ErrorType](ErrorType.md) (31 shared connections)
- [get_logger](get_logger.md) (30 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (22 shared connections)
- [Stats](Stats.md) (14 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (12 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (12 shared connections)
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (7 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (7 shared connections)
- [GameBundle](GameBundle.md) (5 shared connections)
- [test_profession_service.py](test_profession_service.py.md) (3 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/character_creation.py`
- `server/api/professions.py`
- `server/commands/admin_shutdown_command.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_types.py`
- `server/game/profession_service.py`
- `server/main.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_professions_endpoints.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 555 (98%)
- INFERRED: 14 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*