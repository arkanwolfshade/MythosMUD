# Server Caching (2)

> 52 nodes

## Key Concepts

- **RoomCacheService** (14 connections) — `server/caching/cache_service.py`
- **NPCCacheService** (14 connections) — `server/caching/cache_service.py`
- **Any** (13 connections)
- **_FakeNPCService** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_npc_cache()** (7 connections) — `scripts/bench_cache_npc.py`
- **.__init__()** (7 connections) — `server/caching/cache_service.py`
- **bench_cache.py** (6 connections) — `scripts/bench_cache.py`
- **_FakePersistence** (6 connections) — `scripts/bench_cache.py`
- **bench_cache_npc.py** (6 connections) — `scripts/bench_cache_npc.py`
- **bench_room_cache()** (5 connections) — `scripts/bench_cache.py`
- **.get_npc_definitions()** (4 connections) — `scripts/bench_cache_npc.py`
- **Any** (4 connections)
- **.get_spawn_rules()** (4 connections) — `scripts/bench_cache_npc.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_room_sync()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.preload_frequently_accessed_data()** (4 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `scripts/bench_cache_npc.py`
- **.get_room()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `server/caching/cache_service.py`
- **.get_spawn_rules()** (3 connections) — `server/caching/cache_service.py`
- **.get_cache_stats()** (3 connections) — `server/caching/cache_service.py`
- **.async_get_room()** (2 connections) — `scripts/bench_cache.py`
- **Any** (2 connections)
- *... and 27 more nodes in this community*

## Relationships

- [Server Caching](Server_Caching.md) (8 shared connections)
- [Server Caching (3)](Server_Caching_%283%29.md) (5 shared connections)
- [Server Commands](Server_Commands.md) (4 shared connections)
- [Server Commands (6)](Server_Commands_%286%29.md) (3 shared connections)
- [Server Monitoring](Server_Monitoring.md) (3 shared connections)
- [Server Game (8)](Server_Game_%288%29.md) (1 shared connections)

## Source Files

- `scripts/bench_cache.py`
- `scripts/bench_cache_npc.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 155 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*