# Grace Period Blocking Tests

> 22 nodes

## Key Concepts

- **NPCCacheService** (14 connections) — `server/caching/cache_service.py`
- **_FakeNPCService** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_npc_cache()** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_cache_npc.py** (6 connections) — `scripts/bench_cache_npc.py`
- **.get_npc_definitions()** (4 connections) — `scripts/bench_cache_npc.py`
- **Any** (4 connections)
- **.get_spawn_rules()** (4 connections) — `scripts/bench_cache_npc.py`
- **.get_npc_definition()** (3 connections) — `scripts/bench_cache_npc.py`
- **.get_npc_definitions()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `server/caching/cache_service.py`
- **.get_spawn_rules()** (3 connections) — `server/caching/cache_service.py`
- **main()** (2 connections) — `scripts/bench_cache_npc.py`
- **.invalidate_npc_definitions()** (2 connections) — `server/caching/cache_service.py`
- **.invalidate_spawn_rules()** (2 connections) — `server/caching/cache_service.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_npc.py`
- **NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for NP** (1 connections) — `scripts/bench_cache_npc.py`
- **Service for caching NPC definitions and spawn rules.** (1 connections) — `server/caching/cache_service.py`
- **Get NPC definitions with caching.          Args:             session: Database s** (1 connections) — `server/caching/cache_service.py`
- **Get a specific NPC definition with caching.          Args:             session:** (1 connections) — `server/caching/cache_service.py`
- **Get NPC spawn rules with caching.          Args:             session: Database s** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all NPC definition caches.** (1 connections) — `server/caching/cache_service.py`
- **Invalidate all NPC spawn rule caches.** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (8 shared connections)
- [FastAPI App Factory](FastAPI_App_Factory.md) (3 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_npc.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 64 (89%)
- INFERRED: 8 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*