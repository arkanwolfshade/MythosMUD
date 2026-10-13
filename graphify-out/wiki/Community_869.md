# Community 869

> 18 nodes

## Key Concepts

- **CacheService** (15 connections) — `server/caching/cache_service.py`
- **TestCacheService** (9 connections) — `server/tests/unit/caching/test_cache_service.py`
- **fixture** (5 connections)
- **_Profession** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.get_cache_stats()** (3 connections) — `server/caching/cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
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

- [Community 750](Community_750.md) (6 shared connections)
- [Community 522](Community_522.md) (4 shared connections)
- [Community 896](Community_896.md) (1 shared connections)
- [Community 695](Community_695.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 35 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*