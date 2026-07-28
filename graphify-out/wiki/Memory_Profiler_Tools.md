# Memory Profiler Tools

> 61 nodes · cohesion 0.06

## Key Concepts

- **MemoryProfiler** (32 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler.py** (15 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **benchmark_model_memory_usage()** (13 connections) — `server/utils/memory_profiler.py`
- **memory_profiler.py** (10 connections) — `server/utils/memory_profiler.py`
- **.measure_model_deserialization()** (8 connections) — `server/utils/memory_profiler.py`
- **.measure_model_instantiation()** (8 connections) — `server/utils/memory_profiler.py`
- **Any** (8 connections)
- **.measure_model_serialization()** (7 connections) — `server/utils/memory_profiler.py`
- **SampleModel** (6 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.get_current_memory_usage()** (6 connections) — `server/utils/memory_profiler.py`
- **.get_memory_delta()** (6 connections) — `server/utils/memory_profiler.py`
- **.compare_models_memory_usage()** (5 connections) — `server/utils/memory_profiler.py`
- **.print_comparison_results()** (5 connections) — `server/utils/memory_profiler.py`
- **.start_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **.stop_profiling()** (5 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler_measure_model_instantiation()** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_measure_model_instantiation_zero_iterations()** (4 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **.get_memory_usage_summary()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_memory_summary()** (4 connections) — `server/utils/memory_profiler.py`
- **.print_model_memory_usage()** (4 connections) — `server/utils/memory_profiler.py`
- **test_memory_profiler_get_current_memory_usage()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_delta_no_baseline()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_get_memory_usage_summary()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- **test_memory_profiler_init()** (3 connections) — `server/tests/unit/utils/test_memory_profiler.py`
- *... and 36 more nodes in this community*

## Relationships

- [Exploration Command Factories](Exploration_Command_Factories.md) (5 shared connections)
- [UI Panel Manager](UI_Panel_Manager.md) (3 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (2 shared connections)
- [Character Stats Model](Character_Stats_Model.md) (2 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (1 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (1 shared connections)
- [Cursor Setup Guide](Cursor_Setup_Guide.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_memory_profiler.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 204 (93%)
- INFERRED: 15 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*