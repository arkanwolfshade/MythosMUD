# Test Connection Session Management

> 27 nodes

## Key Concepts

- **_as_mgr()** (21 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_make_manager()** (20 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **asyncio** (13 connections)
- **test_disconnect_connection_for_session_success()** (8 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_FakeSessionManager** (6 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_all_connections_for_session_empty_list()** (6 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_none_websocket()** (6 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_not_in_active()** (6 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_error()** (6 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_no_existing_session()** (6 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_cleanup_old_session_tracking_no_player()** (5 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_cleanup_old_session_tracking_session_not_in_connections()** (5 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_cleanup_old_session_tracking_success()** (5 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_cleanup_player_data_for_session()** (5 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_cleanup_player_data_for_session_no_last_seen()** (5 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Typed stand-in for ConnectionManager; MagicMock attributes are Any.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Test _disconnect_connection_for_session() successfully disconnects connection.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Test _disconnect_connection_for_session() returns False when not in…** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Test _disconnect_connection_for_session() handles None websocket.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Test _disconnect_all_connections_for_session() handles empty list.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Test _cleanup_old_session_tracking() handles player not in player_sessions.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Test _cleanup_old_session_tracking() cleans up old session on reconnect.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Test _cleanup_old_session_tracking() handles session not in session_connections.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Test _cleanup_player_data_for_session() cleans up all player data.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Test _cleanup_player_data_for_session() handles player not in last_seen.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- *... and 2 more nodes in this community*

## Relationships

- [Test Connection Session Management](Test_Connection_Session_Management.md) (38 shared connections)
- [Connection Session Management](Connection_Session_Management.md) (12 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_session_management.py`

## Audit Trail

- EXTRACTED: 92 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*