# scripts bench cache npc

> 10 nodes

## Key Concepts

- **_FakeNPCService** (6 connections) — `scripts/bench_cache_npc.py`
- **bench_cache_npc.py** (6 connections) — `scripts/bench_cache_npc.py`
- **bench_npc_cache()** (5 connections) — `scripts/bench_cache_npc.py`
- **Any** (4 connections)
- **.get_npc_definition()** (2 connections) — `scripts/bench_cache_npc.py`
- **.get_npc_definitions()** (2 connections) — `scripts/bench_cache_npc.py`
- **.get_spawn_rules()** (2 connections) — `scripts/bench_cache_npc.py`
- **main()** (2 connections) — `scripts/bench_cache_npc.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_npc.py`
- **NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for…** (1 connections) — `scripts/bench_cache_npc.py`

## Relationships

- [server caching cache service](server_caching_cache_service.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_npc.py`

## Audit Trail

- EXTRACTED: 15 (88%)
- INFERRED: 2 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*