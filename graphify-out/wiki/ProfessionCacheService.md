# ProfessionCacheService

> 15 nodes

## Key Concepts

- **ProfessionCacheService** (20 connections) — `server/caching/cache_service.py`
- **TestProfessionCacheService** (7 connections) — `server/tests/unit/caching/test_cache_service.py`
- **fixture** (5 connections)
- **_Profession** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_professions()** (2 connections) — `server/caching/cache_service.py`
- **.test_get_all_professions_hit_and_miss()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_not_found()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_professions()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Service for caching profession data.** (1 connections) — `server/caching/cache_service.py`
- **Initialize the profession cache service. Args: persistence: Persistence layer…** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all profession caches.** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [test_cache_service.py](test_cache_service.py.md) (7 shared connections)
- [Any](Any.md) (3 shared connections)
- [bench_cache_professions.py](bench_cache_professions.py.md) (2 shared connections)
- [CacheService](CacheService.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [NPCCacheService](NPCCacheService.md) (1 shared connections)
- [RoomCacheService](RoomCacheService.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 37 (92%)
- INFERRED: 3 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*