# ProfessionCacheService

> 19 nodes

## Key Concepts

- **ProfessionCacheService** (20 connections) — `server/caching/cache_service.py`
- **TestProfessionCacheService** (7 connections) — `server/tests/unit/caching/test_cache_service.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **fixture** (5 connections)
- **_Profession** (4 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.get_all_professions()** (3 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (3 connections) — `server/caching/cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_professions()** (2 connections) — `server/caching/cache_service.py`
- **.test_get_all_professions_hit_and_miss()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_not_found()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_professions()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Service for caching profession data.** (1 connections) — `server/caching/cache_service.py`
- **Get all professions with caching. Returns: List of profession objects** (1 connections) — `server/caching/cache_service.py`
- **Get a specific profession by ID with caching. Args: profession_id: The…** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all profession caches.** (1 connections) — `server/caching/cache_service.py`
- **Create room and profession cache services; set to None on RuntimeError.** (1 connections) — `server/container/bundles/game.py`

## Relationships

- [NPCCacheService](NPCCacheService.md) (7 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [RoomCacheService](RoomCacheService.md) (3 shared connections)
- [Any](Any.md) (3 shared connections)
- [bench_cache_professions.py](bench_cache_professions.py.md) (2 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [CacheService](CacheService.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/container/bundles/game.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 43 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*