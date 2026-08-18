# Room

> 97 nodes

## Key Concepts

- **Room** (73 connections) — `server/models/room.py`
- **test_room_class.py** (30 connections) — `server/tests/unit/models/test_room_class.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **UUID** (6 connections)
- **.__init__()** (5 connections) — `server/models/room.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **instance_manager()** (5 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.get_containers()** (4 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **tutorial_room()** (4 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.add_player_silently()** (3 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **.remove_player_silently()** (3 connections) — `server/models/room.py`
- **room_cache()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_room_add_player_silently()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_containers()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_npcs()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_objects()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_occupant_count()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_players()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_has_npc()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 72 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (17 shared connections)
- [NPCDefinition](NPCDefinition.md) (5 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (2 shared connections)
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [._compute_player_context](_compute_player_context.md) (2 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (2 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (1 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 168 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*