# api/character_creation.py

> 257 nodes

## Key Concepts

- **api/character_creation.py** (66 connections) — `server/api/character_creation.py`
- **players/__init__.py** (48 connections) — `server/schemas/players/__init__.py`
- **PlayerRead** (47 connections) — `server/schemas/players/player.py`
- **SkillService** (38 connections) — `server/game/skill_service.py`
- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **CreateCharacterRequest** (25 connections) — `server/schemas/players/player_requests.py`
- **RollStatsRequest** (23 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (23 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **ProfessionService** (21 connections) — `server/game/profession_service.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **professions.py** (20 connections) — `server/api/professions.py`
- **players/player.py** (20 connections) — `server/schemas/players/player.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- **asyncio** (14 connections)
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **test_professions_endpoints.py** (13 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **RollStatsResponse** (12 connections) — `server/schemas/players/character_creation.py`
- **TestRollCharacterStats** (12 connections) — `server/tests/unit/api/test_character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **get_all_professions()** (11 connections) — `server/api/professions.py`
- **get_profession_by_id()** (11 connections) — `server/api/professions.py`
- **PlayerBase** (10 connections) — `server/schemas/players/player.py`
- *... and 232 more nodes in this community*

## Relationships

- [server/dependencies.py](server-dependencies.py.md) (37 shared connections)
- [User](User.md) (35 shared connections)
- [get_logger](get_logger.md) (32 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (27 shared connections)
- [players.py](players.py.md) (25 shared connections)
- [test_player_requests.py](test_player_requests.py.md) (24 shared connections)
- [PlayerService](PlayerService.md) (16 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (12 shared connections)
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (7 shared connections)
- [SkillRepository](SkillRepository.md) (6 shared connections)
- [PlayerRespawnWrapper](PlayerRespawnWrapper.md) (5 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/api/professions.py`
- `server/commands/admin_shutdown_command.py`
- `server/dependencies.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/profession.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_professions_endpoints.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 729 (97%)
- INFERRED: 21 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*