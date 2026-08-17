# test_cache_service.py

> 18 nodes

## Key Concepts

- **test_cache_service.py** (22 connections) — `server/tests/unit/caching/test_cache_service.py`
- **ProfessionCacheService** (20 connections) — `server/caching/cache_service.py`
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
- **Service for caching profession data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all profession caches.** (1 connections) — `server/caching/cache_service.py`
- **Reset the global cache manager (for testing).** (1 connections) — `server/caching/lru_cache.py`
- **Unit tests for server.caching.cache_service.** (1 connections) — `server/tests/unit/caching/test_cache_service.py`

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [NPCCacheService](NPCCacheService.md) (5 shared connections)
- [CacheService](CacheService.md) (4 shared connections)
- [RoomCacheService](RoomCacheService.md) (4 shared connections)
- [Any](Any.md) (3 shared connections)
- [cached](cached.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [bench_cache_professions.py](bench_cache_professions.py.md) (2 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 56 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*