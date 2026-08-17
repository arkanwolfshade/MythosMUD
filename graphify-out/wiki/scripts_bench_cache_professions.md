# scripts bench cache professions

> 10 nodes

## Key Concepts

- **bench_cache_professions.py** (7 connections) — `scripts/bench_cache_professions.py`
- **bench_profession_cache()** (5 connections) — `scripts/bench_cache_professions.py`
- **_FakePersistence** (4 connections) — `scripts/bench_cache_professions.py`
- **_get_empty_dict()** (4 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (3 connections) — `scripts/bench_cache_professions.py`
- **Any** (3 connections)
- **main()** (2 connections) — `scripts/bench_cache_professions.py`
- **.__init__()** (1 connections) — `scripts/bench_cache_professions.py`
- **Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit…** (1 connections) — `scripts/bench_cache_professions.py`
- **Helper function to return empty dict for mock methods.** (1 connections) — `scripts/bench_cache_professions.py`

## Relationships

- [server caching cache service](server_caching_cache_service.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `scripts/bench_cache_professions.py`

## Audit Trail

- EXTRACTED: 15 (88%)
- INFERRED: 2 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*