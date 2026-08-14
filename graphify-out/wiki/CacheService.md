# CacheService

> 14 nodes

## Key Concepts

- **CacheService** (24 connections) — `server/caching/cache_service.py`
- **TestCacheService** (12 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.__init__()** (7 connections) — `server/caching/cache_service.py`
- **.preload_frequently_accessed_data()** (2 connections) — `server/caching/cache_service.py`
- **.test_get_cache_stats_and_clear()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_with_npc_service()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_init_without_npc_service()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_frequently_accessed_data()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_handles_profession_failure()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_preload_handles_room_failure()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.clear_all_caches()** (1 connections) — `server/caching/cache_service.py`
- **Main cache service that coordinates all caching operations. This service…** (1 connections) — `server/caching/cache_service.py`
- **Initialize the cache service. Args: persistence: Persistence layer instance…** (1 connections) — `server/caching/cache_service.py`
- **Preload frequently accessed data into caches. This method loads commonly used…** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [get_cache_manager](get_cache_manager.md) (6 shared connections)
- [NPCCacheService](NPCCacheService.md) (5 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (5 shared connections)
- [RoomCacheService](RoomCacheService.md) (4 shared connections)
- [Any](Any.md) (2 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 29 (69%)
- INFERRED: 13 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*