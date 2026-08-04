# config rationale config()

> 11 nodes

## Key Concepts

- **CacheService** (24 connections) — `server/caching/cache_service.py`
- **TestCacheService** (12 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.persistence()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_without_npc_service()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_with_npc_service()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_cache_stats_and_clear()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_frequently_accessed_data()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_handles_room_failure()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_handles_profession_failure()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.clear_all_caches()** (1 connections) — `server/caching/cache_service.py`
- **Main cache service that coordinates all caching operations.      This service pr** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [commands skills rationale](commands_skills_rationale.md) (5 shared connections)
- [startup npc service](startup_npc_service.md) (4 shared connections)
- [uuid services npc](uuid_services_npc.md) (4 shared connections)
- [services lucidity repository](services_lucidity_repository.md) (4 shared connections)
- [cache caching service](cache_caching_service.md) (2 shared connections)
- [caching lru cache](caching_lru_cache.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 38 (73%)
- INFERRED: 14 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*