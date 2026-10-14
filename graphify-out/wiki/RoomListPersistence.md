# RoomListPersistence

> 11 nodes

## Key Concepts

- **RoomListPersistence** (7 connections) — `server/services/room_item_seeder.py`
- **RoomDropSink** (5 connections) — `server/services/room_item_seeder.py`
- **.add_room_drop()** (2 connections) — `server/services/room_item_seeder.py`
- **.list_rooms()** (2 connections) — `server/services/room_item_seeder.py`
- **.warmup_room_cache()** (2 connections) — `server/services/room_item_seeder.py`
- **Protocol** (2 connections)
- **Room** (2 connections)
- **The slice of the room manager the seeder needs.** (1 connections) — `server/services/room_item_seeder.py`
- **Add a stack to a room's floor drops.** (1 connections) — `server/services/room_item_seeder.py`
- **The slice of AsyncPersistenceLayer the startup hook needs.** (1 connections) — `server/services/room_item_seeder.py`
- **Load the room cache if it is not loaded yet.** (1 connections) — `server/services/room_item_seeder.py`

## Relationships

- [ItemFactory](ItemFactory.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)

## Source Files

- `server/services/room_item_seeder.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*