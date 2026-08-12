# NPCCacheService

> 37 nodes

## Key Concepts

- **NPCCacheService** (14 connections) — `server/caching/cache_service.py`
- **Any** (13 connections)
- **_FakeNPCService** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_cache_npc.py** (6 connections) — `scripts/bench_cache_npc.py`
- **bench_npc_cache()** (5 connections) — `scripts/bench_cache_npc.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **Any** (4 connections)
- **.get_npc_definition()** (3 connections) — `scripts/bench_cache_npc.py`
- **.get_npc_definitions()** (3 connections) — `scripts/bench_cache_npc.py`
- **.get_spawn_rules()** (3 connections) — `scripts/bench_cache_npc.py`
- **.get_cache_stats()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (3 connections) — `server/caching/cache_service.py`
- **.get_spawn_rules()** (3 connections) — `server/caching/cache_service.py`
- **.get_all_professions()** (3 connections) — `server/caching/cache_service.py`
- **.get_room()** (3 connections) — `server/caching/cache_service.py`
- **.get_room_sync()** (3 connections) — `server/caching/cache_service.py`
- **main()** (2 connections) — `scripts/bench_cache_npc.py`
- **.invalidate_npc_definitions()** (2 connections) — `server/caching/cache_service.py`
- **.invalidate_spawn_rules()** (2 connections) — `server/caching/cache_service.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_npc.py`
- **NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for…** (1 connections) — `scripts/bench_cache_npc.py`
- **Initialize the room cache service. Args: persistence: Persistence layer instance** (1 connections) — `server/caching/cache_service.py`
- *... and 12 more nodes in this community*

## Relationships

- [LRUCache](LRUCache.md) (10 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (3 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (3 shared connections)
- [RoomCacheService](RoomCacheService.md) (3 shared connections)
- [time.py](time.py.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_npc.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 104 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*