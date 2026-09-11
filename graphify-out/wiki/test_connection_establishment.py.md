# test_connection_establishment.py

> 41 nodes

## Key Concepts

- **test_connection_establishment.py** (57 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_track_player_presence()** (13 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (11 connections) — `server/realtime/connection_establishment.py`
- **asyncio** (11 connections)
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **test_cleanup_dead_connections_with_dead()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_empty_list()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_persistence()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_room_id()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_success()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_cancels_leftover_rest()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_existing_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_new_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_reconnect_during_grace_runs_enter_setup()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_remove_dead_connection_not_present()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_connection_metadata_no_session_token()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_error()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_FakeClientState** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **.__init__()** (2 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **UUID** (2 connections)
- **.__init__()** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Remove a single dead connection from tracking structures. Args: conn_id: The…** (1 connections) — `server/realtime/connection_establishment.py`
- **Clean up dead connections under lock. Args: dead_connection_ids: List of dead…** (1 connections) — `server/realtime/connection_establishment.py`
- *... and 16 more nodes in this community*

## Relationships

- [_as_mgr](_as_mgr.md) (55 shared connections)
- [connection_establishment.py](connection_establishment.py.md) (25 shared connections)
- [_FakeEstablishmentManager](_FakeEstablishmentManager.md) (3 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (1 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 148 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*