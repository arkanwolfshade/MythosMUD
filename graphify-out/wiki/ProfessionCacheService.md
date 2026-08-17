# ProfessionCacheService

> 32 nodes

## Key Concepts

- **ProfessionCacheService** (20 connections) — `server/caching/cache_service.py`
- **TestProfessionCacheService** (7 connections) — `server/tests/unit/caching/test_cache_service.py`
- **bench_cache_professions.py** (7 connections) — `scripts/bench_cache_professions.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **bench_profession_cache()** (5 connections) — `scripts/bench_cache_professions.py`
- **._build_prototype_payload()** (5 connections) — `server/container/bundles/game.py`
- **_FakePersistence** (4 connections) — `scripts/bench_cache_professions.py`
- **_get_empty_dict()** (4 connections) — `scripts/bench_cache_professions.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **._wire_user_manager_after_init()** (4 connections) — `server/container/bundles/game.py`
- **.get_all_professions()** (3 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (3 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (3 connections) — `server/caching/cache_service.py`
- **.test_get_profession_by_id_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Any** (3 connections)
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
- *... and 7 more nodes in this community*

## Relationships

- [RoomCacheService](RoomCacheService.md) (9 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (9 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [._initialize_item_services](_initialize_item_services.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_professions.py`
- `server/caching/cache_service.py`
- `server/container/bundles/game.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 59 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*