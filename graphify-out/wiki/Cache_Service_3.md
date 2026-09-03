# Cache Service

> 17 nodes

## Key Concepts

- **ProfessionCacheService** (20 connections) — `server/caching/cache_service.py`
- **TestProfessionCacheService** (7 connections) — `server/tests/unit/caching/test_cache_service.py`
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

## Relationships

- [Cache Service](Cache_Service.md) (7 shared connections)
- [Test Cache Service](Test_Cache_Service.md) (5 shared connections)
- [Bench Cache Professions](Bench_Cache_Professions.md) (2 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (2 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Lru Cache](Lru_Cache.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 38 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*