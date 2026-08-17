# MemoryProfiler

> 12 nodes

## Key Concepts

- **MemoryProfiler** (33 connections) — `server/utils/memory_profiler.py`
- **.get_memory_usage_summary()** (4 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler_get_memory_delta()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_init()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.print_memory_summary()** (3 connections) — `server/utils/memory_profiler.py`
- **.__init__()** (2 connections) — `server/utils/memory_profiler.py`
- **Test MemoryProfiler initialization.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.get_memory_delta() calculates difference.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Memory profiler for analyzing model memory usage.** (1 connections) — `server/utils/memory_profiler.py`
- **Get a summary of current memory usage.** (1 connections) — `server/utils/memory_profiler.py`
- **Initialize the memory profiler.** (1 connections) — `server/utils/memory_profiler.py`
- **Print a formatted memory usage summary.** (1 connections) — `server/utils/memory_profiler.py`

## Relationships

- [test_memory_profiler.py](test_memory_profiler.py.md) (13 shared connections)
- [.measure_model_deserialization](measure_model_deserialization.md) (7 shared connections)
- [memory_profiler.py](memory_profiler.py.md) (6 shared connections)
- [test_memory_profiler_measure_model_instantiation_zero_iterations](test_memory_profiler_measure_model_instantiation_zero_iterations.md) (1 shared connections)
- [SampleModel](SampleModel.md) (1 shared connections)
- [test_memory_profiler_print_model_memory_usage](test_memory_profiler_print_model_memory_usage.md) (1 shared connections)
- [test_memory_profiler_print_model_memory_usage_error](test_memory_profiler_print_model_memory_usage_error.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_memory_profiler.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 26 (62%)
- INFERRED: 16 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*