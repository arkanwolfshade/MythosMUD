# server tests unit utils test

> 71 nodes

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
- *... and 46 more nodes in this community*

## Relationships

- [server api monitoring](server_api_monitoring.md) (4 shared connections)
- [server alias storage aliasstorage add](server_alias_storage_aliasstorage_add.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (2 shared connections)
- [computed field](computed_field.md) (1 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (1 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_memory_profiler.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 107 (85%)
- INFERRED: 19 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*