# AsyncPersistenceLayer

> 199 nodes

## Key Concepts

- **AsyncPersistenceLayer** (168 connections) — `server/async_persistence.py`
- **async_persistence.py** (93 connections) — `server/async_persistence.py`
- **RoomCacheLoader** (26 connections) — `server/async_persistence_room_loader.py`
- **Player** (20 connections)
- **AsyncPersistenceRoomFacade** (16 connections) — `server/async_persistence_room_facade.py`
- **UUID** (15 connections)
- **async_persistence_room_facade.py** (14 connections) — `server/async_persistence_room_facade.py`
- **ProcessedRoomData** (12 connections) — `server/async_persistence_room_loader.py`
- **ExitJsonEntry** (10 connections) — `server/async_persistence_room_loader.py`
- **.load()** (9 connections) — `server/async_persistence_room_loader.py`
- **._process_combined_rows()** (8 connections) — `server/async_persistence_room_loader.py`
- **_AsyncPersistenceRoomFacadeBase** (7 connections) — `server/async_persistence_room_facade.py`
- **RoomLoadResult** (7 connections) — `server/async_persistence_room_loader.py`
- **InstanceRoomLookup** (7 connections) — `server/async_persistence_types.py`
- **._build_room_data_from_row()** (7 connections) — `server/async_persistence_room_loader.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **async_persistence_types.py** (7 connections) — `server/async_persistence_types.py`
- **async_persistence_access.py** (7 connections) — `server/container/async_persistence_access.py`
- **ContainerCreateKwargs** (6 connections) — `server/async_persistence_types.py`
- **PlayerEffectOptions** (6 connections) — `server/async_persistence_types.py`
- **infrastructure/conftest.py** (6 connections) — `server/tests/unit/infrastructure/conftest.py`
- **_ContainerWithPersistence** (5 connections) — `server/container/async_persistence_access.py`
- **.create_container()** (5 connections) — `server/async_persistence.py`
- **._build_room_objects()** (5 connections) — `server/async_persistence_room_loader.py`
- **_ApplicationContainerType** (4 connections) — `server/container/async_persistence_access.py`
- *... and 174 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (33 shared connections)
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) (26 shared connections)
- [EventBus](EventBus.md) (17 shared connections)
- [event_types.py](event_types.py.md) (9 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (8 shared connections)
- [item_instance_persistence.py](item_instance_persistence.py.md) (8 shared connections)
- [Player](Player.md) (7 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (6 shared connections)
- [User](User.md) (6 shared connections)
- [CombatParticipant](CombatParticipant.md) (6 shared connections)
- [test_async_persistence_core.py](test_async_persistence_core.py.md) (5 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (4 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_room_facade.py`
- `server/async_persistence_room_loader.py`
- `server/async_persistence_types.py`
- `server/container/async_persistence_access.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`

## Audit Trail

- EXTRACTED: 476 (91%)
- INFERRED: 49 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*