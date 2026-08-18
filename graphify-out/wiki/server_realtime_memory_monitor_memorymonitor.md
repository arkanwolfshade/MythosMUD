# server realtime memory monitor memorymonitor

> 23 nodes

## Key Concepts

- **MemoryMonitor** (39 connections) — `server/realtime/memory_monitor.py`
- **test_memory_monitor.py** (32 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **.get_memory_stats()** (3 connections) — `server/realtime/memory_monitor.py`
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
- **Get detailed memory statistics. Returns: dict: Memory statistics including RSS,…** (1 connections) — `server/realtime/memory_monitor.py`
- **Update the last cleanup time to the current time.** (1 connections) — `server/realtime/memory_monitor.py`
- **Cancel the sampler task and stop tracemalloc if this monitor started it.** (1 connections) — `server/realtime/memory_monitor.py`
- **Unit tests for MemoryMonitor.** (1 connections) — `server/tests/unit/realtime/test_memory_monitor.py`

## Relationships

- [server realtime memory monitor idle](server_realtime_memory_monitor_idle.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server realtime memory monitor max](server_realtime_memory_monitor_max.md) (5 shared connections)
- [server realtime memory monitor append](server_realtime_memory_monitor_append.md) (5 shared connections)
- [server realtime memory monitor as](server_realtime_memory_monitor_as.md) (3 shared connections)
- [deque](deque.md) (2 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (2 shared connections)
- [server realtime connection manager methods](server_realtime_connection_manager_methods.md) (2 shared connections)
- [server realtime memory monitor collect](server_realtime_memory_monitor_collect.md) (2 shared connections)
- [memorymonitor](memorymonitor.md) (1 shared connections)
- [server realtime monitoring health monitor](server_realtime_monitoring_health_monitor.md) (1 shared connections)
- [server realtime memory monitor memorymonitor](server_realtime_memory_monitor_memorymonitor.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 70 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*