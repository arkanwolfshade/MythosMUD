# .load

> 12 nodes

## Key Concepts

- **.load()** (9 connections) — `server/async_persistence_room_loader.py`
- **._build_room_objects()** (5 connections) — `server/async_persistence_room_loader.py`
- **.__init__()** (4 connections) — `server/async_persistence_room_loader.py`
- **._apply_rooms_to_cache()** (3 connections) — `server/async_persistence_room_loader.py`
- **._handle_room_load_error()** (3 connections) — `server/async_persistence_room_loader.py`
- **._query_rooms_with_exits_async()** (3 connections) — `server/async_persistence_room_loader.py`
- **Room** (3 connections)
- **._log_room_cache_after_load()** (2 connections) — `server/async_persistence_room_loader.py`
- **AsyncSession** (1 connections)
- **BaseException** (1 connections)
- **BoundLogger** (1 connections)
- **Load rooms from PostgreSQL and update the room cache.** (1 connections) — `server/async_persistence_room_loader.py`

## Relationships

- [RoomCacheLoader](RoomCacheLoader.md) (8 shared connections)
- [ProcessedRoomData](ProcessedRoomData.md) (2 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)

## Source Files

- `server/async_persistence_room_loader.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*