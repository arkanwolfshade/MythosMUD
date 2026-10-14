# safe_close_websocket_impl

> 24 nodes

## Key Concepts

- **safe_close_websocket_impl()** (13 connections) — `server/realtime/connection_websocket_close.py`
- **is_websocket_open_impl()** (7 connections) — `server/realtime/connection_websocket_close.py`
- **connection_websocket_close.py** (7 connections) — `server/realtime/connection_websocket_close.py`
- **_CloseableWebSocketManager** (5 connections) — `server/realtime/connection_websocket_close.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._is_websocket_open()** (4 connections) — `server/realtime/connection_manager.py`
- **._safe_close_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **WebSocket** (4 connections)
- **.get_connection_id_from_websocket()** (3 connections) — `server/realtime/connection_manager.py`
- **test_safe_close_websocket_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **.is_websocket_closed()** (2 connections) — `server/realtime/connection_websocket_close.py`
- **.mark_websocket_closed()** (2 connections) — `server/realtime/connection_websocket_close.py`
- **test_is_websocket_open_impl()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **WebSocket** (2 connections)
- **Protocol** (1 connections)
- **Check if a WebSocket is open.** (1 connections) — `server/realtime/connection_manager.py`
- **Safely close a WebSocket connection.** (1 connections) — `server/realtime/connection_manager.py`
- **Connect a WebSocket for a player.** (1 connections) — `server/realtime/connection_manager.py`
- **Get connection ID from a WebSocket instance.** (1 connections) — `server/realtime/connection_manager.py`
- **Safe WebSocket close helpers for connection management. Leaf module: no imports…** (1 connections) — `server/realtime/connection_websocket_close.py`
- **Return True if this WebSocket id was already marked closed.** (1 connections) — `server/realtime/connection_websocket_close.py`
- **Record that this WebSocket id has been closed.** (1 connections) — `server/realtime/connection_websocket_close.py`
- **Check if a WebSocket is open.** (1 connections) — `server/realtime/connection_websocket_close.py`
- **Safely close a WebSocket connection.** (1 connections) — `server/realtime/connection_websocket_close.py`

## Relationships

- [MessageQueue](MessageQueue.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (5 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_websocket_close.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*