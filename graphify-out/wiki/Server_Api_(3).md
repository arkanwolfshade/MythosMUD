# Server Api (3)

> 204 nodes

## Key Concepts

- **PlayerService** (135 connections) — `server/game/player_service.py`
- **players.py** (66 connections) — `server/api/players.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **test_players_api_coverage.py** (28 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **FastAPIRequest** (16 connections)
- **start_login_grace_period_endpoint()** (16 connections) — `server/api/players.py`
- **get_current_tick()** (15 connections) — `server/app/game_tick_processing.py`
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **get_player_quests()** (14 connections) — `server/api/players.py`
- **UUID** (14 connections)
- **UUID** (13 connections)
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- **_disconnect_other_characters()** (12 connections) — `server/api/players.py`
- **select_character()** (12 connections) — `server/api/players.py`
- **_user()** (12 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **Any** (11 connections)
- **PlayerBase** (11 connections) — `server/schemas/players/player.py`
- **create_player()** (10 connections) — `server/api/players.py`
- **list_players()** (10 connections) — `server/api/players.py`
- **_validate_character_id()** (10 connections) — `server/api/players.py`
- **PlayerCreate** (10 connections) — `server/schemas/players/player.py`
- *... and 179 more nodes in this community*

## Relationships

- [Server Infrastructure](Server_Infrastructure.md) (42 shared connections)
- [Server Admin](Server_Admin.md) (36 shared connections)
- [Server Api](Server_Api.md) (24 shared connections)
- [Server Game](Server_Game.md) (23 shared connections)
- [Server Schemas](Server_Schemas.md) (20 shared connections)
- [Server Api (4)](Server_Api_%284%29.md) (16 shared connections)
- [Server Game (4)](Server_Game_%284%29.md) (9 shared connections)
- [Server Utils](Server_Utils.md) (8 shared connections)
- [Server Game (9)](Server_Game_%289%29.md) (8 shared connections)
- [Server Realtime (8)](Server_Realtime_%288%29.md) (8 shared connections)
- [Server Models (12)](Server_Models_%2812%29.md) (6 shared connections)
- [Server Quest](Server_Quest.md) (5 shared connections)

## Source Files

- `server/api/players.py`
- `server/app/game_tick_processing.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 963 (90%)
- INFERRED: 105 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*