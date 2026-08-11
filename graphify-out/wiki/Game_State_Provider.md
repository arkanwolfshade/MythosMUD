# Game State Provider

> 39 nodes

## Key Concepts

- **UUID** (15 connections)
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_data_for_client()** (9 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (8 connections) — `server/realtime/nats_message_handler.py`
- **._convert_player_uuids_to_names()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (5 connections)
- **.get_room_occupants()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **Initialize the game state provider.          Args:             room_manager: Roo** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get a player from the persistence layer (async version).          Args:** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get multiple players from the persistence layer in a single batch operation.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get NPC names for multiple NPCs in a batch operation.          Args:** (1 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 14 more nodes in this community*

## Relationships

- [Game State Provider Tests](Game_State_Provider_Tests.md) (18 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (4 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (3 shared connections)
- [Container Persistence Queries](Container_Persistence_Queries.md) (2 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (2 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (1 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (1 shared connections)
- [3. Systematic Investigation Approach](3._Systematic_Investigation_Approach.md) (1 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (1 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (1 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (1 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 156 (92%)
- INFERRED: 14 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*