# room build realtime

> 9 nodes

## Key Concepts

- **bench_cache.py** (6 connections) — `scripts/bench_cache.py`
- **_FakePersistence** (6 connections) — `scripts/bench_cache.py`
- **bench_room_cache()** (5 connections) — `scripts/bench_cache.py`
- **.async_get_room()** (2 connections) — `scripts/bench_cache.py`
- **Any** (2 connections)
- **main()** (2 connections) — `scripts/bench_cache.py`
- **.__init__()** (1 connections) — `scripts/bench_cache.py`
- **Lightweight cache benchmark for CI artifacts.  Measures miss vs. hit timings for** (1 connections) — `scripts/bench_cache.py`
- **Fake persistence layer providing async_get_room with simulated latency.** (1 connections) — `scripts/bench_cache.py`

## Relationships

- [startup npc service](startup_npc_service.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `scripts/bench_cache.py`

## Audit Trail

- EXTRACTED: 23 (88%)
- INFERRED: 3 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*