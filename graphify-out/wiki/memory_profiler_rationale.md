# memory profiler rationale

> 73 nodes

## Key Concepts

- **MemoryProfiler** (38 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler.py** (21 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **benchmark_model_memory_usage()** (13 connections) — `server/utils/memory_profiler.py`
- **memory_profiler.py** (10 connections) — `server/utils/memory_profiler.py`
- **SampleModel** (9 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.measure_model_instantiation()** (8 connections) — `server/utils/memory_profiler.py`
- **Any** (8 connections)
- **.measure_model_deserialization()** (8 connections) — `server/utils/memory_profiler.py`
- **.measure_model_serialization()** (7 connections) — `server/utils/memory_profiler.py`
- **.get_current_memory_usage()** (6 connections) — `server/utils/memory_profiler.py`
- **.get_memory_delta()** (6 connections) — `server/utils/memory_profiler.py`
- **OtherModel** (5 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_compare_models_memory_usage()** (5 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.start_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **.stop_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **.compare_models_memory_usage()** (5 connections) — `server/utils/memory_profiler.py`
- **.print_comparison_results()** (5 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler_measure_model_instantiation()** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_instantiation_zero_iterations()** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_serialization()** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_deserialization()** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.get_memory_usage_summary()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_memory_summary()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_model_memory_usage()** (4 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler_init()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- *... and 48 more nodes in this community*

## Relationships

- [grace period login](grace_period_login.md) (5 shared connections)
- [alias models rationale](alias_models_rationale.md) (3 shared connections)
- [command factories communication](command_factories_communication.md) (3 shared connections)
- [player service game](player_service_game.md) (2 shared connections)
- [command communication models](command_communication_models.md) (1 shared connections)
- [message queue realtime](message_queue_realtime.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_memory_profiler.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 242 (91%)
- INFERRED: 23 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*