# Dead Code Cleanup Plan

> 159 nodes

## Key Concepts

- **PlayerService** (141 connections) — `server/game/player_service.py`
- **players.py** (69 connections) — `server/api/players.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **test_players_api_coverage.py** (28 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **FastAPIRequest** (17 connections)
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **UUID** (15 connections)
- **get_player_quests()** (14 connections) — `server/api/players.py`
- **UUID** (14 connections)
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (13 connections) — `server/api/players.py`
- **select_character()** (12 connections) — `server/api/players.py`
- **_user()** (12 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **Any** (11 connections)
- **create_player()** (10 connections) — `server/api/players.py`
- **list_players()** (10 connections) — `server/api/players.py`
- **_validate_character_id()** (10 connections) — `server/api/players.py`
- **get_player_skills()** (9 connections) — `server/api/players.py`
- **_get_connection_manager()** (9 connections) — `server/api/players.py`
- **start_login_grace_period_endpoint()** (9 connections) — `server/api/players.py`
- **.delete_player()** (9 connections) — `server/game/player_service.py`
- **DeleteCharacterResponse** (9 connections) — `server/schemas/players/player.py`
- **LoginGracePeriodResponse** (9 connections) — `server/schemas/players/player.py`
- **__init__.py** (9 connections) — `server/schemas/quest/__init__.py`
- *... and 134 more nodes in this community*

## Relationships

- [Player Domain Model](Player_Domain_Model.md) (34 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (24 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (24 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (24 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (17 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (13 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (10 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (8 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (8 shared connections)
- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (8 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (7 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (7 shared connections)

## Source Files

- `server/api/players.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/schemas/players/player.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_api_coverage.py`

## Audit Trail

- EXTRACTED: 820 (91%)
- INFERRED: 86 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*