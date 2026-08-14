# RoomDataCache

> 12 nodes

## Key Concepts

- **RoomDataCache** (40 connections) — `server/services/room_data_cache.py`
- **test_room_data_cache.py** (4 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_newer_data_old_newer_than_new()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_room_data_fresh_custom_threshold()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.clear_cache()** (2 connections) — `server/services/room_data_cache.py`
- **.__init__()** (2 connections) — `server/services/room_data_cache.py`
- **Manages room data caching and freshness validation.** (1 connections) — `server/services/room_data_cache.py`
- **Initialize the room data cache. Args: freshness_threshold_seconds: Threshold in…** (1 connections) — `server/services/room_data_cache.py`
- **Clear room data cache. Args: room_id: Specific room ID to clear, or None to…** (1 connections) — `server/services/room_data_cache.py`
- **Unit tests for room data cache. Tests the RoomDataCache class for caching and…** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test _is_newer_data when old is newer than new.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test is_room_data_fresh with custom threshold parameter.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`

## Relationships

- [TestRoomDataCache](TestRoomDataCache.md) (11 shared connections)
- [Any](Any.md) (6 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [RoomSyncService](RoomSyncService.md) (2 shared connections)
- [.test_clear_cache_all](test_clear_cache_all.md) (1 shared connections)
- [.test_clear_cache_specific_room](test_clear_cache_specific_room.md) (1 shared connections)
- [.test_get_cache_not_found](test_get_cache_not_found.md) (1 shared connections)
- [.test_get_cache_stats_empty](test_get_cache_stats_empty.md) (1 shared connections)
- [.test_init_custom_threshold](test_init_custom_threshold.md) (1 shared connections)
- [.test_init_default_threshold](test_init_default_threshold.md) (1 shared connections)
- [.test_is_newer_data_both_have_timestamps](test_is_newer_data_both_have_timestamps.md) (1 shared connections)
- [.test_is_newer_data_new_has_timestamp_old_doesnt](test_is_newer_data_new_has_timestamp_old_doesnt.md) (1 shared connections)

## Source Files

- `server/services/room_data_cache.py`
- `server/tests/unit/services/test_room_data_cache.py`

## Audit Trail

- EXTRACTED: 47 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*