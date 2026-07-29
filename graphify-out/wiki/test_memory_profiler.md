# test memory profiler

> 32 nodes

## Key Concepts

- **MemoryProfiler** (32 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler.py** (15 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **memory_profiler.py** (10 connections) — `server/utils/memory_profiler.py`
- **SampleModel** (6 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_instantiation()** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_instantiation_zero_iterations()** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_init()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_start_profiling()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_stop_profiling()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_current_memory_usage()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta_no_baseline()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_usage_summary()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_print_memory_summary()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_print_model_memory_usage()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.measure_model_instantiation() measures memory.** (2 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.__init__()** (2 connections) — `server/utils/memory_profiler.py`
- **BaseModel** (1 connections)
- **Unit tests for memory profiler utilities.  Tests the MemoryProfiler class method** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test Pydantic model for memory profiling tests.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler initialization.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.start_profiling() sets baseline.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.stop_profiling() stops tracemalloc.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.get_current_memory_usage() returns RSS.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **Test MemoryProfiler.get_memory_delta() calculates difference.** (1 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- *... and 7 more nodes in this community*

## Relationships

- [benchmark model memory usage()](benchmark_model_memory_usage%28%29.md) (14 shared connections)
- [get health status()](get_health_status%28%29.md) (4 shared connections)
- [alias](alias.md) (2 shared connections)
- [Spell Targeting](Spell_Targeting.md) (2 shared connections)
- [Core character statistics with Lovecraftian](Core_character_statistics_with_Lovecraftian.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_memory_profiler.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 108 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*