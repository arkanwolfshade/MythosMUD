# Memory Profiler Tools

> 60 nodes · cohesion 0.06

## Key Concepts

- **MemoryProfiler** (32 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler.py** (14 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **HealthStatus** (13 connections) — `server/models/health.py`
- **Any** (11 connections) — `server/utils/memory_profiler.py`
- **memory_profiler.py** (9 connections) — `server/utils/memory_profiler.py`
- **.measure_model_deserialization()** (8 connections) — `server/utils/memory_profiler.py`
- **.measure_model_instantiation()** (8 connections) — `server/utils/memory_profiler.py`
- **benchmark_model_memory_usage()** (7 connections) — `server/utils/memory_profiler.py`
- **.measure_model_serialization()** (7 connections) — `server/utils/memory_profiler.py`
- **.get_current_memory_usage()** (6 connections) — `server/utils/memory_profiler.py`
- **.get_memory_delta()** (6 connections) — `server/utils/memory_profiler.py`
- **.compare_models_memory_usage()** (5 connections) — `server/utils/memory_profiler.py`
- **.print_comparison_results()** (5 connections) — `server/utils/memory_profiler.py`
- **.start_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **.stop_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **BaseModel** (4 connections) — `server/utils/memory_profiler.py`
- **.get_memory_usage_summary()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_memory_summary()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_model_memory_usage()** (4 connections) — `server/utils/memory_profiler.py`
- **SampleModel** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_current_memory_usage()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta_no_baseline()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_usage_summary()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_init()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- *... and 35 more nodes in this community*

## Relationships

- [[Health Check Models]] (7 shared connections)
- [[Command Alias Model]] (4 shared connections)
- [[Monitoring API Endpoints]] (2 shared connections)
- [[SQLAlchemy Model Base]] (1 shared connections)
- [[Spell Registry Costs]] (1 shared connections)
- [[Health Service Tests]] (1 shared connections)
- [[Game Magic Spell]] (1 shared connections)
- [[Status Effect Model]] (1 shared connections)
- [[Character Stats Model]] (1 shared connections)
- [[Admin NPC Schemas]] (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/tests/unit/utils/test_memory_profiler.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 212 (94%)
- INFERRED: 14 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
