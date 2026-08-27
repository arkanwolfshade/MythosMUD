# Disconnect Grace Period (linkdead)

> 4 nodes

## Key Concepts

- **.get_memory_usage_summary()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_memory_summary()** (3 connections) — `server/utils/memory_profiler.py`
- **Get a summary of current memory usage.** (1 connections) — `server/utils/memory_profiler.py`
- **Print a formatted memory usage summary.** (1 connections) — `server/utils/memory_profiler.py`

## Relationships

- [TrackedTaskManager](TrackedTaskManager.md) (2 shared connections)
- [bench_cache.py](bench_cache.py.md) (1 shared connections)

## Source Files

- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*