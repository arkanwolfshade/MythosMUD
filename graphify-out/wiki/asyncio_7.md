# asyncio

> 11 nodes

## Key Concepts

- **asyncio** (6 connections)
- **test_ensure_room_cache_loaded_database_error()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_already_loaded()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_concurrent_load()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_os_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **test_ensure_room_cache_loaded_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _ensure_room_cache_loaded returns early when cache is already loaded.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _ensure_room_cache_loaded handles concurrent load scenario (double-check…** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _ensure_room_cache_loaded handles DatabaseError gracefully.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _ensure_room_cache_loaded handles OSError gracefully.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **Test _ensure_room_cache_loaded handles RuntimeError gracefully.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Relationships

- [test_async_persistence_room_loading.py](test_async_persistence_room_loading.py.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Audit Trail

- EXTRACTED: 16 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*