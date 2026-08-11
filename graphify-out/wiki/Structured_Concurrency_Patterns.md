# Structured Concurrency Patterns

> 16 nodes

## Key Concepts

- **ProfessionCacheService** (15 connections) — `server/caching/cache_service.py`
- **bench_cache_professions.py** (7 connections) — `scripts/bench_cache_professions.py`
- **bench_profession_cache()** (6 connections) — `scripts/bench_cache_professions.py`
- **_FakePersistence** (5 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (5 connections) — `scripts/bench_cache_professions.py`
- **_get_empty_dict()** (4 connections) — `scripts/bench_cache_professions.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **Any** (3 connections)
- **main()** (2 connections) — `scripts/bench_cache_professions.py`
- **.invalidate_professions()** (2 connections) — `server/caching/cache_service.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_professions.py`
- **Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit timing** (1 connections) — `scripts/bench_cache_professions.py`
- **Helper function to return empty dict for mock methods.** (1 connections) — `scripts/bench_cache_professions.py`
- **Service for caching profession data.** (1 connections) — `server/caching/cache_service.py`
- **Initialize the profession cache service.          Args:             persistence:** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all profession caches.** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [Alias Command Models](Alias_Command_Models.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)
- [Schedule Service Loader](Schedule_Service_Loader.md) (1 shared connections)
- [Grace Period Blocking Tests](Grace_Period_Blocking_Tests.md) (1 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_professions.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 52 (88%)
- INFERRED: 7 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*