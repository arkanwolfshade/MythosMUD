# Alias Command Models

> 16 nodes

## Key Concepts

- **NPCCacheService** (14 connections) — `server/caching/cache_service.py`
- **_FakeNPCService** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_npc_cache()** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_cache_npc.py** (6 connections) — `scripts/bench_cache_npc.py`
- **.get_npc_definitions()** (4 connections) — `scripts/bench_cache_npc.py`
- **Any** (4 connections)
- **.get_spawn_rules()** (4 connections) — `scripts/bench_cache_npc.py`
- **.get_npc_definition()** (3 connections) — `scripts/bench_cache_npc.py`
- **main()** (2 connections) — `scripts/bench_cache_npc.py`
- **.invalidate_npc_definitions()** (2 connections) — `server/caching/cache_service.py`
- **.invalidate_spawn_rules()** (2 connections) — `server/caching/cache_service.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_npc.py`
- **NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for NP** (1 connections) — `scripts/bench_cache_npc.py`
- **Service for caching NPC definitions and spawn rules.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all NPC definition caches.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all NPC spawn rule caches.** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [Grace Period Blocking Tests](Grace_Period_Blocking_Tests.md) (6 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_npc.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 52 (87%)
- INFERRED: 8 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*