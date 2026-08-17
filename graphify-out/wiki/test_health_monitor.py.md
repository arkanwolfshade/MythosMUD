# test_health_monitor.py

> 70 nodes

## Key Concepts

- **test_health_monitor.py** (27 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **HealthMonitor** (21 connections) — `server/realtime/monitoring/health_monitor.py`
- **asyncio** (12 connections)
- **UUID** (9 connections)
- **._process_single_connection()** (8 connections) — `server/realtime/monitoring/health_monitor.py`
- **.check_all_connections_health()** (6 connections) — `server/realtime/monitoring/health_monitor.py`
- **.periodic_health_check_task()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.start_periodic_checks()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **fixture** (5 connections)
- **.check_player_connection_health()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._cleanup_stale_connections()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._find_player_id_for_cleanup()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._wait_for_task_cancellation()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **health_monitor()** (4 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **._check_connection_stale()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_websocket_open()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **.stop_periodic_checks()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._validate_and_update_token()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **mock_cleanup_dead_websocket()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_is_websocket_open()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_performance_tracker()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_validate_token()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_all_connections_health()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_player_connection_health()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- *... and 45 more nodes in this community*

## Relationships

- [test_connection_session_management.py](test_connection_session_management.py.md) (3 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (2 shared connections)
- [PerformanceTracker](PerformanceTracker.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/health_monitor.py`
- `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Audit Trail

- EXTRACTED: 109 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*