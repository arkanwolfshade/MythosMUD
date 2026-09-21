# MemoryMonitor

> 21 nodes

## Key Concepts

- **MemoryMonitor** (39 connections) — `server/realtime/memory_monitor.py`
- **test_memory_monitor.py** (35 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **.get_memory_stats()** (3 connections) — `server/realtime/memory_monitor.py`
- **.force_garbage_collection()** (2 connections) — `server/realtime/memory_monitor.py`
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
- **Get detailed memory statistics. Returns: dict: Memory statistics including RSS,…** (1 connections) — `server/realtime/memory_monitor.py`
- **Force garbage collection to free memory.** (1 connections) — `server/realtime/memory_monitor.py`
- **Unit tests for MemoryMonitor.** (1 connections) — `server/tests/unit/realtime/test_memory_monitor.py`

## Relationships

- [connection_manager.py](connection_manager.py.md) (10 shared connections)
- [idle_sampler_enabled](idle_sampler_enabled.md) (9 shared connections)
- [._run_idle_sampler](_run_idle_sampler.md) (6 shared connections)
- [_max_connection_age_seconds](_max_connection_age_seconds.md) (5 shared connections)
- [.get_memory_alerts](get_memory_alerts.md) (3 shared connections)
- [_task_qualname](_task_qualname.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [collect_idle_memory_sample](collect_idle_memory_sample.md) (2 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (1 shared connections)
- [.update_cleanup_time](update_cleanup_time.md) (1 shared connections)
- [.stop_idle_sampler](stop_idle_sampler.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 72 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*