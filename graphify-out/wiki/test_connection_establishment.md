# test connection establishment

> 22 nodes

## Key Concepts

- **test_connection_establishment.py** (47 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_register_new_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_connection_metadata()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_session_tracking_no_session_id()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_existing_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_none()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_cleans_dead_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Unit tests for connection establishment.  Tests the connection_establishment mod** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _register_new_connection() registers new connection.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_connection_metadata() creates metadata.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_session_tracking() handles None session_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() successfully sets up player and room.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() handles player with no room_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _track_player_presence() broadcasts for existing player.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_failed_connection() handles None connection_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_failed_connection() cleans up connection.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test establish_websocket_connection() successfully establishes connection.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test establish_websocket_connection() cleans up dead connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`

## Relationships

- [PerformanceTracker](PerformanceTracker.md) (18 shared connections)
- [Test get spawn rules() successfully](Test_get_spawn_rules%28%29_successfully.md) (6 shared connections)
- [middleware()](middleware%28%29.md) (6 shared connections)
- [Test subscribe to subject returns](Test_subscribe_to_subject_returns.md) (4 shared connections)
- [real time](real_time.md) (1 shared connections)
- [test_cleanup_failed_connection_error](test_cleanup_failed_connection_error.md) (1 shared connections)
- [test_establish_websocket_connection_cancels_rest_countdown](test_establish_websocket_connection_cancels_rest_countdown.md) (1 shared connections)
- [test_establish_websocket_connection_error](test_establish_websocket_connection_error.md) (1 shared connections)
- [test_establish_websocket_connection_player_not_found](test_establish_websocket_connection_player_not_found.md) (1 shared connections)
- [test_register_new_connection_existing_player](test_register_new_connection_existing_player.md) (1 shared connections)
- [test_setup_connection_metadata_no_session_token](test_setup_connection_metadata_no_session_token.md) (1 shared connections)
- [test_setup_player_and_room_no_persistence](test_setup_player_and_room_no_persistence.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 88 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*