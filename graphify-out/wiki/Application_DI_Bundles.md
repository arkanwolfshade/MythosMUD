# Application DI Bundles

> 10 nodes

## Key Concepts

- **bench_cache_professions.py** (7 connections) — `scripts/bench_cache_professions.py`
- **bench_profession_cache()** (6 connections) — `scripts/bench_cache_professions.py`
- **_FakePersistence** (5 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (5 connections) — `scripts/bench_cache_professions.py`
- **_get_empty_dict()** (4 connections) — `scripts/bench_cache_professions.py`
- **Any** (3 connections)
- **main()** (2 connections) — `scripts/bench_cache_professions.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_professions.py`
- **Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit timing** (1 connections) — `scripts/bench_cache_professions.py`
- **Helper function to return empty dict for mock methods.** (1 connections) — `scripts/bench_cache_professions.py`

## Relationships

- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (3 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)
- [FastAPI App Factory](FastAPI_App_Factory.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_professions.py`

## Audit Trail

- EXTRACTED: 31 (89%)
- INFERRED: 4 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*