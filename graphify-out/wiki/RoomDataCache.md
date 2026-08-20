# RoomDataCache

> 73 nodes

## Key Concepts

- **RoomDataCache** (40 connections) — `server/services/room_data_cache.py`
- **TestRoomDataCache** (28 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Any** (6 connections)
- **._is_newer_data()** (4 connections) — `server/services/room_data_cache.py`
- **.merge_room_data()** (4 connections) — `server/services/room_data_cache.py`
- **test_room_data_cache.py** (4 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.get_cache()** (3 connections) — `server/services/room_data_cache.py`
- **.get_cache_stats()** (3 connections) — `server/services/room_data_cache.py`
- **.is_room_data_fresh()** (3 connections) — `server/services/room_data_cache.py`
- **.set_cache()** (3 connections) — `server/services/room_data_cache.py`
- **.test_clear_cache_all()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_clear_cache_nonexistent_room()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_clear_cache_specific_room()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_get_cache_found()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_get_cache_not_found()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_get_cache_stats_empty()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_get_cache_stats_with_fresh_and_stale()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_init_custom_threshold()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_init_default_threshold()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_newer_data_both_have_timestamps()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_newer_data_new_has_timestamp_old_doesnt()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_newer_data_old_newer_than_new()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_room_data_fresh_custom_threshold()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_room_data_fresh_exactly_at_threshold()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_room_data_fresh_fresh()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- *... and 48 more nodes in this community*

## Relationships

- [test_room_sync_service.py](test_room_sync_service.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/services/room_data_cache.py`
- `server/tests/unit/services/test_room_data_cache.py`

## Audit Trail

- EXTRACTED: 107 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*