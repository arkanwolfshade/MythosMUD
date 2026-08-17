# server tests unit infrastructure test

> 13 nodes

## Key Concepts

- **asyncio** (12 connections)
- **test_get_players_batch_empty_list()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_get_user_by_username_case_insensitive_no_session()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_other_error_raises()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_rooms_none()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_success_with_rooms_logs_sample_ids()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **test_load_room_cache_async_warning_logging()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test get_user_by_username_case_insensitive when no session is yielded.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test get_players_batch with empty list.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _load_room_cache_async handles case when rooms is None.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _load_room_cache_async logs warning when table not found.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _load_room_cache_async logs sample room IDs when rooms are loaded…** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test _load_room_cache_async raises other errors.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Relationships

- [server tests unit infrastructure test](server_tests_unit_infrastructure_test.md) (12 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*