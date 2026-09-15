# AsyncPersistenceRoomFacade

> 17 nodes

## Key Concepts

- **AsyncPersistenceRoomFacade** (16 connections) — `server/async_persistence_room_facade.py`
- **._parse_exits_json()** (3 connections) — `server/async_persistence_room_facade.py`
- **._process_combined_rows()** (3 connections) — `server/async_persistence_room_facade.py`
- **._process_exits_for_room()** (3 connections) — `server/async_persistence_room_facade.py`
- **._process_room_rows()** (3 connections) — `server/async_persistence_room_facade.py`
- **._query_rooms_with_exits_async()** (3 connections) — `server/async_persistence_room_facade.py`
- **._generate_room_id_from_zone_data()** (2 connections) — `server/async_persistence_room_facade.py`
- **._process_exit_rows()** (2 connections) — `server/async_persistence_room_facade.py`
- **AsyncSession** (1 connections)
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence_room_facade.py`
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence_room_facade.py`
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence_room_facade.py`
- **Mixin: lazy room-cache load and loader delegation for unit tests.** (1 connections) — `server/async_persistence_room_facade.py`
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence_room_facade.py`
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence_room_facade.py`
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence_room_facade.py`
- **Delegate to room loader; exposed for unit tests.** (1 connections) — `server/async_persistence_room_facade.py`

## Relationships

- [ProcessedRoomData](ProcessedRoomData.md) (5 shared connections)
- [async_persistence_room_loader.py](async_persistence_room_loader.py.md) (4 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [_AsyncPersistenceRoomFacadeBase](_AsyncPersistenceRoomFacadeBase.md) (1 shared connections)

## Source Files

- `server/async_persistence_room_facade.py`

## Audit Trail

- EXTRACTED: 25 (89%)
- INFERRED: 3 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*