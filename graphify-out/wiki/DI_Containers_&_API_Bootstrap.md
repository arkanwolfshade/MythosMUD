# DI Containers & API Bootstrap

> 326 nodes

## Key Concepts

- **PlayerService** (105 connections) — `server/game/player_service.py`
- **players.py** (76 connections) — `server/api/players.py`
- **server/schemas/__init__.py** (70 connections) — `server/schemas/__init__.py`
- **players/__init__.py** (48 connections) — `server/schemas/players/__init__.py`
- **PlayerRead** (46 connections) — `server/schemas/players/player.py`
- **player_service.py** (38 connections) — `server/game/player_service.py`
- **api/player_respawn.py** (28 connections) — `server/api/player_respawn.py`
- **player_schema_converter.py** (21 connections) — `server/game/player_schema_converter.py`
- **stats_generator.py** (21 connections) — `server/game/stats_generator.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **_start_login_grace_period_body()** (17 connections) — `server/api/players.py`
- **FastAPIRequest** (16 connections)
- **get_player_quests()** (15 connections) — `server/api/players.py`
- **spell_costs.py** (15 connections) — `server/game/magic/spell_costs.py`
- **players/player.py** (15 connections) — `server/schemas/players/player.py`
- **UUID** (14 connections)
- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **select_character()** (13 connections) — `server/api/players.py`
- **UUID** (13 connections)
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **PositionState** (12 connections) — `server/models/game.py`
- **get_skills_catalog()** (12 connections) — `server/api/skills.py`
- *... and 301 more nodes in this community*

## Relationships

- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (81 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (54 shared connections)
- [Player Effects (Corruption/Fear/Lucidity)](Player_Effects_Corruption-Fear-Lucidity.md) (30 shared connections)
- [User Manager & Character Info](User_Manager_&_Character_Info.md) (27 shared connections)
- [FastAPI Dependency Providers](FastAPI_Dependency_Providers.md) (21 shared connections)
- [Admin NPC Management API](Admin_NPC_Management_API.md) (14 shared connections)
- [Community 479](Community_479.md) (12 shared connections)
- [Community 110](Community_110.md) (8 shared connections)
- [Community 375](Community_375.md) (8 shared connections)
- [Community 61](Community_61.md) (8 shared connections)
- [Community 122](Community_122.md) (7 shared connections)
- [Community 60](Community_60.md) (7 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/containers.py`
- `server/api/player_respawn.py`
- `server/api/player_router.py`
- `server/api/players.py`
- `server/api/skills.py`
- `server/app/game_tick_processing.py`
- `server/dependencies.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/player_schema_converter.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/game/quest/__init__.py`
- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/realtime/connection_manager_api.py`
- `server/schemas/__init__.py`
- `server/schemas/players/__init__.py`

## Audit Trail

- EXTRACTED: 988 (97%)
- INFERRED: 31 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*