# Cache and NPC Cache

> 21 nodes · cohesion 0.05

## Key Concepts

- **Any** (14 connections) — `server/caching/cache_service.py`
- **_FakeNPCService** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_npc_cache()** (6 connections) — `scripts/bench_cache_npc.py`
- **bench_cache_professions.py** (6 connections) — `scripts/bench_cache_professions.py`
- **bench_profession_cache()** (6 connections) — `scripts/bench_cache_professions.py`
- **bench_cache_npc.py** (5 connections) — `scripts/bench_cache_npc.py`
- **Any** (5 connections) — `scripts/bench_cache_npc.py`
- **_FakePersistence** (5 connections) — `scripts/bench_cache_professions.py`
- **.get_npc_definitions()** (4 connections) — `scripts/bench_cache_npc.py`
- **.get_spawn_rules()** (4 connections) — `scripts/bench_cache_npc.py`
- **.get_all_professions()** (4 connections) — `scripts/bench_cache_professions.py`
- **Any** (4 connections) — `scripts/bench_cache_professions.py`
- **.get_npc_definition()** (3 connections) — `scripts/bench_cache_npc.py`
- **_get_empty_dict()** (3 connections) — `scripts/bench_cache_professions.py`
- **main()** (2 connections) — `scripts/bench_cache_professions.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_npc.py`
- **main()** (1 connections) — `scripts/bench_cache_npc.py`
- **NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for NP** (1 connections) — `scripts/bench_cache_npc.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_professions.py`
- **Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit timing** (1 connections) — `scripts/bench_cache_professions.py`
- **Helper function to return empty dict for mock methods.** (1 connections) — `scripts/bench_cache_professions.py`

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (4 shared connections)

## Source Files

- `scripts/bench_cache_npc.py`
- `scripts/bench_cache_professions.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 75 (89%)
- INFERRED: 9 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*