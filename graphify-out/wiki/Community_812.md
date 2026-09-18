# Community 812

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

- [Community 336](Community_336.md) (4 shared connections)
- [Community 62](Community_62.md) (3 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (3 shared connections)
- [Community 93](Community_93.md) (2 shared connections)
- [Community 442](Community_442.md) (1 shared connections)
- [Community 95](Community_95.md) (1 shared connections)
- [Community 92](Community_92.md) (1 shared connections)
- [Community 42](Community_42.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_connection.py`

## Audit Trail

- EXTRACTED: 38 (90%)
- INFERRED: 4 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*