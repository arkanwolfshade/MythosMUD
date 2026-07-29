# test connection establishment

> 26 nodes

## Key Concepts

- **test_connection_establishment.py** (46 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_connection_metadata_no_session_token()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_session_tracking_no_session_id()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_session_tracking_new_session()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_new_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_existing_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_none()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_error()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_error()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_cleans_dead_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Unit tests for connection establishment.  Tests the connection_establishment mod** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_connection_metadata() handles None session and token.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_session_tracking() handles None session_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_session_tracking() creates new session entry.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() successfully sets up player and room.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() handles no persistence.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _track_player_presence() tracks new player.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _track_player_presence() broadcasts for existing player.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_failed_connection() handles None connection_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_failed_connection() cleans up connection.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_failed_connection() handles errors during cleanup.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test establish_websocket_connection() handles errors.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 1 more nodes in this community*

## Relationships

- [connection establishment](connection_establishment.md) (19 shared connections)
- [find dead connections()](find_dead_connections%28%29.md) (6 shared connections)
- [cleanup dead connections()](cleanup_dead_connections%28%29_2.md) (6 shared connections)
- [Update player's connection list to](Update_player%27s_connection_list_to.md) (4 shared connections)
- [WebSocket](WebSocket.md) (3 shared connections)
- [Test setup player and room()](Test_setup_player_and_room%28%29.md) (2 shared connections)
- [Reconnect cancels an in progress](Reconnect_cancels_an_in_progress.md) (1 shared connections)
- [Test establish websocket connection() returns](Test_establish_websocket_connection%28%29_returns.md) (1 shared connections)
- [Test establish websocket connection() successfully](Test_establish_websocket_connection%28%29_successfully.md) (1 shared connections)
- [Test setup connection metadata() creates](Test_setup_connection_metadata%28%29_creates.md) (1 shared connections)
- [Test setup session tracking() adds](Test_setup_session_tracking%28%29_adds.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 95 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*