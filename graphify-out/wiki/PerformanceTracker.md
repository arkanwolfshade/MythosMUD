# PerformanceTracker

> 40 nodes

## Key Concepts

- **PerformanceTracker** (25 connections) — `server/realtime/monitoring/performance_tracker.py`
- **performance_tracker.py** (13 connections) — `server/realtime/monitoring/performance_tracker.py`
- **test_performance_tracker.py** (9 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
- **server/realtime/monitoring/__init__.py** (7 connections) — `server/realtime/monitoring/__init__.py`
- **PerformanceStats** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.get_stats()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
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
- **Any** (1 connections)
- **TypedDict** (1 connections)
- **Monitoring components for connection management. This package provides modular…** (1 connections) — `server/realtime/monitoring/__init__.py`
- **Performance tracking for connection management. This module provides…** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a session switch event. Args: duration_ms: Duration in milliseconds** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a health check event. Args: duration_ms: Duration in milliseconds** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- *... and 15 more nodes in this community*

## Relationships

- [RoomSubscriptionManager](RoomSubscriptionManager.md) (3 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (3 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (2 shared connections)
- [test_health_monitor.py](test_health_monitor.py.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/tests/unit/realtime/monitoring/test_performance_tracker.py`

## Audit Trail

- EXTRACTED: 64 (90%)
- INFERRED: 7 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*