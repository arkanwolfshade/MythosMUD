# Game Session Lifecycle

> 56 nodes · cohesion 0.06

## Key Concepts

- **test_connection_session_management.py** (29 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_disconnect_connection_for_session()** (13 connections) — `server/realtime/connection_session_management.py`
- **handle_new_game_session_impl()** (13 connections) — `server/realtime/connection_session_management.py`
- **_disconnect_all_connections_for_session()** (10 connections) — `server/realtime/connection_session_management.py`
- **_cleanup_old_session_tracking()** (9 connections) — `server/realtime/connection_session_management.py`
- **_is_websocket_connected()** (9 connections) — `server/realtime/connection_session_management.py`
- **_cleanup_player_data_for_session()** (8 connections) — `server/realtime/connection_session_management.py`
- **UUID** (6 connections) — `server/realtime/connection_session_management.py`
- **Any** (5 connections) — `server/realtime/connection_session_management.py`
- **test_disconnect_connection_for_session_close_error()** (4 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_cleanup_old_session_tracking_no_player()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_cleanup_old_session_tracking_session_not_in_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_cleanup_old_session_tracking_success()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_cleanup_player_data_for_session()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_cleanup_player_data_for_session_no_last_seen()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_all_connections_for_session()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_all_connections_for_session_empty_list()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_all_connections_for_session_partial_success()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_key_error()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_none_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_not_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_not_in_active()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_success()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_error()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_no_existing_session()** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- *... and 31 more nodes in this community*

## Relationships

- [[NPC Admin API]] (9 shared connections)
- [[Room Occupant Events]] (2 shared connections)

## Source Files

- `server/realtime/connection_session_management.py`
- `server/tests/unit/realtime/test_connection_session_management.py`

## Audit Trail

- EXTRACTED: 195 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
