# Any

> 13 nodes

## Key Concepts

- **Any** (6 connections)
- **._is_newer_data()** (4 connections) — `server/services/room_data_cache.py`
- **.merge_room_data()** (4 connections) — `server/services/room_data_cache.py`
- **.get_cache()** (3 connections) — `server/services/room_data_cache.py`
- **.get_cache_stats()** (3 connections) — `server/services/room_data_cache.py`
- **.is_room_data_fresh()** (3 connections) — `server/services/room_data_cache.py`
- **.set_cache()** (3 connections) — `server/services/room_data_cache.py`
- **Get statistics about the room data cache. Args: is_room_data_fresh_func:…** (1 connections) — `server/services/room_data_cache.py`
- **Merge room data with proper conflict resolution. Args: old_data: Existing room…** (1 connections) — `server/services/room_data_cache.py`
- **Check if new data is newer than old data for a specific key. Args: old_data:…** (1 connections) — `server/services/room_data_cache.py`
- **Check if room data is fresh enough to use. Args: room_data: Room data to check…** (1 connections) — `server/services/room_data_cache.py`
- **Get room data from cache. Args: room_id: Room ID to retrieve Returns: Dict[str,…** (1 connections) — `server/services/room_data_cache.py`
- **Store room data in cache. Args: room_id: Room ID to store room_data: Room data…** (1 connections) — `server/services/room_data_cache.py`

## Relationships

- [RoomDataCache](RoomDataCache.md) (6 shared connections)

## Source Files

- `server/services/room_data_cache.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*