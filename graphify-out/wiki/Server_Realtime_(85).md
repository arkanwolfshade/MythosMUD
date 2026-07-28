# Server Realtime (85)

> 16 nodes

## Key Concepts

- **test_connection_disconnection_websockets.py** (15 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_disconnect_connection_by_id_impl_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **mock_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_empty_list()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_idempotent_second_pass()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_continues_after_none_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_disconnect_connection_by_id_impl_not_found()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **mock_safe_close_websocket()** (2 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Unit tests for connection disconnection websocket functions.  Tests the websocke** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Patch safe_close_websocket_impl used by disconnection helpers.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Test disconnect_all_websockets_impl() with empty connection list.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Second disconnect pass must not KeyError when registry already cleared.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **None websocket on one connection must not skip remaining connection ids.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Test disconnect_connection_by_id_impl() returns False when connection not found.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **Test disconnect_connection_by_id_impl() disconnects websocket connection.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`

## Relationships

- [Server Realtime (60)](Server_Realtime_%2860%29.md) (8 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Realtime (15)](Server_Realtime_%2815%29.md) (2 shared connections)
- [Server Realtime (30)](Server_Realtime_%2830%29.md) (2 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`

## Audit Trail

- EXTRACTED: 42 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*