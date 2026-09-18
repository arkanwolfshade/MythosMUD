# Community 730

> 23 nodes

## Key Concepts

- **MemoryMonitor** (35 connections) — `server/realtime/memory_monitor.py`
- **test_memory_monitor.py** (35 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **.force_garbage_collection()** (2 connections) — `server/realtime/memory_monitor.py`
- **.stop_idle_sampler()** (2 connections) — `server/realtime/memory_monitor.py`
- **.update_cleanup_time()** (2 connections) — `server/realtime/memory_monitor.py`
- **test_force_garbage_collection_runtime_error()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_alerts()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_alerts_error_path()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_alerts_warning_and_info_levels()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_stats()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_stats_error_returns_empty()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_usage_error_returns_zero()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_usage_invalid_type()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_usage_success()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_should_cleanup_memory_threshold()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_should_cleanup_returns_false()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_should_cleanup_time_based()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_update_cleanup_time_and_gc()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **Monitor memory usage and trigger cleanup when needed. This class provides…** (1 connections) — `server/realtime/memory_monitor.py`
- **Update the last cleanup time to the current time.** (1 connections) — `server/realtime/memory_monitor.py`
- **Force garbage collection to free memory.** (1 connections) — `server/realtime/memory_monitor.py`
- **Cancel the sampler task and stop tracemalloc if this monitor started it.** (1 connections) — `server/realtime/memory_monitor.py`
- **Unit tests for MemoryMonitor.** (1 connections) — `server/tests/unit/realtime/test_memory_monitor.py`

## Relationships

- [Community 931](Community_931.md) (8 shared connections)
- [Community 1306](Community_1306.md) (7 shared connections)
- [Community 42](Community_42.md) (6 shared connections)
- [Community 1356](Community_1356.md) (5 shared connections)
- [Community 1301](Community_1301.md) (3 shared connections)
- [Community 1240](Community_1240.md) (3 shared connections)
- [Community 891](Community_891.md) (2 shared connections)
- [Community 211](Community_211.md) (1 shared connections)
- [Community 1138](Community_1138.md) (1 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 70 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*