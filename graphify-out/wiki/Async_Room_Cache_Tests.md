# Async Room Cache Tests

> 17 nodes · cohesion 0.15

## Key Concepts

- **cleanup_websocket_connection()** (7 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (7 connections) — `server/realtime/websocket_handler_connection.py`
- **AsyncPersistenceRoomLookup** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **PlayerDisconnectService** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (5 connections)
- **_fetch_room_for_tracked_player()** (4 connections) — `server/realtime/websocket_helpers.py`
- **.get_room_by_id()** (3 connections) — `server/realtime/websocket_handler_connection.py`
- **.on_player_disconnect()** (3 connections) — `server/realtime/websocket_handler_connection.py`
- **Protocol** (2 connections)
- **WebSocket** (2 connections)
- **Send welcome event to the client.      Returns:         True if successful, Fals** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Notify subsystems when a WebSocket session ends for a player.** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Narrow persistence surface for loading ``Room`` by id in the WS handler.** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Clean up connection, follow state, party state, and player mute data on disconne** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Set up initial connection state and send initial game state.      Returns:** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Load the room instance for the player's current_room_id.      Returns:** (1 connections) — `server/realtime/websocket_helpers.py`

## Relationships

- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (9 shared connections)
- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (3 shared connections)
- [WebSocket Player Helpers](WebSocket_Player_Helpers.md) (2 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_helpers.py`

## Audit Trail

- EXTRACTED: 49 (86%)
- INFERRED: 8 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*