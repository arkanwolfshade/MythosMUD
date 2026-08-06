# commands channel rationale

> 9 nodes

## Key Concepts

- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._is_websocket_open()** (4 connections) — `server/realtime/connection_manager.py`
- **WebSocket** (4 connections)
- **._safe_close_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **.get_connection_id_from_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **Check if a WebSocket is open.** (1 connections) — `server/realtime/connection_manager.py`
- **Safely close a WebSocket connection.** (1 connections) — `server/realtime/connection_manager.py`
- **Connect a WebSocket for a player.** (1 connections) — `server/realtime/connection_manager.py`
- **Get connection ID from a WebSocket instance.** (1 connections) — `server/realtime/connection_manager.py`

## Relationships

- [Room Broadcast](Room_Broadcast.md) (7 shared connections)
- [connection establishment realtime](connection_establishment_realtime.md) (1 shared connections)
- [target resolution service](target_resolution_service.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*