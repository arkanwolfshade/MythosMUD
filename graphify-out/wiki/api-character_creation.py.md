# api/character_creation.py

> 223 nodes

## Key Concepts

- **api/character_creation.py** (67 connections) — `server/api/character_creation.py`
- **RateLimitError** (49 connections) — `server/exceptions.py`
- **PlayerRead** (46 connections) — `server/schemas/players/player.py`
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
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
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
- *... and 198 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (57 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (30 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (28 shared connections)
- [pytest.md](pytest.md.md) (20 shared connections)
- [DatabaseError](DatabaseError.md) (17 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (15 shared connections)
- [Stats](Stats.md) (15 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (7 shared connections)
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (7 shared connections)
- [test_exceptions.py](test_exceptions.py.md) (6 shared connections)
- [AuthenticationError](AuthenticationError.md) (6 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/commands/admin_shutdown_command.py`
- `server/dependencies.py`
- `server/exceptions.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/schemas/test_player_requests.py`
- `server/tests/unit/test_dependency_injection.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 614 (94%)
- INFERRED: 36 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*