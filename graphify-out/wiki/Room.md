# Room

> 96 nodes

## Key Concepts

- **Room** (73 connections) — `server/models/room.py`
- **test_room_class.py** (30 connections) — `server/tests/unit/models/test_room_class.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **UUID** (6 connections)
- **.player_entered()** (5 connections) — `server/models/room.py`
- **.get_containers()** (4 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **.add_player_silently()** (3 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **.remove_player_silently()** (3 connections) — `server/models/room.py`
- **test_room_add_player_silently()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_containers()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_npcs()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_objects()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_occupant_count()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_players()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_has_npc()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 71 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (2 shared connections)
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [InstanceManager](InstanceManager.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (2 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [database.py](database.py.md) (1 shared connections)
- [PlayerRepository](PlayerRepository.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 137 (80%)
- INFERRED: 34 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*