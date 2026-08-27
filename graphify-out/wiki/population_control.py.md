# population_control.py

> 90 nodes

## Key Concepts

- **test_connection_session_management.py** (51 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **connection_session_management.py** (26 connections) — `server/realtime/connection_session_management.py`
- **_as_mgr()** (21 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_make_manager()** (20 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **handle_new_game_session_impl()** (15 connections) — `server/realtime/connection_session_management.py`
- **_SessionConnectionManager** (14 connections) — `server/realtime/connection_session_management.py`
- **_as_ws()** (14 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_FakeWebSocket** (13 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_disconnect_connection_for_session()** (13 connections) — `server/realtime/connection_session_management.py`
- **asyncio** (13 connections)
- **_disconnect_all_connections_for_session()** (10 connections) — `server/realtime/connection_session_management.py`
- **_cleanup_old_session_tracking()** (9 connections) — `server/realtime/connection_session_management.py`
- **_is_websocket_connected()** (9 connections) — `server/realtime/connection_session_management.py`
- **test_disconnect_all_connections_for_session()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_all_connections_for_session_partial_success()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_close_error()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_key_error()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_same_session_is_noop()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_success()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_cleanup_player_data_for_session()** (8 connections) — `server/realtime/connection_session_management.py`
- **_meta()** (8 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_not_connected()** (8 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_success()** (8 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_FakeSessionManager** (6 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_all_connections_for_session_empty_list()** (6 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- *... and 65 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (13 shared connections)
- [P3 · realtime-connection + events-nats](P3_·_realtime-connection_+_events-nats.md) (5 shared connections)
- [API Endpoints (Phase 2)](API_Endpoints_Phase_2.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [test_go_command.py](test_go_command.py.md) (3 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [chat_service.py](chat_service.py.md) (2 shared connections)

## Source Files

- `server/realtime/connection_session_management.py`
- `server/tests/unit/realtime/test_connection_session_management.py`

## Audit Trail

- EXTRACTED: 245 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*