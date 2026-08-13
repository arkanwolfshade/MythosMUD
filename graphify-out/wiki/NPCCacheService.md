# NPCCacheService

> 40 nodes

## Key Concepts

- **NPCCacheService** (14 connections) — `server/caching/cache_service.py`
- **Any** (13 connections)
- **CacheService** (8 connections) — `server/caching/cache_service.py`
- **_FakeNPCService** (7 connections) — `scripts/bench_cache_npc.py`
- **.__init__()** (7 connections) — `server/caching/cache_service.py`
- **bench_cache_npc.py** (6 connections) — `scripts/bench_cache_npc.py`
- **bench_npc_cache()** (5 connections) — `scripts/bench_cache_npc.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_cache_stats()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (3 connections) — `server/caching/cache_service.py`
- **.get_spawn_rules()** (3 connections) — `server/caching/cache_service.py`
- **.get_all_professions()** (3 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (3 connections) — `server/caching/cache_service.py`
- **.get_room_sync()** (3 connections) — `server/caching/cache_service.py`
- **main()** (2 connections) — `scripts/bench_cache_npc.py`
- **.preload_frequently_accessed_data()** (2 connections) — `server/caching/cache_service.py`
- **.invalidate_npc_definitions()** (2 connections) — `server/caching/cache_service.py`
- **.invalidate_spawn_rules()** (2 connections) — `server/caching/cache_service.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_npc.py`
- **.clear_all_caches()** (1 connections) — `server/caching/cache_service.py`
- **NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for…** (1 connections) — `scripts/bench_cache_npc.py`
- **Initialize the room cache service. Args: persistence: Persistence layer instance** (1 connections) — `server/caching/cache_service.py`
- *... and 15 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (4 shared connections)
- [RoomCacheService](RoomCacheService.md) (4 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (4 shared connections)
- [LRUCache](LRUCache.md) (2 shared connections)

## Source Files

- `scripts/bench_cache_npc.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 68 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*