# session connection management

> 61 nodes

## Key Concepts

- **test_connection_session_management.py** (30 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **connection_session_management.py** (14 connections) — `server/realtime/connection_session_management.py`
- **_disconnect_connection_for_session()** (14 connections) — `server/realtime/connection_session_management.py`
- **handle_new_game_session_impl()** (14 connections) — `server/realtime/connection_session_management.py`
- **_disconnect_all_connections_for_session()** (10 connections) — `server/realtime/connection_session_management.py`
- **_is_websocket_connected()** (9 connections) — `server/realtime/connection_session_management.py`
- **_cleanup_old_session_tracking()** (9 connections) — `server/realtime/connection_session_management.py`
- **_cleanup_player_data_for_session()** (8 connections) — `server/realtime/connection_session_management.py`
- **UUID** (6 connections)
- **Any** (5 connections)
- **test_disconnect_connection_for_session_close_error()** (4 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_is_websocket_connected_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_is_websocket_connected_disconnected()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_is_websocket_connected_no_client_state()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_is_websocket_connected_no_name()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_success()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_not_in_active()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_none_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_not_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_key_error()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_all_connections_for_session()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_all_connections_for_session_empty_list()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_all_connections_for_session_partial_success()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_cleanup_old_session_tracking_no_player()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_cleanup_old_session_tracking_success()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- *... and 36 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)

## Source Files

- `server/realtime/connection_session_management.py`
- `server/tests/unit/realtime/test_connection_session_management.py`

## Audit Trail

- EXTRACTED: 211 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*