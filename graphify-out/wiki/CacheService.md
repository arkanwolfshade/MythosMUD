# CacheService

> 14 nodes

## Key Concepts

- **CacheService** (15 connections) — `server/caching/cache_service.py`
- **TestCacheService** (9 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.get_cache_stats()** (3 connections) — `server/caching/cache_service.py`
- **.preload_frequently_accessed_data()** (2 connections) — `server/caching/cache_service.py`
- **.test_get_cache_stats_and_clear()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_with_npc_service()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_without_npc_service()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_frequently_accessed_data()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_handles_profession_failure()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_handles_room_failure()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.clear_all_caches()** (1 connections) — `server/caching/cache_service.py`
- **Main cache service that coordinates all caching operations. This service…** (1 connections) — `server/caching/cache_service.py`
- **Get statistics for all caches. Returns: Dictionary containing cache statistics** (1 connections) — `server/caching/cache_service.py`
- **Preload frequently accessed data into caches. This method loads commonly used…** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [RoomCacheService](RoomCacheService.md) (7 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 25 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*