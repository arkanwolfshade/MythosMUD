# Room

> 118 nodes

## Key Concepts

- **Room** (73 connections) — `server/models/room.py`
- **test_room_class.py** (30 connections) — `server/tests/unit/models/test_room_class.py`
- **RoomRepository** (16 connections) — `server/persistence/repositories/room_repository.py`
- **RoomRepositoryProtocol** (11 connections) — `server/persistence/protocols.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **room_repository.py** (8 connections) — `server/persistence/repositories/room_repository.py`
- **test_room_repository.py** (7 connections) — `server/tests/unit/persistence/test_room_repository.py`
- **UUID** (6 connections)
- **.__init__()** (5 connections) — `server/models/room.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **.get_containers()** (4 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **.add_player_silently()** (3 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **.remove_player_silently()** (3 connections) — `server/models/room.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/room_repository.py`
- **test_room_add_player_silently()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_containers()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 93 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (23 shared connections)
- [pytest.md](pytest.md.md) (7 shared connections)
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (4 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (3 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (2 shared connections)
- [InstanceManager](InstanceManager.md) (2 shared connections)
- [._compute_player_context](_compute_player_context.md) (2 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (2 shared connections)
- [_StubPlayerRepo](_StubPlayerRepo.md) (2 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (2 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (1 shared connections)
- [get_session_maker](get_session_maker.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/persistence/protocols.py`
- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/persistence/test_room_repository.py`

## Audit Trail

- EXTRACTED: 176 (82%)
- INFERRED: 39 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*