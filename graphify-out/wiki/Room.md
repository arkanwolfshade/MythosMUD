# Room

> 204 nodes

## Key Concepts

- **Room** (82 connections) — `server/models/room.py`
- **models/room.py** (39 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **RoomCacheLoader** (26 connections) — `server/async_persistence_room_loader.py`
- **async_persistence_room_loader.py** (21 connections) — `server/async_persistence_room_loader.py`
- **movement_integration.py** (20 connections) — `server/npc/movement_integration.py`
- **AsyncPersistenceRoomFacade** (16 connections) — `server/async_persistence_room_facade.py`
- **test_instance_manager.py** (16 connections) — `server/tests/unit/game/test_instance_manager.py`
- **ProcessedRoomData** (15 connections) — `server/async_persistence_room_loader.py`
- **async_persistence_room_facade.py** (13 connections) — `server/async_persistence_room_facade.py`
- **instance_manager.py** (13 connections) — `server/game/instance_manager.py`
- **ExitJsonEntry** (10 connections) — `server/async_persistence_room_loader.py`
- **RoomLoadResult** (10 connections) — `server/async_persistence_room_loader.py`
- **.load()** (9 connections) — `server/async_persistence_room_loader.py`
- **test_async_persistence_room_rest_location.py** (9 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **._process_combined_rows()** (8 connections) — `server/async_persistence_room_loader.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **_AsyncPersistenceRoomFacadeBase** (7 connections) — `server/async_persistence_room_facade.py`
- **._build_room_data_from_row()** (7 connections) — `server/async_persistence_room_loader.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **instance_manager()** (7 connections) — `server/tests/unit/game/test_instance_manager.py`
- **async_persistence_types.py** (7 connections) — `server/async_persistence_types.py`
- **RoomInitPayload** (6 connections) — `server/async_persistence_room_loader.py`
- **test_build_room_objects_defaults_rest_location_false()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_promotes_rest_location_from_attributes()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- *... and 179 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (18 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [InstanceManager](InstanceManager.md) (13 shared connections)
- [RoomService](RoomService.md) (9 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (9 shared connections)
- [build_event](build_event.md) (6 shared connections)
- [EventBus](EventBus.md) (6 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (5 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (5 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (4 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (4 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (3 shared connections)

## Source Files

- `server/async_persistence_room_facade.py`
- `server/async_persistence_room_loader.py`
- `server/async_persistence_types.py`
- `server/game/instance_manager.py`
- `server/models/room.py`
- `server/npc/movement_integration.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 416 (92%)
- INFERRED: 35 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*