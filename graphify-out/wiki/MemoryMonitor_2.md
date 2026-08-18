# MemoryMonitor

> 19 nodes

## Key Concepts

- **MemoryMonitor** (39 connections) — `server/realtime/memory_monitor.py`
- **test_memory_monitor.py** (32 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **.stop_idle_sampler()** (2 connections) — `server/realtime/memory_monitor.py`
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
- **Cancel the sampler task and stop tracemalloc if this monitor started it.** (1 connections) — `server/realtime/memory_monitor.py`
- **Unit tests for MemoryMonitor.** (1 connections) — `server/tests/unit/realtime/test_memory_monitor.py`

## Relationships

- [idle_sampler_enabled](idle_sampler_enabled.md) (9 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [_max_connection_age_seconds](_max_connection_age_seconds.md) (5 shared connections)
- [._run_idle_sampler](_run_idle_sampler.md) (5 shared connections)
- [.get_memory_alerts](get_memory_alerts.md) (3 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (2 shared connections)
- [collect_idle_memory_sample](collect_idle_memory_sample.md) (2 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (1 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (1 shared connections)
- [IdleMemorySample](IdleMemorySample.md) (1 shared connections)
- [.update_cleanup_time](update_cleanup_time.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 67 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*