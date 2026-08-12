# Room

> 118 nodes

## Key Concepts

- **Room** (74 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **websocket_handler_connection.py** (17 connections) — `server/realtime/websocket_handler_connection.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **._notify_room_and_threads()** (6 connections) — `server/npc/lifecycle_manager.py`
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (6 connections)
- **AsyncPersistenceRoomLookup** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **PlayerDisconnectService** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **.get_containers()** (5 connections) — `server/models/room.py`
- **.__init__()** (5 connections) — `server/models/room.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **cleanup_websocket_connection()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (5 connections)
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.npc_entered()** (4 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **.add_player_silently()** (3 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- *... and 93 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (25 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [InstanceManager](InstanceManager.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (2 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (2 shared connections)
- [bundles/game.py](bundles-game.py.md) (2 shared connections)

## Source Files

- `server/models/room.py`
- `server/npc/lifecycle_manager.py`
- `server/realtime/websocket_handler_connection.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 366 (96%)
- INFERRED: 16 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*