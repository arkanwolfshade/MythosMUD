# Real-Time Architecture Docs

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

- [Player Combat XP](Player_Combat_XP.md) (4 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (3 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (3 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (2 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_helpers.py`

## Audit Trail

- EXTRACTED: 67 (89%)
- INFERRED: 8 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*