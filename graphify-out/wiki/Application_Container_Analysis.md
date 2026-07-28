# Application Container Analysis

> 13 nodes · cohesion 0.17

## Key Concepts

- **Any** (6 connections)
- **._is_newer_data()** (4 connections) — `server/services/room_data_cache.py`
- **.merge_room_data()** (4 connections) — `server/services/room_data_cache.py`
- **.get_cache()** (3 connections) — `server/services/room_data_cache.py`
- **.get_cache_stats()** (3 connections) — `server/services/room_data_cache.py`
- **.is_room_data_fresh()** (3 connections) — `server/services/room_data_cache.py`
- **.set_cache()** (3 connections) — `server/services/room_data_cache.py`
- **Get statistics about the room data cache.          Args:             is_room_dat** (1 connections) — `server/services/room_data_cache.py`
- **Merge room data with proper conflict resolution.          Args:             old_** (1 connections) — `server/services/room_data_cache.py`
- **Check if new data is newer than old data for a specific key.          Args:** (1 connections) — `server/services/room_data_cache.py`
- **Check if room data is fresh enough to use.          Args:             room_data:** (1 connections) — `server/services/room_data_cache.py`
- **Get room data from cache.          Args:             room_id: Room ID to retriev** (1 connections) — `server/services/room_data_cache.py`
- **Store room data in cache.          Args:             room_id: Room ID to store** (1 connections) — `server/services/room_data_cache.py`

## Relationships

- [Inventory Command Factories](Inventory_Command_Factories.md) (6 shared connections)

## Source Files

- `server/services/room_data_cache.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*