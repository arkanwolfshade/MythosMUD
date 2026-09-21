# api/character_creation.py

> 256 nodes

## Key Concepts

- **api/character_creation.py** (66 connections) — `server/api/character_creation.py`
- **player_service.py** (50 connections) — `server/game/player_service.py`
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
- **player_creation_service.py** (16 connections) — `server/game/player_creation_service.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- **asyncio** (14 connections)
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **test_professions_endpoints.py** (13 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **RollStatsResponse** (12 connections) — `server/schemas/players/character_creation.py`
- **TestRollCharacterStats** (12 connections) — `server/tests/unit/api/test_character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **get_all_professions()** (11 connections) — `server/api/professions.py`
- **get_profession_by_id()** (11 connections) — `server/api/professions.py`
- *... and 231 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (65 shared connections)
- [User](User.md) (27 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (27 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (19 shared connections)
- [Stats](Stats.md) (18 shared connections)
- [ValidationError](ValidationError.md) (12 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (12 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (10 shared connections)
- [SkillRepository](SkillRepository.md) (9 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (6 shared connections)
- [Player](Player.md) (6 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/api/professions.py`
- `server/dependencies.py`
- `server/game/player_creation_service.py`
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
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_professions_endpoints.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 781 (97%)
- INFERRED: 23 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*