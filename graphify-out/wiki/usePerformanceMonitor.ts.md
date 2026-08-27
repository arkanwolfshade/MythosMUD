# usePerformanceMonitor.ts

> 10 nodes

## Key Concepts

- **AsyncPersistenceRoomLookup** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **PlayerDisconnectService** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **PlayerMuteCleanup** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **Protocol** (3 connections)
- **.on_player_disconnect()** (2 connections) — `server/realtime/websocket_handler_connection.py`
- **.get_room_by_id()** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **.cleanup_player_mutes()** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Notify subsystems when a WebSocket session ends for a player.** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Narrow persistence surface for loading ``Room`` by id in the WS handler.** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Narrow UserManager surface for clearing a disconnected player's mute state.** (1 connections) — `server/realtime/websocket_handler_connection.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_connection.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*