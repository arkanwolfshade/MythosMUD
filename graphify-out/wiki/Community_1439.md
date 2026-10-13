# Community 1439

> 6 nodes

## Key Concepts

- **.async_list_rooms()** (3 connections) — `server/async_persistence.py`
- **.get_room_by_id()** (3 connections) — `server/async_persistence.py`
- **.list_rooms()** (3 connections) — `server/async_persistence.py`
- **Room** (3 connections)
- **List all rooms from the cache. Delegates to RoomRepository. Returns:…** (2 connections) — `server/async_persistence.py`
- **Get a room by ID. Checks instance manager first, then cache. Instanced room IDs…** (1 connections) — `server/async_persistence.py`

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*