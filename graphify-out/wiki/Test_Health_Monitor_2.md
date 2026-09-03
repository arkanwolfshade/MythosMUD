# Test Health Monitor

> 27 nodes

## Key Concepts

- **test_health_monitor.py** (27 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **asyncio** (12 connections)
- **test_check_all_connections_health()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_player_connection_health()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_player_connection_health_no_websockets()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_player_connection_health_unhealthy()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_start_periodic_checks()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_stop_periodic_checks()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_all_connections_health_with_metadata()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_cleanup_stale_connections()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_health_monitor_init()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_periodic_health_check_task_cancel()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_process_single_connection_paths()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_validate_and_update_token()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_wait_for_task_cancellation()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_connection_stale()** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_websocket_open()** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_find_player_id_for_cleanup()** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_start_periodic_checks_already_running()** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Unit tests for health monitor. Tests the HealthMonitor class.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Test check_all_connections_health() checks all connections.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Test start_periodic_checks() starts periodic checks.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Test stop_periodic_checks() stops periodic checks.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Test HealthMonitor initialization.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Test check_player_connection_health() returns health status.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- *... and 2 more nodes in this community*

## Relationships

- [Test Health Monitor](Test_Health_Monitor.md) (5 shared connections)
- [Health Monitor](Health_Monitor.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*