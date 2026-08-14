# Room

> 141 nodes

## Key Concepts

- **Room** (74 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **RoomRepository** (17 connections) — `server/persistence/repositories/room_repository.py`
- **test_instance_manager.py** (15 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **room_repository.py** (8 connections) — `server/persistence/repositories/room_repository.py`
- **test_room_repository.py** (7 connections) — `server/tests/unit/persistence/test_room_repository.py`
- **UUID** (6 connections)
- **.get_containers()** (5 connections) — `server/models/room.py`
- **.__init__()** (5 connections) — `server/models/room.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **instance_manager()** (5 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **tutorial_room()** (4 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.add_player_silently()** (3 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **.remove_player_silently()** (3 connections) — `server/models/room.py`
- *... and 116 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [event_types.py](event_types.py.md) (11 shared connections)
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (2 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (1 shared connections)
- [movement_helpers.py](movement_helpers.py.md) (1 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/persistence/test_room_repository.py`

## Audit Trail

- EXTRACTED: 227 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*