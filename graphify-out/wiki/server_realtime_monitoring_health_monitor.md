# server realtime monitoring health monitor

> 99 nodes

## Key Concepts

- **PerformanceTracker** (26 connections) — `server/realtime/monitoring/performance_tracker.py`
- **statistics_aggregator.py** (25 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **HealthMonitor** (23 connections) — `server/realtime/monitoring/health_monitor.py`
- **health_monitor.py** (18 connections) — `server/realtime/monitoring/health_monitor.py`
- **test_statistics_aggregator.py** (15 connections) — `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`
- **performance_tracker.py** (14 connections) — `server/realtime/monitoring/performance_tracker.py`
- **UUID** (9 connections)
- **test_performance_tracker.py** (9 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **._process_single_connection()** (8 connections) — `server/realtime/monitoring/health_monitor.py`
- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
- **server/realtime/monitoring/__init__.py** (7 connections) — `server/realtime/monitoring/__init__.py`
- **.check_all_connections_health()** (6 connections) — `server/realtime/monitoring/health_monitor.py`
- **fixture** (6 connections)
- **.periodic_health_check_task()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.start_periodic_checks()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.check_player_connection_health()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._cleanup_stale_connections()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._find_player_id_for_cleanup()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._wait_for_task_cancellation()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **statistics_aggregator()** (4 connections) — `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`
- **PerformanceStats** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **._check_connection_stale()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_websocket_open()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **.stop_periodic_checks()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- *... and 74 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (12 shared connections)
- [deque](deque.md) (9 shared connections)
- [server realtime monitoring statistics aggregator](server_realtime_monitoring_statistics_aggregator.md) (7 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (5 shared connections)
- [server realtime connection manager methods](server_realtime_connection_manager_methods.md) (5 shared connections)
- [server tests unit realtime monitoring](server_tests_unit_realtime_monitoring.md) (4 shared connections)
- [server realtime connection models](server_realtime_connection_models.md) (4 shared connections)
- [server realtime connection establishment](server_realtime_connection_establishment.md) (2 shared connections)
- [server app tracked task manager](server_app_tracked_task_manager.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (2 shared connections)
- [server realtime memory monitor memorymonitor](server_realtime_memory_monitor_memorymonitor.md) (1 shared connections)
- [server realtime rate limiter py](server_realtime_rate_limiter_py.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 193 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*