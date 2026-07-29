# websocket handler connection

> 16 nodes

## Key Concepts

- **websocket_handler_connection.py** (17 connections) — `server/realtime/websocket_handler_connection.py`
- **cleanup_websocket_connection()** (7 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (7 connections) — `server/realtime/websocket_handler_connection.py`
- **PlayerDisconnectService** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **AsyncPersistenceRoomLookup** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (5 connections)
- **.on_player_disconnect()** (3 connections) — `server/realtime/websocket_handler_connection.py`
- **Protocol** (2 connections)
- **WebSocket** (2 connections)
- **WebSocket connection lifecycle: setup, welcome, and cleanup on disconnect.  Extr** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Notify subsystems when a WebSocket session ends for a player.** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Narrow persistence surface for loading ``Room`` by id in the WS handler.** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Clean up connection, follow state, party state, and player mute data on disconne** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Set up initial connection state and send initial game state.      Returns:** (1 connections) — `server/realtime/websocket_handler_connection.py`
- **Send welcome event to the client.      Returns:         True if successful, Fals** (1 connections) — `server/realtime/websocket_handler_connection.py`

## Relationships

- [. init ()](_init_%28%29.md) (4 shared connections)
- [Player](Player.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [.shutdown()](shutdown%28%29.md) (2 shared connections)
- [spawn defaults](spawn_defaults.md) (2 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [.get room by id()](get_room_by_id%28%29.md) (2 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_connection.py`

## Audit Trail

- EXTRACTED: 61 (91%)
- INFERRED: 6 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*