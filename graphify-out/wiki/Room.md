# Room

> 173 nodes

## Key Concepts

- **Room** (84 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **InstanceManager** (27 connections) — `server/game/instance_manager.py`
- **test_instance_manager.py** (16 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **instance_manager()** (7 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_room_map_coordinates.py** (7 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **_as_float()** (6 connections) — `server/models/room.py`
- **.__init__()** (6 connections) — `server/models/room.py`
- **_room_from_persistence()** (6 connections) — `server/npc/spawning_request_execution.py`
- **_room()** (6 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **UUID** (6 connections)
- **TestRoomCoordinates** (5 connections) — `server/tests/unit/models/test_room_map_coordinates.py`
- **.__init__()** (5 connections) — `server/game/instance_manager.py`
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **room_cache()** (5 connections) — `server/tests/unit/game/test_instance_manager.py`
- **tutorial_room()** (5 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Room** (5 connections)
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._get_template_rooms()** (4 connections) — `server/game/instance_manager.py`
- **._remap_exits()** (4 connections) — `server/game/instance_manager.py`
- **.get_containers()** (4 connections) — `server/models/room.py`
- *... and 148 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (14 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (3 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (3 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (2 shared connections)
- [protocols.py](protocols.py.md) (2 shared connections)
- [._compute_player_context](_compute_player_context.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)

## Source Files

- `server/game/instance_manager.py`
- `server/models/room.py`
- `server/npc/spawning_request_execution.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/models/test_room_map_coordinates.py`

## Audit Trail

- EXTRACTED: 283 (93%)
- INFERRED: 22 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*