# server realtime connection manager connectionmanager

> 9 nodes

## Key Concepts

- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._is_websocket_open()** (4 connections) — `server/realtime/connection_manager.py`
- **._safe_close_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **WebSocket** (4 connections)
- **.get_connection_id_from_websocket()** (3 connections) — `server/realtime/connection_manager.py`
- **Check if a WebSocket is open.** (1 connections) — `server/realtime/connection_manager.py`
- **Safely close a WebSocket connection.** (1 connections) — `server/realtime/connection_manager.py`
- **Connect a WebSocket for a player.** (1 connections) — `server/realtime/connection_manager.py`
- **Get connection ID from a WebSocket instance.** (1 connections) — `server/realtime/connection_manager.py`

## Relationships

- [playercombatservice](playercombatservice.md) (4 shared connections)
- [server realtime connection websocket close](server_realtime_connection_websocket_close.md) (2 shared connections)
- [server realtime connection establishment establish](server_realtime_connection_establishment_establish.md) (1 shared connections)
- [newgamesessionresult](newgamesessionresult.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*