# PerformanceTracker

> 69 nodes

## Key Concepts

- **PerformanceTracker** (26 connections) — `server/realtime/monitoring/performance_tracker.py`
- **HealthMonitor** (23 connections) — `server/realtime/monitoring/health_monitor.py`
- **get_global_tracked_manager()** (19 connections) — `server/app/tracked_task_manager.py`
- **health_monitor.py** (18 connections) — `server/realtime/monitoring/health_monitor.py`
- **UUID** (9 connections)
- **test_performance_tracker.py** (9 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **._process_single_connection()** (8 connections) — `server/realtime/monitoring/health_monitor.py`
- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
- **server/realtime/monitoring/__init__.py** (7 connections) — `server/realtime/monitoring/__init__.py`
- **.check_all_connections_health()** (6 connections) — `server/realtime/monitoring/health_monitor.py`
- **.periodic_health_check_task()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.start_periodic_checks()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.check_player_connection_health()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._cleanup_stale_connections()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._find_player_id_for_cleanup()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._wait_for_task_cancellation()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_connection_stale()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_websocket_open()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **.stop_periodic_checks()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._validate_and_update_token()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **.get_stats()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_connection_establishment()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_disconnection()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_health_check()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- *... and 44 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (21 shared connections)
- [test_health_monitor.py](test_health_monitor.py.md) (4 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (4 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (3 shared connections)
- [MessageQueue](MessageQueue.md) (2 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (2 shared connections)
- [._background_audit_cycle](_background_audit_cycle.md) (2 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (2 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (2 shared connections)
- [connection_establishment.py](connection_establishment.py.md) (1 shared connections)
- [.get_memory_status_report](get_memory_status_report.md) (1 shared connections)
- [.force_single_audit_cycle](force_single_audit_cycle.md) (1 shared connections)

## Source Files

- `server/app/tracked_task_manager.py`
- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/tests/unit/realtime/monitoring/test_performance_tracker.py`

## Audit Trail

- EXTRACTED: 137 (93%)
- INFERRED: 10 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*