# Dead Code Cleanup Plan

> 112 nodes

## Key Concepts

- **players.py** (69 connections) — `server/api/players.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **test_players_api_coverage.py** (28 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **FastAPIRequest** (17 connections)
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **UUID** (15 connections)
- **get_player_quests()** (14 connections) — `server/api/players.py`
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (13 connections) — `server/api/players.py`
- **select_character()** (12 connections) — `server/api/players.py`
- **_user()** (12 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **get_skills_catalog()** (11 connections) — `server/api/skills.py`
- **create_player()** (10 connections) — `server/api/players.py`
- **list_players()** (10 connections) — `server/api/players.py`
- **_validate_character_id()** (10 connections) — `server/api/players.py`
- **get_player_skills()** (9 connections) — `server/api/players.py`
- **_get_connection_manager()** (9 connections) — `server/api/players.py`
- **start_login_grace_period_endpoint()** (9 connections) — `server/api/players.py`
- **LoginGracePeriodResponse** (9 connections) — `server/schemas/players/player.py`
- **__init__.py** (9 connections) — `server/schemas/quest/__init__.py`
- **get_user_characters()** (8 connections) — `server/api/players.py`
- **get_player()** (8 connections) — `server/api/players.py`
- **delete_player()** (8 connections) — `server/api/players.py`
- **skill.py** (8 connections) — `server/schemas/players/skill.py`
- *... and 87 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (30 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (24 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (19 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (18 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (10 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (8 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (7 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (7 shared connections)
- [Async Persistence Migration](Async_Persistence_Migration.md) (7 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (5 shared connections)
- [Quest Service Core](Quest_Service_Core.md) (5 shared connections)
- [Logging System Planning](Logging_System_Planning.md) (5 shared connections)

## Source Files

- `server/api/players.py`
- `server/api/skills.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/schemas/players/player.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 585 (96%)
- INFERRED: 25 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*