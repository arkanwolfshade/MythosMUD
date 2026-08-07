# ascii map renderer

> 10 nodes

## Key Concepts

- **_FakeNPCService** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_npc_cache()** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_cache_npc.py** (6 connections) — `scripts/bench_cache_npc.py`
- **Any** (4 connections)
- **.get_npc_definitions()** (3 connections) — `scripts/bench_cache_npc.py`
- **.get_spawn_rules()** (3 connections) — `scripts/bench_cache_npc.py`
- **.get_npc_definition()** (2 connections) — `scripts/bench_cache_npc.py`
- **main()** (2 connections) — `scripts/bench_cache_npc.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_npc.py`
- **NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for NP** (1 connections) — `scripts/bench_cache_npc.py`

## Relationships

- [player requests schemas](player_requests_schemas.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_npc.py`

## Audit Trail

- EXTRACTED: 33 (92%)
- INFERRED: 3 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*