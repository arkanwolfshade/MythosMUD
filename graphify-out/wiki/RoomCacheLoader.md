# RoomCacheLoader

> 76 nodes

## Key Concepts

- **RoomCacheLoader** (26 connections) — `server/async_persistence_room_loader.py`
- **ProcessedRoomData** (21 connections) — `server/async_persistence_room_loader.py`
- **AsyncPersistenceRoomFacade** (16 connections) — `server/async_persistence_room_facade.py`
- **RoomLoadResult** (13 connections) — `server/async_persistence_room_loader.py`
- **test_async_persistence_room_rest_location.py** (12 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **ExitJsonEntry** (10 connections) — `server/async_persistence_room_loader.py`
- **RoomInitPayload** (9 connections) — `server/async_persistence_room_loader.py`
- **.load()** (9 connections) — `server/async_persistence_room_loader.py`
- **._process_combined_rows()** (9 connections) — `server/async_persistence_room_loader.py`
- **._build_room_data_from_row()** (8 connections) — `server/async_persistence_room_loader.py`
- **_AsyncPersistenceRoomFacadeBase** (7 connections) — `server/async_persistence_room_facade.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **test_build_room_objects_carries_display_names()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_carries_map_coordinates()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_defaults_rest_location_false()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_promotes_rest_location_from_attributes()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_tolerates_missing_coordinates()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **._build_room_objects()** (5 connections) — `server/async_persistence_room_loader.py`
- **._build_room_objects()** (4 connections) — `server/async_persistence_room_facade.py`
- **.__init__()** (4 connections) — `server/async_persistence_room_loader.py`
- **._parse_exits_json()** (4 connections) — `server/async_persistence_room_loader.py`
- **._parse_zone_parts()** (4 connections) — `server/async_persistence_room_loader.py`
- **._process_exit_rows()** (4 connections) — `server/async_persistence_room_loader.py`
- **._process_exits_for_room()** (4 connections) — `server/async_persistence_room_loader.py`
- **_row_optional_float()** (4 connections) — `server/async_persistence_room_loader.py`
- *... and 51 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (23 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (8 shared connections)
- [test_async_persistence_room_loading.py](test_async_persistence_room_loading.py.md) (1 shared connections)
- [test_build_room_objects_with_dict_attributes](test_build_room_objects_with_dict_attributes.md) (1 shared connections)
- [test_build_room_objects_without_environment_in_attributes](test_build_room_objects_without_environment_in_attributes.md) (1 shared connections)
- [session](session.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/async_persistence_room_facade.py`
- `server/async_persistence_room_loader.py`
- `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`

## Audit Trail

- EXTRACTED: 141 (83%)
- INFERRED: 29 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*