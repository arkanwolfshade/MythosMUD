# is_websocket_open_impl

> 13 nodes

## Key Concepts

- **is_websocket_open_impl()** (7 connections) — `server/realtime/connection_websocket_close.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._is_websocket_open()** (4 connections) — `server/realtime/connection_manager.py`
- **._safe_close_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **WebSocket** (4 connections)
- **.get_connection_id_from_websocket()** (3 connections) — `server/realtime/connection_manager.py`
- **test_is_websocket_open_impl()** (2 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **WebSocket** (2 connections)
- **Check if a WebSocket is open.** (1 connections) — `server/realtime/connection_manager.py`
- **Safely close a WebSocket connection.** (1 connections) — `server/realtime/connection_manager.py`
- **Connect a WebSocket for a player.** (1 connections) — `server/realtime/connection_manager.py`
- **Get connection ID from a WebSocket instance.** (1 connections) — `server/realtime/connection_manager.py`
- **Check if a WebSocket is open.** (1 connections) — `server/realtime/connection_websocket_close.py`

## Relationships

- [ConnectionManager](ConnectionManager.md) (7 shared connections)
- [RateLimiter](RateLimiter.md) (3 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_websocket_close.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*