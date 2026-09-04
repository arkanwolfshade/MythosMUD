# Room Repository

> 20 nodes

## Key Concepts

- **RoomRepository** (14 connections) — `server/persistence/repositories/room_repository.py`
- **room_repository.py** (8 connections) — `server/persistence/repositories/room_repository.py`
- **test_room_repository.py** (7 connections) — `server/tests/unit/persistence/test_room_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/room_repository.py`
- **.get_room_by_id()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.list_rooms()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.save_room()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.save_rooms()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **test_get_room_by_id_from_cache()** (2 connections) — `server/tests/unit/persistence/test_room_repository.py`
- **test_list_rooms_returns_cache_values()** (2 connections) — `server/tests/unit/persistence/test_room_repository.py`
- **test_save_room_updates_cache()** (2 connections) — `server/tests/unit/persistence/test_room_repository.py`
- **test_save_rooms_updates_cache()** (2 connections) — `server/tests/unit/persistence/test_room_repository.py`
- **Room repository for async persistence operations. This module provides async…** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Repository for room persistence operations. Handles room caching and retrieval.…** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Initialize the room repository. Args: room_cache: Shared room cache dictionary** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Get a room by ID from cache. Args: room_id: Room identifier Returns: Room |…** (1 connections) — `server/persistence/repositories/room_repository.py`
- **List all cached rooms. Returns: list[Room]: List of all rooms Note: This is…** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Save a room to the cache. Args: room: Room object to save Note: Rooms are…** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Save multiple rooms to the cache. Args: rooms: List of room objects to save…** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Unit tests for RoomRepository.** (1 connections) — `server/tests/unit/persistence/test_room_repository.py`

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Player Skill Repository](Player_Skill_Repository.md) (2 shared connections)
- [Test Container Persistence Extended Crud](Test_Container_Persistence_Extended_Crud.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/persistence/test_room_repository.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*