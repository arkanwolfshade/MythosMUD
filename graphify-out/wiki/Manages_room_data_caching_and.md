# Manages room data caching and

> 60 nodes

## Key Concepts

- **RoomDataCache** (40 connections) — `server/services/room_data_cache.py`
- **TestRoomDataCache** (28 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **test_room_data_cache.py** (4 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_init_default_threshold()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_init_custom_threshold()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_room_data_fresh_fresh()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_room_data_fresh_stale()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_room_data_fresh_no_timestamp()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_room_data_fresh_custom_threshold()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_room_data_fresh_exactly_at_threshold()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_is_room_data_fresh_invalid_input()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_get_cache_not_found()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_get_cache_found()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_set_cache()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_set_cache_overwrites()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_clear_cache_specific_room()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_clear_cache_all()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_clear_cache_nonexistent_room()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_get_cache_stats_empty()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_get_cache_stats_with_fresh_and_stale()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_merge_room_data_newer_timestamp()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_merge_room_data_older_timestamp()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_merge_room_data_new_field()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_merge_room_data_preserves_old_data()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- **.test_merge_room_data_invalid_input()** (3 connections) — `server/tests/unit/services/test_room_data_cache.py`
- *... and 35 more nodes in this community*

## Relationships

- [Any](Any.md) (7 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [combat taunt](combat_taunt.md) (1 shared connections)

## Source Files

- `server/services/room_data_cache.py`
- `server/tests/unit/services/test_room_data_cache.py`

## Audit Trail

- EXTRACTED: 178 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*