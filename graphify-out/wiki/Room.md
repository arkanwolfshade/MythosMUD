# Room

> 149 nodes

## Key Concepts

- **Room** (73 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **test_instance_manager.py** (15 connections) — `server/tests/unit/game/test_instance_manager.py`
- **RoomRepositoryProtocol** (11 connections) — `server/persistence/protocols.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **UUID** (6 connections)
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **.get_containers()** (5 connections) — `server/models/room.py`
- **.__init__()** (5 connections) — `server/models/room.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **instance_manager()** (5 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Room** (5 connections)
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._get_template_rooms()** (4 connections) — `server/game/instance_manager.py`
- **._remap_exits()** (4 connections) — `server/game/instance_manager.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **tutorial_room()** (4 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.get_instance()** (3 connections) — `server/game/instance_manager.py`
- **.get_room_by_id()** (3 connections) — `server/game/instance_manager.py`
- *... and 124 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (27 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [._compute_player_context](_compute_player_context.md) (2 shared connections)
- [test_protocols.py](test_protocols.py.md) (2 shared connections)
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (2 shared connections)
- [.get_room_by_id](get_room_by_id.md) (2 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (2 shared connections)

## Source Files

- `server/game/instance_manager.py`
- `server/models/room.py`
- `server/persistence/protocols.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 217 (85%)
- INFERRED: 39 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*