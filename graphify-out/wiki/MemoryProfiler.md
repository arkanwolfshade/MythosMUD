# MemoryProfiler

> 71 nodes

## Key Concepts

- **MemoryProfiler** (38 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler.py** (21 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.measure_model_deserialization()** (8 connections) — `server/utils/memory_profiler.py`
- **.measure_model_instantiation()** (8 connections) — `server/utils/memory_profiler.py`
- **Any** (8 connections)
- **.measure_model_serialization()** (7 connections) — `server/utils/memory_profiler.py`
- **.get_current_memory_usage()** (6 connections) — `server/utils/memory_profiler.py`
- **.get_memory_delta()** (6 connections) — `server/utils/memory_profiler.py`
- **SampleModel** (5 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.start_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **.stop_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **OtherModel** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_serialization()** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **benchmark_model_memory_usage()** (4 connections) — `server/utils/memory_profiler.py`
- **.compare_models_memory_usage()** (4 connections) — `server/utils/memory_profiler.py`
- **.get_memory_usage_summary()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_comparison_results()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_model_memory_usage()** (4 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler_compare_models_memory_usage()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_current_memory_usage()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta_no_baseline()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_usage_summary()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_init()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_deserialization()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- *... and 46 more nodes in this community*

## Relationships

- [server/models/game.py](server-models-game.py.md) (3 shared connections)
- [test_health.py](test_health.py.md) (2 shared connections)
- [Alias](Alias.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_memory_profiler.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 114 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*