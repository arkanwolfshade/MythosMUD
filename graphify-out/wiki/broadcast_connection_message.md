# .broadcast_connection_message

> 12 nodes

## Key Concepts

- **.broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **._get_players_batch()** (4 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (4 connections) — `server/realtime/connection_manager.py`
- **Get a player from the persistence layer (async version).** (1 connections) — `server/realtime/connection_manager.py`
- **Get a player from the persistence layer (public API).** (1 connections) — `server/realtime/connection_manager.py`
- **Get multiple players from the persistence layer in a single batch operation.** (1 connections) — `server/realtime/connection_manager.py`
- **Track when a player connects.** (1 connections) — `server/realtime/connection_manager.py`
- **Broadcast a connection message for a player who is already tracked as online.** (1 connections) — `server/realtime/connection_manager.py`
- **Send initial game_state event to a newly connected player.** (1 connections) — `server/realtime/connection_manager.py`

## Relationships

- [UUID](UUID.md) (5 shared connections)
- [ConnectionManager](ConnectionManager.md) (5 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (2 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*