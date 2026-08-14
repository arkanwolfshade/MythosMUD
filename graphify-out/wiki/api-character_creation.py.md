# api/character_creation.py

> 230 nodes

## Key Concepts

- **api/character_creation.py** (64 connections) — `server/api/character_creation.py`
- **PlayerRead** (50 connections) — `server/schemas/players/player.py`
- **SkillService** (38 connections) — `server/game/skill_service.py`
- **players/__init__.py** (38 connections) — `server/schemas/players/__init__.py`
- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **RollStatsRequest** (23 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (23 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **ProfessionService** (21 connections) — `server/game/profession_service.py`
- **CreateCharacterRequest** (21 connections) — `server/schemas/players/player_requests.py`
- **players/player.py** (20 connections) — `server/schemas/players/player.py`
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- **asyncio** (14 connections)
- **RollStatsResponse** (13 connections) — `server/schemas/players/character_creation.py`
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **PlayerBase** (11 connections) — `server/schemas/players/player.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **get_stats_generator()** (11 connections) — `server/dependencies.py`
- **CreateCharacterResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **CharacterInfo** (10 connections) — `server/schemas/players/player.py`
- **PlayerCreate** (10 connections) — `server/schemas/players/player.py`
- **RolledStats** (10 connections) — `server/schemas/players/stat_values.py`
- *... and 205 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (37 shared connections)
- [get_logger](get_logger.md) (36 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (22 shared connections)
- [User](User.md) (22 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (21 shared connections)
- [test_player_schemas.py](test_player_schemas.py.md) (17 shared connections)
- [PlayerService](PlayerService.md) (17 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (13 shared connections)
- [Stats](Stats.md) (13 shared connections)
- [MythosMUDError](MythosMUDError.md) (7 shared connections)
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (6 shared connections)
- [test_professions_endpoints.py](test_professions_endpoints.py.md) (4 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/dependencies.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/profession.py`
- `server/schemas/players/stat_values.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 654 (95%)
- INFERRED: 35 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*