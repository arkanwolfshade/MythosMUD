# MemoryProfiler

> 12 nodes

## Key Concepts

- **MemoryProfiler** (33 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler_get_memory_delta_no_baseline()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_instantiation_zero_iterations()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_print_model_memory_usage()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_print_model_memory_usage_error()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.__init__()** (2 connections) — `server/utils/memory_profiler.py`
- **Test MemoryProfiler.measure_model_instantiation() handles zero iterations.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.print_model_memory_usage() doesn't raise.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.print_model_memory_usage() handles error dict.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.get_memory_delta() returns 0 if no baseline.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Memory profiler for analyzing model memory usage.** (1 connections) — `server/utils/memory_profiler.py`
- **Initialize the memory profiler.** (1 connections) — `server/utils/memory_profiler.py`

## Relationships

- [test_memory_profiler.py](test_memory_profiler.py.md) (15 shared connections)
- [.measure_model_deserialization](measure_model_deserialization.md) (7 shared connections)
- [Any](Any.md) (4 shared connections)
- [.get_memory_usage_summary](get_memory_usage_summary.md) (2 shared connections)
- [server/models/game.py](server-models-game.py.md) (1 shared connections)
- [test_memory_profiler_get_current_memory_usage](test_memory_profiler_get_current_memory_usage.md) (1 shared connections)
- [SampleModel](SampleModel.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_memory_profiler.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 26 (62%)
- INFERRED: 16 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*