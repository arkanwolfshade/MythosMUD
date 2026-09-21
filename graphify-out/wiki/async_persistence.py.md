# async_persistence.py

> 118 nodes

## Key Concepts

- **async_persistence.py** (96 connections) — `server/async_persistence.py`
- **RoomCacheLoader** (26 connections) — `server/async_persistence_room_loader.py`
- **async_persistence_room_loader.py** (22 connections) — `server/async_persistence_room_loader.py`
- **ProcessedRoomData** (17 connections) — `server/async_persistence_room_loader.py`
- **AsyncPersistenceRoomFacade** (16 connections) — `server/async_persistence_room_facade.py`
- **async_persistence_room_facade.py** (13 connections) — `server/async_persistence_room_facade.py`
- **profession_service.py** (13 connections) — `server/game/profession_service.py`
- **RoomLoadResult** (12 connections) — `server/async_persistence_room_loader.py`
- **test_async_persistence_room_rest_location.py** (11 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **ExitJsonEntry** (10 connections) — `server/async_persistence_room_loader.py`
- **models/profession.py** (10 connections) — `server/models/profession.py`
- **.load()** (9 connections) — `server/async_persistence_room_loader.py`
- **._process_combined_rows()** (9 connections) — `server/async_persistence_room_loader.py`
- **RoomInitPayload** (8 connections) — `server/async_persistence_room_loader.py`
- **._build_room_data_from_row()** (8 connections) — `server/async_persistence_room_loader.py`
- **_AsyncPersistenceRoomFacadeBase** (7 connections) — `server/async_persistence_room_facade.py`
- **InstanceRoomLookup** (7 connections) — `server/async_persistence_types.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **async_persistence_types.py** (7 connections) — `server/async_persistence_types.py`
- **async_persistence_access.py** (7 connections) — `server/container/async_persistence_access.py`
- **ContainerCreateKwargs** (6 connections) — `server/async_persistence_types.py`
- **PlayerEffectOptions** (6 connections) — `server/async_persistence_types.py`
- **test_build_room_objects_carries_map_coordinates()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_defaults_rest_location_false()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_promotes_rest_location_from_attributes()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- *... and 93 more nodes in this community*

## Relationships

- [Player](Player.md) (32 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [DatabaseError](DatabaseError.md) (7 shared connections)
- [DatabaseManager](DatabaseManager.md) (7 shared connections)
- [item_instance_persistence.py](item_instance_persistence.py.md) (5 shared connections)
- [Profession](Profession.md) (4 shared connections)
- [Room](Room.md) (4 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (4 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [player_effect_repository.py](player_effect_repository.py.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_room_facade.py`
- `server/async_persistence_room_loader.py`
- `server/async_persistence_types.py`
- `server/container/async_persistence_access.py`
- `server/game/profession_service.py`
- `server/models/profession.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`

## Audit Trail

- EXTRACTED: 315 (92%)
- INFERRED: 27 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*