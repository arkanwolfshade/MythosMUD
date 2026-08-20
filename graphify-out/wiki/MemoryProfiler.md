# MemoryProfiler

> 34 nodes

## Key Concepts

- **MemoryProfiler** (33 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler.py** (22 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_compare_models_memory_usage()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta_no_baseline()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_usage_summary()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_init()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_deserialization()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_instantiation()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_instantiation_zero_iterations()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_print_comparison_results()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_print_memory_summary()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_print_model_memory_usage()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_print_model_memory_usage_error()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_start_profiling()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_stop_profiling()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.__init__()** (2 connections) — `server/utils/memory_profiler.py`
- **Unit tests for memory profiler utilities. Tests the MemoryProfiler class…** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.measure_model_instantiation() handles zero iterations.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.get_memory_usage_summary() returns summary.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.print_memory_summary() doesn't raise.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.print_model_memory_usage() doesn't raise.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.print_model_memory_usage() handles error dict.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.measure_model_deserialization() returns stats.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler initialization.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- *... and 9 more nodes in this community*

## Relationships

- [.measure_model_deserialization](measure_model_deserialization.md) (7 shared connections)
- [SampleModel](SampleModel.md) (4 shared connections)
- [Any](Any.md) (4 shared connections)
- [test_memory_profiler_get_current_memory_usage](test_memory_profiler_get_current_memory_usage.md) (2 shared connections)
- [server/models/game.py](server-models-game.py.md) (2 shared connections)
- [.get_memory_usage_summary](get_memory_usage_summary.md) (2 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_memory_profiler.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 69 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*