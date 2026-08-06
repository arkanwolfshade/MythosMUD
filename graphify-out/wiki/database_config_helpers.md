# database config helpers

> 19 nodes

## Key Concepts

- **websocket_handler_connection.py** (17 connections) — `server/realtime/websocket_handler_connection.py`
- **cleanup_websocket_connection()** (7 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (7 connections) — `server/realtime/websocket_handler_connection.py`
- **PlayerDisconnectService** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **AsyncPersistenceRoomLookup** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (5 connections)
- **_fetch_room_for_tracked_player()** (4 connections) — `server/realtime/websocket_helpers.py`
- **.on_player_disconnect()** (3 connections) — `server/realtime/websocket_handler_connection.py`
- **.get_room_by_id()** (3 connections) — `server/realtime/websocket_handler_connection.py`
- **Protocol** (2 connections)
- **WebSocket** (2 connections)
- **WebSocket connection lifecycle: setup, welcome, and cleanup on disconnect.  Extr** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Notify subsystems when a WebSocket session ends for a player.** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Narrow persistence surface for loading ``Room`` by id in the WS handler.** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Clean up connection, follow state, party state, and player mute data on disconne** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Set up initial connection state and send initial game state.      Returns:** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Send welcome event to the client.      Returns:         True if successful, Fals** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Load the room instance for the player's current_room_id.      Returns:         (** (1 connections) — `server/realtime/websocket_helpers.py`

## Relationships

- [command commands aliases](command_commands_aliases.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (2 shared connections)
- [room models instance](room_models_instance.md) (1 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_helpers.py`

## Audit Trail

- EXTRACTED: 67 (89%)
- INFERRED: 8 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*