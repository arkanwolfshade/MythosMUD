# bench_cache.py

> 11 nodes

## Key Concepts

- **memory_profiler.py** (11 connections) — `server/utils/memory_profiler.py`
- **Any** (8 connections)
- **benchmark_model_memory_usage()** (7 connections) — `server/utils/memory_profiler.py`
- **.compare_models_memory_usage()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_comparison_results()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_model_memory_usage()** (4 connections) — `server/utils/memory_profiler.py`
- **Memory profiling utilities for MythosMUD models. This module provides…** (1 connections) — `server/utils/memory_profiler.py`
- **Compare memory usage across multiple model classes. Args: model_classes: List…** (1 connections) — `server/utils/memory_profiler.py`
- **Print formatted model memory usage results.** (1 connections) — `server/utils/memory_profiler.py`
- **Print formatted comparison results.** (1 connections) — `server/utils/memory_profiler.py`
- **Benchmark memory usage for all major models.** (1 connections) — `server/utils/memory_profiler.py`

## Relationships

- [TrackedTaskManager](TrackedTaskManager.md) (6 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (4 shared connections)
- [AuthRateLimitMiddleware](AuthRateLimitMiddleware.md) (4 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [extract_player_name](extract_player_name.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [Disconnect Grace Period (linkdead)](Disconnect_Grace_Period_linkdead.md) (1 shared connections)

## Source Files

- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 29 (91%)
- INFERRED: 3 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*