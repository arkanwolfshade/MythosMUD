# Memory Profiler Tools

> 59 nodes

## Key Concepts

- **MemoryProfiler** (32 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler.py** (15 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **benchmark_model_memory_usage()** (13 connections) — `server/utils/memory_profiler.py`
- **.measure_model_instantiation()** (8 connections) — `server/utils/memory_profiler.py`
- **Any** (8 connections)
- **.measure_model_deserialization()** (8 connections) — `server/utils/memory_profiler.py`
- **.measure_model_serialization()** (7 connections) — `server/utils/memory_profiler.py`
- **SampleModel** (6 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.get_current_memory_usage()** (6 connections) — `server/utils/memory_profiler.py`
- **.get_memory_delta()** (6 connections) — `server/utils/memory_profiler.py`
- **.start_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **.stop_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **.compare_models_memory_usage()** (5 connections) — `server/utils/memory_profiler.py`
- **.print_comparison_results()** (5 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler_measure_model_instantiation()** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_instantiation_zero_iterations()** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.get_memory_usage_summary()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_memory_summary()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_model_memory_usage()** (4 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler_init()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_start_profiling()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_stop_profiling()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_current_memory_usage()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta_no_baseline()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- *... and 34 more nodes in this community*

## Relationships

- [Monitoring Response Models](Monitoring_Response_Models.md) (6 shared connections)
- [Alias Expansion Logic](Alias_Expansion_Logic.md) (2 shared connections)
- [NPC Occupant Processor](NPC_Occupant_Processor.md) (1 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (1 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (1 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_memory_profiler.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 193 (93%)
- INFERRED: 15 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*