# MemoryMonitor

> 45 nodes

## Key Concepts

- **MemoryMonitor** (27 connections) — `server/realtime/memory_monitor.py`
- **connection_cleaner.py** (24 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **statistics_aggregator.py** (23 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **test_memory_monitor.py** (21 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **memory_monitor.py** (10 connections) — `server/realtime/memory_monitor.py`
- **_max_connection_age_seconds()** (7 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_alerts()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_usage()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_stats()** (3 connections) — `server/realtime/memory_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/memory_monitor.py`
- **.should_cleanup()** (3 connections) — `server/realtime/memory_monitor.py`
- **server/realtime/maintenance/__init__.py** (3 connections) — `server/realtime/maintenance/__init__.py`
- **.force_garbage_collection()** (2 connections) — `server/realtime/memory_monitor.py`
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
- **test_max_connection_age_default()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_max_connection_age_e2e()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- *... and 20 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (9 shared connections)
- [RateLimiter](RateLimiter.md) (8 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (4 shared connections)
- [connection_manager_health_cleanup.py](connection_manager_health_cleanup.py.md) (3 shared connections)
- [PerformanceTracker](PerformanceTracker.md) (3 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [User](User.md) (2 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (2 shared connections)
- [test_connection_cleaner.py](test_connection_cleaner.py.md) (1 shared connections)
- [test_statistics_aggregator.py](test_statistics_aggregator.py.md) (1 shared connections)

## Source Files

- `server/realtime/maintenance/__init__.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/memory_monitor.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 102 (88%)
- INFERRED: 14 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*