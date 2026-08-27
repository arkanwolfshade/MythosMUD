# _track_player_presence

> 23 nodes

## Key Concepts

- **_track_player_presence()** (13 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (11 connections) — `server/realtime/connection_establishment.py`
- **asyncio** (11 connections)
- **test_cleanup_dead_connections_empty_list()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_persistence()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_room_id()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_success()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_cancels_leftover_rest()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_existing_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_new_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_reconnect_during_grace_runs_enter_setup()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Get player and setup room subscription. Args: player_id: The player's ID…** (1 connections) — `server/realtime/connection_establishment.py`
- **Track player presence and broadcast connection message. Args: player_id: The…** (1 connections) — `server/realtime/connection_establishment.py`
- **Test _cleanup_dead_connections() handles empty list.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() successfully sets up player and room.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() returns False when player not found.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() handles no persistence.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() handles player with no room_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _track_player_presence() tracks new player.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Already-online reconnect still goes through track_player_connected (occupancy…** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Linkdead reconnect stays in online_players; enter setup must run before grace…** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **WS reconnect must cancel leftover /rest so the countdown cannot kill the new…** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`

## Relationships

- [test_connection_establishment.py](test_connection_establishment.py.md) (22 shared connections)
- [_as_mgr](_as_mgr.md) (20 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 72 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*