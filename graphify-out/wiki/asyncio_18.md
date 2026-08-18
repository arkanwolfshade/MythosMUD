# asyncio

> 13 nodes

## Key Concepts

- **asyncio** (12 connections)
- **test_get_players_batch_with_players()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_other_error_raises()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_success_with_rooms_logs_sample_ids()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_table_not_found()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_query_rooms_with_exits_async_other_error_raises()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_query_rooms_with_exits_async_table_not_found()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test get_players_batch with actual players (UUID conversion).** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _load_room_cache_async logs sample room IDs when rooms are loaded…** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _load_room_cache_async handles table not found error.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _load_room_cache_async raises other errors.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _query_rooms_with_exits_async handles table not found error.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _query_rooms_with_exits_async raises other errors.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Relationships

- [test_async_persistence_room_cache.py](test_async_persistence_room_cache.py.md) (6 shared connections)
- [Player](Player.md) (1 shared connections)
- [test_get_players_batch_empty_list](test_get_players_batch_empty_list.md) (1 shared connections)
- [test_get_professions_no_session](test_get_professions_no_session.md) (1 shared connections)
- [test_get_user_by_username_case_insensitive_no_session](test_get_user_by_username_case_insensitive_no_session.md) (1 shared connections)
- [test_load_room_cache_async_rooms_none](test_load_room_cache_async_rooms_none.md) (1 shared connections)
- [test_load_room_cache_async_warning_logging](test_load_room_cache_async_warning_logging.md) (1 shared connections)
- [test_warmup_room_cache](test_warmup_room_cache.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Audit Trail

- EXTRACTED: 24 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*