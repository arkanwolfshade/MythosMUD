# Websocket Handler Connection

> 20 nodes

## Key Concepts

- **websocket_handler_connection.py** (19 connections) — `server/realtime/websocket_handler_connection.py`
- **send_welcome_event()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (5 connections)
- **AsyncPersistenceRoomLookup** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **PlayerDisconnectService** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **PlayerMuteCleanup** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **cleanup_websocket_connection()** (4 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (4 connections) — `server/realtime/websocket_handler_connection.py`
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

- [Test Envelope](Test_Envelope.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)
- [Connection Manager](Connection_Manager.md) (1 shared connections)
- [Test Websocket Helpers](Test_Websocket_Helpers.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_connection.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*