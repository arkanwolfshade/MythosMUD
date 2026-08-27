# AuthRateLimitMiddleware

> 15 nodes

## Key Concepts

- **.measure_model_deserialization()** (8 connections) — `server/utils/memory_profiler.py`
- **.measure_model_instantiation()** (8 connections) — `server/utils/memory_profiler.py`
- **.measure_model_serialization()** (7 connections) — `server/utils/memory_profiler.py`
- **.get_current_memory_usage()** (6 connections) — `server/utils/memory_profiler.py`
- **.get_memory_delta()** (6 connections) — `server/utils/memory_profiler.py`
- **.start_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **.stop_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **BaseModel** (1 connections)
- **Measure memory usage for model deserialization. Args: model_class: The Pydantic…** (1 connections) — `server/utils/memory_profiler.py`
- **Start memory profiling.** (1 connections) — `server/utils/memory_profiler.py`
- **Stop memory profiling.** (1 connections) — `server/utils/memory_profiler.py`
- **Get current memory usage in bytes.** (1 connections) — `server/utils/memory_profiler.py`
- **Get memory delta from baseline.** (1 connections) — `server/utils/memory_profiler.py`
- **Measure memory usage for model instantiation. Args: model_class: The Pydantic…** (1 connections) — `server/utils/memory_profiler.py`
- **Measure memory usage for model serialization. Args: instances: List of model…** (1 connections) — `server/utils/memory_profiler.py`

## Relationships

- [TrackedTaskManager](TrackedTaskManager.md) (7 shared connections)
- [bench_cache.py](bench_cache.py.md) (4 shared connections)

## Source Files

- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*