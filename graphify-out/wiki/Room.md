# Room

> 225 nodes

## Key Concepts

- **Room** (73 connections) — `server/models/room.py`
- **NPCMovementIntegration** (50 connections) — `server/npc/movement_integration.py`
- **models/room.py** (32 connections) — `server/models/room.py`
- **test_room_class.py** (30 connections) — `server/tests/unit/models/test_room_class.py`
- **test_movement_integration.py** (30 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **server/events/__init__.py** (25 connections) — `server/events/__init__.py`
- **movement_integration.py** (20 connections) — `server/npc/movement_integration.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **idle_movement.py** (18 connections) — `server/npc/idle_movement.py`
- **test_instance_manager.py** (16 connections) — `server/tests/unit/game/test_instance_manager.py`
- **instance_manager.py** (13 connections) — `server/game/instance_manager.py`
- **ObjectAddedToRoom** (8 connections) — `server/events/event_types.py`
- **ObjectRemovedFromRoom** (8 connections) — `server/events/event_types.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **.move_npc_to_room()** (7 connections) — `server/npc/movement_integration.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **UUID** (6 connections)
- **.__init__()** (5 connections) — `server/game/instance_manager.py`
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **.__init__()** (5 connections) — `server/models/room.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **.__init__()** (5 connections) — `server/npc/idle_movement.py`
- **.__init__()** (5 connections) — `server/npc/movement_integration.py`
- **instance_manager()** (5 connections) — `server/tests/unit/game/test_instance_manager.py`
- *... and 200 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (18 shared connections)
- [time.py](time.py.md) (15 shared connections)
- [EventBus](EventBus.md) (12 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [event_types.py](event_types.py.md) (9 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (9 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (6 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (5 shared connections)
- [NPCBase](NPCBase.md) (5 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (5 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)

## Source Files

- `server/events/__init__.py`
- `server/events/event_types.py`
- `server/game/instance_manager.py`
- `server/models/room.py`
- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/npc/test_movement_integration.py`

## Audit Trail

- EXTRACTED: 447 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*