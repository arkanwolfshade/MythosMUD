# ProcessedRoomData

> 15 nodes

## Key Concepts

- **ProcessedRoomData** (15 connections) — `server/async_persistence_room_loader.py`
- **RoomLoadResult** (10 connections) — `server/async_persistence_room_loader.py`
- **test_async_persistence_room_rest_location.py** (9 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **RoomInitPayload** (6 connections) — `server/async_persistence_room_loader.py`
- **test_build_room_objects_defaults_rest_location_false()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_promotes_rest_location_from_attributes()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **._build_room_objects()** (4 connections) — `server/async_persistence_room_facade.py`
- **TypedDict** (4 connections)
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence_room_facade.py`
- **Intermediate room row after zone/id normalization.** (1 connections) — `server/async_persistence_room_loader.py`
- **Mutable container passed through room object construction.** (1 connections) — `server/async_persistence_room_loader.py`
- **Payload passed to Room.__init__ during cache load.** (1 connections) — `server/async_persistence_room_loader.py`
- **Unit tests for _build_room_objects' rest_location promotion (#297). Split out…** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **#297: rest_location lives in the JSONB attributes column (DML), not a top-level…** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **A room with no rest_location attribute must not silently become a rest location.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`

## Relationships

- [async_persistence_room_loader.py](async_persistence_room_loader.py.md) (7 shared connections)
- [AsyncPersistenceRoomFacade](AsyncPersistenceRoomFacade.md) (5 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [.load](load.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/async_persistence_room_facade.py`
- `server/async_persistence_room_loader.py`
- `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`

## Audit Trail

- EXTRACTED: 34 (77%)
- INFERRED: 10 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*