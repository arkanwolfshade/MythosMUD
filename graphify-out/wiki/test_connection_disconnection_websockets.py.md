# test_connection_disconnection_websockets.py

> 30 nodes

## Key Concepts

- **test_connection_disconnection_websockets.py** (26 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **asyncio** (8 connections)
- **_session_cleanup_manager()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_cleanup_websocket_disconnect_clears_session_tracking()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_disconnect_connection_by_id_impl_websocket()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **mock_manager()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_cleanup_fully_disconnected_player_clears_session_tracking()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_cleanup_fully_disconnected_player_keeps_session_while_connected()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_cleanup_websocket_disconnect_continues_after_close_error()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_disconnect_connection_by_id_impl_not_found()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_safe_close_websocket_swallows_websocket_disconnect()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_continues_after_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_empty_list()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_idempotent_second_pass()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **mock_safe_close_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **fixture** (2 connections)
- **UUID** (2 connections)
- **Unit tests for connection disconnection websocket functions. Tests the…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Test disconnect_connection_by_id_impl() disconnects websocket connection.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Regression: e2e logout hit WebSocketDisconnect on close and aborted leave…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Close failures must not skip intentional leave tracking / room cleanup.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Session tracking must not outlive a player's last connection. Leaked session…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **The ordinary disconnect path must clear session tracking too. This is the path…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **A player with a surviving connection keeps their session mapping.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- *... and 5 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (16 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (6 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`

## Audit Trail

- EXTRACTED: 62 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*