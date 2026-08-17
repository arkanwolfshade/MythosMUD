# server realtime connection session management

> 65 nodes

## Key Concepts

- **test_connection_session_management.py** (51 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_as_mgr()** (21 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_make_manager()** (20 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_as_ws()** (14 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_FakeWebSocket** (13 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **asyncio** (13 connections)
- **_is_websocket_connected()** (9 connections) — `server/realtime/connection_session_management.py`
- **test_disconnect_all_connections_for_session()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_all_connections_for_session_partial_success()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_close_error()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_key_error()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_same_session_is_noop()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_success()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_meta()** (8 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_not_connected()** (8 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
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
- *... and 40 more nodes in this community*

## Relationships

- [server realtime connection session management](server_realtime_connection_session_management.md) (28 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (8 shared connections)
- [server realtime connection models connectionmetadata](server_realtime_connection_models_connectionmetadata.md) (3 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/realtime/connection_session_management.py`
- `server/tests/unit/realtime/test_connection_session_management.py`

## Audit Trail

- EXTRACTED: 190 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*