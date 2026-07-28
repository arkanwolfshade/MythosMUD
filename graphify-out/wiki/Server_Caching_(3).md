# Server Caching (3)

> 20 nodes

## Key Concepts

- **ProfessionCacheService** (12 connections) — `server/caching/cache_service.py`
- **bench_cache_professions.py** (7 connections) — `scripts/bench_cache_professions.py`
- **bench_profession_cache()** (6 connections) — `scripts/bench_cache_professions.py`
- **_FakePersistence** (5 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (5 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (5 connections) — `server/caching/cache_service.py`
- **_get_empty_dict()** (4 connections) — `scripts/bench_cache_professions.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (4 connections) — `server/caching/cache_service.py`
- **Any** (3 connections)
- **main()** (2 connections) — `scripts/bench_cache_professions.py`
- **.invalidate_professions()** (2 connections) — `server/caching/cache_service.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_professions.py`
- **Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit timing** (1 connections) — `scripts/bench_cache_professions.py`
- **Helper function to return empty dict for mock methods.** (1 connections) — `scripts/bench_cache_professions.py`
- **Service for caching profession data.** (1 connections) — `server/caching/cache_service.py`
- **Initialize the profession cache service.          Args:             persistence:** (1 connections) — `server/caching/cache_service.py`
- **Get all professions with caching.          Returns:             List of professi** (1 connections) — `server/caching/cache_service.py`
- **Get a specific profession by ID with caching.          Args:             profess** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all profession caches.** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [Server Caching (2)](Server_Caching_%282%29.md) (5 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Caching](Server_Caching.md) (2 shared connections)
- [Server Commands (6)](Server_Commands_%286%29.md) (1 shared connections)
- [Server Monitoring](Server_Monitoring.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_professions.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 61 (91%)
- INFERRED: 6 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*