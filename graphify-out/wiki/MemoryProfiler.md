# MemoryProfiler

> 73 nodes

## Key Concepts

- **MemoryProfiler** (33 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler.py** (22 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **memory_profiler.py** (11 connections) — `server/utils/memory_profiler.py`
- **.measure_model_deserialization()** (8 connections) — `server/utils/memory_profiler.py`
- **.measure_model_instantiation()** (8 connections) — `server/utils/memory_profiler.py`
- **Any** (8 connections)
- **benchmark_model_memory_usage()** (7 connections) — `server/utils/memory_profiler.py`
- **.measure_model_serialization()** (7 connections) — `server/utils/memory_profiler.py`
- **.get_current_memory_usage()** (6 connections) — `server/utils/memory_profiler.py`
- **.get_memory_delta()** (6 connections) — `server/utils/memory_profiler.py`
- **.start_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **.stop_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **SampleModel** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_serialization()** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.compare_models_memory_usage()** (4 connections) — `server/utils/memory_profiler.py`
- **.get_memory_usage_summary()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_comparison_results()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_model_memory_usage()** (4 connections) — `server/utils/memory_profiler.py`
- **OtherModel** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_compare_models_memory_usage()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_current_memory_usage()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta_no_baseline()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_usage_summary()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_init()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- *... and 48 more nodes in this community*

## Relationships

- [HealthStatus](HealthStatus.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [pydantic.md](pydantic.md.md) (2 shared connections)
- [Stats](Stats.md) (1 shared connections)
- [StatusEffect](StatusEffect.md) (1 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_memory_profiler.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 123 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*