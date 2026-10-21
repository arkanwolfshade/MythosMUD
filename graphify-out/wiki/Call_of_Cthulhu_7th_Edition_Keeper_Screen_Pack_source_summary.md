# Call of Cthulhu 7th Edition Keeper Screen Pack (source summary)

> 6 nodes · cohesion 0.40

## Key Concepts

- **.async_list_rooms()** (3 connections) — `server/async_persistence.py`
- **.get_room_by_id()** (3 connections) — `server/async_persistence.py`
- **.list_rooms()** (3 connections) — `server/async_persistence.py`
- **Room** (3 connections)
- **Get a room by ID. Checks instance manager first, then cache. Instanced room IDs…** (1 connections) — `server/async_persistence.py`
- **List all rooms from the cache. Delegates to RoomRepository. Returns:…** (1 connections) — `server/async_persistence.py`

## Relationships

- [test_party_service.py](test_party_service.py.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*