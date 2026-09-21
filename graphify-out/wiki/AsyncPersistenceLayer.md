# AsyncPersistenceLayer

> 193 nodes

## Key Concepts

- **AsyncPersistenceLayer** (177 connections) — `server/async_persistence.py`
- **RoomCacheLoader** (26 connections) — `server/async_persistence_room_loader.py`
- **async_persistence_room_loader.py** (22 connections) — `server/async_persistence_room_loader.py`
- **Player** (20 connections)
- **ProcessedRoomData** (17 connections) — `server/async_persistence_room_loader.py`
- **AsyncPersistenceRoomFacade** (16 connections) — `server/async_persistence_room_facade.py`
- **UUID** (15 connections)
- **async_persistence_room_facade.py** (13 connections) — `server/async_persistence_room_facade.py`
- **RoomLoadResult** (12 connections) — `server/async_persistence_room_loader.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **test_async_persistence_room_rest_location.py** (11 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **ExitJsonEntry** (10 connections) — `server/async_persistence_room_loader.py`
- **.load()** (9 connections) — `server/async_persistence_room_loader.py`
- **._process_combined_rows()** (9 connections) — `server/async_persistence_room_loader.py`
- **RoomInitPayload** (8 connections) — `server/async_persistence_room_loader.py`
- **._build_room_data_from_row()** (8 connections) — `server/async_persistence_room_loader.py`
- **_AsyncPersistenceRoomFacadeBase** (7 connections) — `server/async_persistence_room_facade.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **async_persistence_access.py** (7 connections) — `server/container/async_persistence_access.py`
- **test_build_room_objects_carries_map_coordinates()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_defaults_rest_location_false()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_promotes_rest_location_from_attributes()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_tolerates_missing_coordinates()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **_ContainerWithPersistence** (5 connections) — `server/container/async_persistence_access.py`
- **.create_container()** (5 connections) — `server/async_persistence.py`
- *... and 168 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (28 shared connections)
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) (25 shared connections)
- [get_logger](get_logger.md) (21 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [User](User.md) (5 shared connections)
- [NPCDefinition](NPCDefinition.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [Profession](Profession.md) (4 shared connections)
- [container_events.py](container_events.py.md) (4 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (4 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (4 shared connections)
- [item_instance_persistence.py](item_instance_persistence.py.md) (4 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_room_facade.py`
- `server/async_persistence_room_loader.py`
- `server/container/async_persistence_access.py`
- `server/container/bundles/core.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`

## Audit Trail

- EXTRACTED: 411 (86%)
- INFERRED: 65 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*