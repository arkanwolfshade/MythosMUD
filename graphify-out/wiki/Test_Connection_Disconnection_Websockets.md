# Test Connection Disconnection Websockets

> 42 nodes

## Key Concepts

- **test_connection_disconnection_websockets.py** (26 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **safe_close_websocket_impl()** (13 connections) — `server/realtime/connection_websocket_close.py`
- **asyncio** (8 connections)
- **is_websocket_open_impl()** (7 connections) — `server/realtime/connection_websocket_close.py`
- **_CloseableWebSocketManager** (5 connections) — `server/realtime/connection_websocket_close.py`
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
- **.is_websocket_closed()** (2 connections) — `server/realtime/connection_websocket_close.py`
- **.mark_websocket_closed()** (2 connections) — `server/realtime/connection_websocket_close.py`
- **test_is_websocket_open_impl()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **WebSocket** (2 connections)
- **fixture** (2 connections)
- **UUID** (2 connections)
- **Protocol** (1 connections)
- *... and 17 more nodes in this community*

## Relationships

- [Test Connection Disconnection](Test_Connection_Disconnection.md) (17 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (7 shared connections)
- [Connection Manager](Connection_Manager.md) (2 shared connections)
- [Connection Manager Methods](Connection_Manager_Methods.md) (2 shared connections)
- [Test Connection Rate Limiter](Test_Connection_Rate_Limiter.md) (2 shared connections)
- [Test Message Queue](Test_Message_Queue.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/realtime/connection_websocket_close.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 86 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*