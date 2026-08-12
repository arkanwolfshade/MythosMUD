# .connect_websocket

> 9 nodes

## Key Concepts

- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_connection_id_from_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **._is_websocket_open()** (4 connections) — `server/realtime/connection_manager.py`
- **._safe_close_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **WebSocket** (4 connections)
- **Check if a WebSocket is open.** (1 connections) — `server/realtime/connection_manager.py`
- **Safely close a WebSocket connection.** (1 connections) — `server/realtime/connection_manager.py`
- **Connect a WebSocket for a player.** (1 connections) — `server/realtime/connection_manager.py`
- **Get connection ID from a WebSocket instance.** (1 connections) — `server/realtime/connection_manager.py`

## Relationships

- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*