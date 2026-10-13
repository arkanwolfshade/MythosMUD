# Character Creation & Professions

> 304 nodes

## Key Concepts

- **server/schemas/__init__.py** (70 connections) — `server/schemas/__init__.py`
- **api/character_creation.py** (66 connections) — `server/api/character_creation.py`
- **players/__init__.py** (48 connections) — `server/schemas/players/__init__.py`
- **SkillService** (41 connections) — `server/game/skill_service.py`
- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **CreateCharacterRequest** (25 connections) — `server/schemas/players/player_requests.py`
- **RollStatsRequest** (23 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (23 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **PlayerRead** (20 connections) — `server/schemas/players/player.py`
- **players/player.py** (20 connections) — `server/schemas/players/player.py`
- **ProfessionService** (19 connections) — `server/game/profession_service.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- **test_invite_schemas.py** (15 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **asyncio** (14 connections)
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **schemas/auth/__init__.py** (13 connections) — `server/schemas/auth/__init__.py`
- **RollStatsResponse** (12 connections) — `server/schemas/players/character_creation.py`
- **TestRollCharacterStats** (12 connections) — `server/tests/unit/api/test_character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **get_stats_generator()** (11 connections) — `server/dependencies.py`
- **maps/__init__.py** (11 connections) — `server/schemas/maps/__init__.py`
- *... and 279 more nodes in this community*

## Relationships

- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (39 shared connections)
- [Community 67](Community_67.md) (30 shared connections)
- [Container API Models](Container_API_Models.md) (28 shared connections)
- [API Response Models](API_Response_Models.md) (26 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (23 shared connections)
- [Community 326](Community_326.md) (16 shared connections)
- [Community 150](Community_150.md) (16 shared connections)
- [Community 671](Community_671.md) (11 shared connections)
- [Community 213](Community_213.md) (11 shared connections)
- [Community 361](Community_361.md) (7 shared connections)
- [Map & Admin Responses](Map_&_Admin_Responses.md) (7 shared connections)
- [Community 569](Community_569.md) (6 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/character_creation.py`
- `server/commands/admin_shutdown_command.py`
- `server/dependencies.py`
- `server/game/player_search_service.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/schemas/__init__.py`
- `server/schemas/auth/__init__.py`
- `server/schemas/auth/invite.py`
- `server/schemas/auth/user.py`
- `server/schemas/game/__init__.py`
- `server/schemas/game/game.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`

## Audit Trail

- EXTRACTED: 844 (98%)
- INFERRED: 18 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*