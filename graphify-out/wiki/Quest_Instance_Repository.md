# Quest Instance Repository

> 14 nodes

## Key Concepts

- **RoomRepository** (12 connections) — `server/persistence/repositories/room_repository.py`
- **room_repository.py** (7 connections) — `server/persistence/repositories/room_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/room_repository.py`
- **.get_room_by_id()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.list_rooms()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.save_room()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.save_rooms()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **Room repository for async persistence operations.  This module provides async da** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Repository for room persistence operations.      Handles room caching and retrie** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Initialize the room repository.          Args:             room_cache: Shared ro** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Get a room by ID from cache.          Args:             room_id: Room identifier** (1 connections) — `server/persistence/repositories/room_repository.py`
- **List all cached rooms.          Returns:             list[Room]: List of all roo** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Save a room to the cache.          Args:             room: Room object to save** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Save multiple rooms to the cache.          Args:             rooms: List of room** (1 connections) — `server/persistence/repositories/room_repository.py`

## Relationships

- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (2 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)
- [Draggable Panel UI](Draggable_Panel_UI.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/room_repository.py`

## Audit Trail

- EXTRACTED: 36 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*