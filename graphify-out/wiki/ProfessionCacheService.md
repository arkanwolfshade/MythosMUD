# ProfessionCacheService

> 14 nodes

## Key Concepts

- **ProfessionCacheService** (15 connections) — `server/caching/cache_service.py`
- **bench_cache_professions.py** (7 connections) — `scripts/bench_cache_professions.py`
- **_FakePersistence** (5 connections) — `scripts/bench_cache_professions.py`
- **bench_profession_cache()** (5 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (4 connections) — `scripts/bench_cache_professions.py`
- **_get_empty_dict()** (4 connections) — `scripts/bench_cache_professions.py`
- **Any** (3 connections)
- **main()** (2 connections) — `scripts/bench_cache_professions.py`
- **.invalidate_professions()** (2 connections) — `server/caching/cache_service.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_professions.py`
- **Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit…** (1 connections) — `scripts/bench_cache_professions.py`
- **Helper function to return empty dict for mock methods.** (1 connections) — `scripts/bench_cache_professions.py`
- **Service for caching profession data.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all profession caches.** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [NPCCacheService](NPCCacheService.md) (4 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_professions.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 27 (84%)
- INFERRED: 5 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*