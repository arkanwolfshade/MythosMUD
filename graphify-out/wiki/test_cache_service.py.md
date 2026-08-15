# test_cache_service.py

> 20 nodes

## Key Concepts

- **test_cache_service.py** (21 connections) — `server/tests/unit/caching/test_cache_service.py`
- **ProfessionCacheService** (20 connections) — `server/caching/cache_service.py`
- **TestProfessionCacheService** (7 connections) — `server/tests/unit/caching/test_cache_service.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
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
- **Service for caching profession data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all profession caches.** (1 connections) — `server/caching/cache_service.py`
- **Reset the global cache manager (for testing).** (1 connections) — `server/caching/lru_cache.py`
- **Create room and profession cache services; set to None on RuntimeError.** (1 connections) — `server/container/bundles/game.py`
- **Unit tests for server.caching.cache_service.** (1 connections) — `server/tests/unit/caching/test_cache_service.py`

## Relationships

- [RoomCacheService](RoomCacheService.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [NPCCacheService](NPCCacheService.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [Any](Any.md) (3 shared connections)
- [CacheService](CacheService.md) (3 shared connections)
- [cached](cached.md) (3 shared connections)
- [bench_cache_professions.py](bench_cache_professions.py.md) (2 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/container/bundles/game.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 60 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*