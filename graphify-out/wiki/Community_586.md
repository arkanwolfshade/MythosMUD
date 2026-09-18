# Community 586

> 29 nodes

## Key Concepts

- **test_connection_disconnection_websockets.py** (25 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **disconnect_connection_by_id_impl()** (12 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_fully_disconnected_player()** (10 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (8 connections)
- **_session_cleanup_manager()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_cleanup_websocket_disconnect_clears_session_tracking()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_disconnect_connection_by_id_impl_websocket()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_cleanup_fully_disconnected_player_clears_session_tracking()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_cleanup_fully_disconnected_player_keeps_session_while_connected()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_cleanup_websocket_disconnect_continues_after_close_error()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_disconnect_connection_by_id_impl_not_found()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_safe_close_websocket_swallows_websocket_disconnect()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_continues_after_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_empty_list()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_idempotent_second_pass()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **UUID** (2 connections)
- **Remove player-scoped tracking when no websocket connections remain.** (1 connections) — `server/realtime/connection_disconnection.py`
- **Disconnect a specific connection by its ID. Args: connection_id: The connection…** (1 connections) — `server/realtime/connection_disconnection.py`
- **Unit tests for connection disconnection websocket functions. Tests the…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Test disconnect_connection_by_id_impl() disconnects websocket connection.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Regression: e2e logout hit WebSocketDisconnect on close and aborted leave…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Close failures must not skip intentional leave tracking / room cleanup.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Session tracking must not outlive a player's last connection. Leaked session…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **The ordinary disconnect path must clear session tracking too. This is the path…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **A player with a surviving connection keeps their session mapping.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- *... and 4 more nodes in this community*

## Relationships

- [Community 531](Community_531.md) (14 shared connections)
- [Community 42](Community_42.md) (3 shared connections)
- [Community 532](Community_532.md) (2 shared connections)
- [Community 185](Community_185.md) (2 shared connections)
- [Community 1044](Community_1044.md) (2 shared connections)
- [Community 1480](Community_1480.md) (2 shared connections)
- [Community 1006](Community_1006.md) (1 shared connections)
- [Community 1189](Community_1189.md) (1 shared connections)
- [Community 92](Community_92.md) (1 shared connections)
- [Community 188](Community_188.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`

## Audit Trail

- EXTRACTED: 72 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*