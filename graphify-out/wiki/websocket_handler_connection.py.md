# websocket_handler_connection.py

> 20 nodes

## Key Concepts

- **websocket_handler_connection.py** (18 connections) — `server/realtime/websocket_handler_connection.py`
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **cleanup_websocket_connection()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (5 connections)
- **AsyncPersistenceRoomLookup** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **PlayerDisconnectService** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **PlayerMuteCleanup** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **Protocol** (3 connections)
- **.on_player_disconnect()** (2 connections) — `server/realtime/websocket_handler_connection.py`
- **WebSocket** (2 connections)
- **.get_room_by_id()** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **.cleanup_player_mutes()** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **WebSocket connection lifecycle: setup, welcome, and cleanup on disconnect.…** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Send welcome event to the client. Returns: True if successful, False if…** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Notify subsystems when a WebSocket session ends for a player.** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Narrow persistence surface for loading ``Room`` by id in the WS handler.** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Narrow UserManager surface for clearing a disconnected player's mute state.** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Clean up connection, follow state, party state, and player mute data on…** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Set up initial connection state and send initial game state. Returns: Tuple of…** (1 connections) — `server/realtime/websocket_handler_connection.py`

## Relationships

- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_connection.py`

## Audit Trail

- EXTRACTED: 38 (90%)
- INFERRED: 4 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*