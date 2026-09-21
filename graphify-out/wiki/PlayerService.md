# PlayerService

> 356 nodes

## Key Concepts

- **PlayerService** (109 connections) — `server/game/player_service.py`
- **server/schemas/__init__.py** (70 connections) — `server/schemas/__init__.py`
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
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- **UUID** (14 connections)
- **asyncio** (14 connections)
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **get_player_service()** (13 connections) — `server/dependencies.py`
- **RollStatsResponse** (12 connections) — `server/schemas/players/character_creation.py`
- **TestRollCharacterStats** (12 connections) — `server/tests/unit/api/test_character_creation.py`
- **get_current_user()** (12 connections) — `docs/examples/logging/fastapi_integration.py`
- *... and 331 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (67 shared connections)
- [get_logger](get_logger.md) (42 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (41 shared connections)
- [User](User.md) (35 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (31 shared connections)
- [Stats](Stats.md) (28 shared connections)
- [test_skill_service.py](test_skill_service.py.md) (11 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (11 shared connections)
- [SpellCostsService](SpellCostsService.md) (7 shared connections)
- [test_professions_endpoints.py](test_professions_endpoints.py.md) (7 shared connections)
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (7 shared connections)
- [endpoints.py](endpoints.py.md) (6 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/__init__.py`
- `server/api/character_creation.py`
- `server/api/player_router.py`
- `server/api/professions.py`
- `server/commands/admin_shutdown_command.py`
- `server/dependencies.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/schemas/__init__.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/profession.py`

## Audit Trail

- EXTRACTED: 1018 (96%)
- INFERRED: 43 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*