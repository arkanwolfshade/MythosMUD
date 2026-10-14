# ProfessionCacheService

> 22 nodes

## Key Concepts

- **ProfessionCacheService** (20 connections) — `server/caching/cache_service.py`
- **cache_service.py** (14 connections) — `server/caching/cache_service.py`
- **lru_cache.py** (13 connections) — `server/caching/lru_cache.py`
- **server/caching/__init__.py** (12 connections) — `server/caching/__init__.py`
- **TestProfessionCacheService** (7 connections) — `server/tests/unit/caching/test_cache_service.py`
- **reset_cache_manager()** (5 connections) — `server/caching/lru_cache.py`
- **fixture** (5 connections)
- **_Profession** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_reset_cache_manager()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_professions()** (2 connections) — `server/caching/cache_service.py`
- **.test_get_all_professions_hit_and_miss()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_not_found()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_professions()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Cache service for MythosMUD server. This module provides caching services that…** (1 connections) — `server/caching/cache_service.py`
- **Service for caching profession data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all profession caches.** (1 connections) — `server/caching/cache_service.py`
- **Caching module for MythosMUD server. This module provides comprehensive caching…** (1 connections) — `server/caching/__init__.py`
- **LRU Cache implementation for MythosMUD server. This module provides thread-safe…** (1 connections) — `server/caching/lru_cache.py`
- **Reset the global cache manager (for testing).** (1 connections) — `server/caching/lru_cache.py`

## Relationships

- [NPCCacheService](NPCCacheService.md) (10 shared connections)
- [RoomCacheService](RoomCacheService.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [LRUCache](LRUCache.md) (4 shared connections)
- [Any](Any.md) (3 shared connections)
- [CacheService](CacheService.md) (3 shared connections)
- [bench_cache_professions.py](bench_cache_professions.py.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [cached](cached.md) (2 shared connections)
- [CacheManager](CacheManager.md) (2 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [test_lru_cache.py](test_lru_cache.py.md) (1 shared connections)

## Source Files

- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 72 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*