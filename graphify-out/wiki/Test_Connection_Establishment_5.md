# Test Connection Establishment

> 32 nodes

## Key Concepts

- **_as_mgr()** (44 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_make_manager()** (42 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_register_new_connection()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_register_new_connection_existing_player()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_update_player_connection_list_with_active()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_persistence()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_success()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_reconnect_during_grace_runs_enter_setup()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_none()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_connection_metadata()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_connection_metadata_no_session_token()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_session_tracking_existing_session()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_session_tracking_new_session()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_session_tracking_no_session_id()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_update_player_connection_list_no_active()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_update_player_connection_list_no_player()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_error()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _update_player_connection_list() handles player not in player_websockets.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _update_player_connection_list() keeps active connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _update_player_connection_list() removes player when no active connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _register_new_connection() registers new connection.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _register_new_connection() adds to existing player connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_connection_metadata() creates metadata.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_connection_metadata() handles None session and token.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_session_tracking() handles None session_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 7 more nodes in this community*

## Relationships

- [Test Connection Establishment](Test_Connection_Establishment.md) (54 shared connections)
- [Test Connection Establishment Ws](Test_Connection_Establishment_Ws.md) (28 shared connections)
- [Connection Establishment](Connection_Establishment.md) (14 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 140 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*