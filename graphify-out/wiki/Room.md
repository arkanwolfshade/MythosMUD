# Room

> 100 nodes

## Key Concepts

- **Room** (75 connections) — `server/models/room.py`
- **test_room_class.py** (30 connections) — `server/tests/unit/models/test_room_class.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **UUID** (6 connections)
- **.__init__()** (5 connections) — `server/models/room.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **.get_containers()** (4 connections) — `server/models/room.py`
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
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **.remove_player_silently()** (3 connections) — `server/models/room.py`
- **test_room_add_player_silently()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_containers()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_npcs()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_objects()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_occupant_count()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 75 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (12 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (3 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (2 shared connections)
- [InstanceManager](InstanceManager.md) (2 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (2 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [RoomRepository](RoomRepository.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 170 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*