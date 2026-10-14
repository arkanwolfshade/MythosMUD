# PerformanceTracker

> 40 nodes

## Key Concepts

- **PerformanceTracker** (28 connections) — `server/realtime/monitoring/performance_tracker.py`
- **test_performance_tracker.py** (9 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
- **server/realtime/monitoring/__init__.py** (7 connections) — `server/realtime/monitoring/__init__.py`
- **._build_stats_response()** (5 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.get_stats()** (5 connections) — `server/realtime/monitoring/performance_tracker.py`
- **._calculate_stats()** (4 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_connection_establishment()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_disconnection()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_health_check()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_message_delivery()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_session_switch()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **test_get_stats_calculates_averages()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_get_stats_empty_returns_zeros()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_get_stats_error_path_returns_error_dict()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_get_stats_non_websocket_connections_excluded_from_websocket_stats()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_record_events_increase_counters()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_trim_samples_keeps_max_samples()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **.__init__()** (2 connections) — `server/realtime/monitoring/performance_tracker.py`
- **ndarray** (2 connections)
- **Any** (2 connections)
- **Monitoring components for connection management. This package provides modular…** (1 connections) — `server/realtime/monitoring/__init__.py`
- **Record a session switch event. Args: duration_ms: Duration in milliseconds** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a health check event. Args: duration_ms: Duration in milliseconds** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Trim samples to prevent unbounded memory growth. Args: metric_key: Key in…** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- *... and 15 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (4 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (2 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (1 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (1 shared connections)
- [HealthMonitor](HealthMonitor.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/tests/unit/realtime/monitoring/test_performance_tracker.py`

## Audit Trail

- EXTRACTED: 68 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*