# Bench Cache Npc

> 10 nodes · cohesion 0.33

## Key Concepts

- **_FakeNPCService** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_npc_cache()** (6 connections) — `scripts/bench_cache_npc.py`
- **bench_cache_npc.py** (5 connections) — `scripts/bench_cache_npc.py`
- **Any** (5 connections) — `scripts/bench_cache_npc.py`
- **.get_npc_definitions()** (4 connections) — `scripts/bench_cache_npc.py`
- **.get_spawn_rules()** (4 connections) — `scripts/bench_cache_npc.py`
- **.get_npc_definition()** (3 connections) — `scripts/bench_cache_npc.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_npc.py`
- **main()** (1 connections) — `scripts/bench_cache_npc.py`
- **NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for NP** (1 connections) — `scripts/bench_cache_npc.py`

## Relationships

- [[Cache and NPC Cache]] (4 shared connections)
- [[Communication Command Flows]] (3 shared connections)

## Source Files

- `scripts/bench_cache_npc.py`

## Audit Trail

- EXTRACTED: 32 (86%)
- INFERRED: 5 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
