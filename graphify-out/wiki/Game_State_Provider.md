# Game State Provider

> 29 nodes · cohesion 0.15

## Key Concepts

- **GameStateProvider** (27 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (15 connections) — `server/realtime/integration/game_state_provider.py`
- **Any** (13 connections) — `server/realtime/integration/game_state_provider.py`
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_data_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_room_occupants()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **Get list of occupants in a room.          Args:             room_id: The room ID** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get room data and convert player UUIDs to names.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Add grace period indicators to occupant name.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Process room occupants and separate into players and NPCs with grace period indi** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get fallback player data when PlayerService is unavailable.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Provides initial game state for newly connected players.      This class provide** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get complete player data using PlayerService or fallback.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get who this player is following for client title panel: { target_name, target_t** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get login grace period status for player.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 4 more nodes in this community*

## Relationships

- [[Realtime Game State]] (14 shared connections)
- [[Look Command Helpers]] (8 shared connections)
- [[Room Occupant Events]] (4 shared connections)
- [[Game State Provider Tests]] (1 shared connections)
- [[Combat Player Broadcasts]] (1 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`

## Audit Trail

- EXTRACTED: 146 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
