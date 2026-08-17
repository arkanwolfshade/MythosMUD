# server realtime monitoring performance tracker

> 33 nodes

## Key Concepts

- **PerformanceTracker** (23 connections) — `server/realtime/monitoring/performance_tracker.py`
- **test_performance_tracker.py** (9 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
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
- **Record a session switch event. Args: duration_ms: Duration in milliseconds** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a health check event. Args: duration_ms: Duration in milliseconds** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Trim samples to prevent unbounded memory growth. Args: metric_key: Key in…** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Get comprehensive performance statistics with calculated averages. Returns:…** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Tracks performance metrics for connection management operations. This class…** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Initialize the performance tracker. Args: max_samples: Maximum number of…** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a connection establishment event. Args: connection_type: Type of…** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a message delivery event. Args: message_type: Type of message…** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- *... and 8 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server realtime connection initialization initialize](server_realtime_connection_initialization_initialize.md) (1 shared connections)
- [server realtime monitoring statistics aggregator](server_realtime_monitoring_statistics_aggregator.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/performance_tracker.py`
- `server/tests/unit/realtime/monitoring/test_performance_tracker.py`

## Audit Trail

- EXTRACTED: 44 (86%)
- INFERRED: 7 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*