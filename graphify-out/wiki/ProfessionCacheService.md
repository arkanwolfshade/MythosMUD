# ProfessionCacheService

> 23 nodes

## Key Concepts

- **ProfessionCacheService** (29 connections) — `server/caching/cache_service.py`
- **TestProfessionCacheService** (10 connections) — `server/tests/unit/caching/test_cache_service.py`
- **_Profession** (8 connections) — `server/tests/unit/caching/test_cache_service.py`
- **bench_cache_professions.py** (7 connections) — `scripts/bench_cache_professions.py`
- **_FakePersistence** (5 connections) — `scripts/bench_cache_professions.py`
- **bench_profession_cache()** (5 connections) — `scripts/bench_cache_professions.py`
- **fixture** (5 connections)
- **_get_empty_dict()** (4 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (3 connections) — `scripts/bench_cache_professions.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Any** (3 connections)
- **main()** (2 connections) — `scripts/bench_cache_professions.py`
- **.invalidate_professions()** (2 connections) — `server/caching/cache_service.py`
- **.test_get_all_professions_hit_and_miss()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_not_found()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_professions()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_professions.py`
- **Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit…** (1 connections) — `scripts/bench_cache_professions.py`
- **Helper function to return empty dict for mock methods.** (1 connections) — `scripts/bench_cache_professions.py`
- **Service for caching profession data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all profession caches.** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [get_cache_manager](get_cache_manager.md) (7 shared connections)
- [NPCCacheService](NPCCacheService.md) (6 shared connections)
- [CacheService](CacheService.md) (5 shared connections)
- [RoomCacheService](RoomCacheService.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [Any](Any.md) (3 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_professions.py`
- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 48 (72%)
- INFERRED: 19 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*