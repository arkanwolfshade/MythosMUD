# config rationale config()

> 14 nodes

## Key Concepts

- **CacheService** (24 connections) — `server/caching/cache_service.py`
- **TestCacheService** (12 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.get_room_sync()** (4 connections) — `server/caching/cache_service.py`
- **.preload_frequently_accessed_data()** (4 connections) — `server/caching/cache_service.py`
- **.test_init_without_npc_service()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_with_npc_service()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_cache_stats_and_clear()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_frequently_accessed_data()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_handles_room_failure()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_handles_profession_failure()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.clear_all_caches()** (1 connections) — `server/caching/cache_service.py`
- **Get room data with caching (synchronous version).          Args:             roo** (1 connections) — `server/caching/cache_service.py`
- **Main cache service that coordinates all caching operations.      This service pr** (1 connections) — `server/caching/cache_service.py`
- **Preload frequently accessed data into caches.          This method loads commonl** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [startup npc service](startup_npc_service.md) (5 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (5 shared connections)
- [uuid services npc](uuid_services_npc.md) (4 shared connections)
- [services lucidity repository](services_lucidity_repository.md) (4 shared connections)
- [cache caching service](cache_caching_service.md) (3 shared connections)
- [caching lru cache](caching_lru_cache.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 46 (77%)
- INFERRED: 14 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*