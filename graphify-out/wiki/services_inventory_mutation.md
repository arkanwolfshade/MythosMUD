# services inventory mutation

> 16 nodes

## Key Concepts

- **safe_close_websocket_impl()** (10 connections) — `server/realtime/connection_manager_methods.py`
- **is_websocket_open_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_connection_id_from_websocket_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._is_websocket_open()** (4 connections) — `server/realtime/connection_manager.py`
- **WebSocket** (4 connections)
- **._safe_close_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **.get_connection_id_from_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **WebSocket** (3 connections)
- **Check if a WebSocket is open.** (1 connections) — `server/realtime/connection_manager.py`
- **Safely close a WebSocket connection.** (1 connections) — `server/realtime/connection_manager.py`
- **Connect a WebSocket for a player.** (1 connections) — `server/realtime/connection_manager.py`
- **Get connection ID from a WebSocket instance.** (1 connections) — `server/realtime/connection_manager.py`
- **Get connection ID from a WebSocket instance.** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Check if a WebSocket is open.** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Safely close a WebSocket connection.** (1 connections) — `server/realtime/connection_manager_methods.py`

## Relationships

- [Room Broadcast](Room_Broadcast.md) (8 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (3 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (3 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (3 shared connections)
- [connection establishment realtime](connection_establishment_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*