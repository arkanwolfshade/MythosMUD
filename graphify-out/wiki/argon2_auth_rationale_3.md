# argon2 auth rationale

> 20 nodes

## Key Concepts

- **RoomRepository** (17 connections) — `server/persistence/repositories/room_repository.py`
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
- **Room repository for async persistence operations.  This module provides async da** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Repository for room persistence operations.      Handles room caching and retrie** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Initialize the room repository.          Args:             room_cache: Shared ro** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Get a room by ID from cache.          Args:             room_id: Room identifier** (1 connections) — `server/persistence/repositories/room_repository.py`
- **List all cached rooms.          Returns:             list[Room]: List of all roo** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Save a room to the cache.          Args:             room: Room object to save** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Save multiple rooms to the cache.          Args:             rooms: List of room** (1 connections) — `server/persistence/repositories/room_repository.py`
- **Unit tests for RoomRepository.** (1 connections) — `server/tests/unit/persistence/test_room_repository.py`

## Relationships

- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [room models instance](room_models_instance.md) (2 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [command admin setlucidity](command_admin_setlucidity.md) (1 shared connections)
- [persistence container item](persistence_container_item.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/persistence/test_room_repository.py`

## Audit Trail

- EXTRACTED: 58 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*