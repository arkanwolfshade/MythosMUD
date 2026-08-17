# User

> 213 nodes

## Key Concepts

- **User** (293 connections) — `server/models/user.py`
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
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **RollStatsResponse** (12 connections) — `server/schemas/players/character_creation.py`
- **TestRollCharacterStats** (12 connections) — `server/tests/unit/api/test_character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- **get_profession_service()** (10 connections) — `server/dependencies.py`
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **Any** (9 connections)
- **TestCreateCharacterWithStats** (8 connections) — `server/tests/unit/api/test_character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- *... and 188 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (66 shared connections)
- [PlayerService](PlayerService.md) (49 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (41 shared connections)
- [login_user](login_user.md) (20 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (19 shared connections)
- [ExplorationService](ExplorationService.md) (19 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (18 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (17 shared connections)
- [pytest.md](pytest.md.md) (17 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (15 shared connections)
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (14 shared connections)
- [test_endpoints_invites.py](test_endpoints_invites.py.md) (11 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/character_creation.py`
- `server/auth/users.py`
- `server/commands/admin_shutdown_command.py`
- `server/dependencies.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/models/user.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/auth/test_users_current_user_logging.py`
- `server/tests/unit/models/test_user.py`

## Audit Trail

- EXTRACTED: 705 (87%)
- INFERRED: 106 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*