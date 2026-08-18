# TestRoomDataCache

> 16 nodes

## Key Concepts

- **TestRoomDataCache** (28 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_clear_cache_nonexistent_room()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_get_cache_found()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_get_cache_stats_with_fresh_and_stale()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_room_data_fresh_exactly_at_threshold()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_merge_room_data_invalid_input()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_merge_room_data_new_field()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_set_cache_overwrites()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test clear_cache handles nonexistent room gracefully.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test get_cache_stats with mix of fresh and stale data.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test suite for RoomDataCache class.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test merge_room_data adds new fields from new data.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test merge_room_data handles invalid input.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test is_room_data_fresh at exactly threshold boundary.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test get_cache returns cached data.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **Test set_cache overwrites existing data.** (1 connections) — `server/tests/unit/services/test_room_data_cache.py`

## Relationships

- [RoomDataCache](RoomDataCache.md) (11 shared connections)
- [.test_clear_cache_all](test_clear_cache_all.md) (1 shared connections)
- [.test_get_cache_stats_empty](test_get_cache_stats_empty.md) (1 shared connections)
- [.test_merge_room_data_newer_timestamp](test_merge_room_data_newer_timestamp.md) (1 shared connections)
- [.test_init_default_threshold](test_init_default_threshold.md) (1 shared connections)
- [.test_merge_room_data_older_timestamp](test_merge_room_data_older_timestamp.md) (1 shared connections)
- [.test_merge_room_data_preserves_old_data](test_merge_room_data_preserves_old_data.md) (1 shared connections)
- [.test_is_newer_data_new_has_timestamp_old_doesnt](test_is_newer_data_new_has_timestamp_old_doesnt.md) (1 shared connections)
- [.test_is_newer_data_both_have_timestamps](test_is_newer_data_both_have_timestamps.md) (1 shared connections)
- [.test_init_custom_threshold](test_init_custom_threshold.md) (1 shared connections)
- [.test_is_room_data_fresh_fresh](test_is_room_data_fresh_fresh.md) (1 shared connections)
- [.test_is_room_data_fresh_stale](test_is_room_data_fresh_stale.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_room_data_cache.py`

## Audit Trail

- EXTRACTED: 41 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*