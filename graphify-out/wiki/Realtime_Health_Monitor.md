# Realtime Health Monitor

> 26 nodes · cohesion 0.08

## Key Concepts

- **test_health_monitor.py** (15 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **health_monitor()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_cleanup_dead_websocket()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_is_websocket_open()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_performance_tracker()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_validate_token()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_all_connections_health()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_player_connection_health()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_player_connection_health_no_websockets()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_player_connection_health_unhealthy()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_health_monitor_init()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_start_periodic_checks()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_stop_periodic_checks()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Unit tests for health monitor.  Tests the HealthMonitor class.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Test check_all_connections_health() checks all connections.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Test start_periodic_checks() starts periodic checks.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Test stop_periodic_checks() stops periodic checks.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Create a mock is_websocket_open callback.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Create a mock validate_token callback.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Create a mock cleanup_dead_websocket callback.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Create a mock performance tracker.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Create a HealthMonitor instance.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Test HealthMonitor initialization.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Test check_player_connection_health() returns health status.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Test check_player_connection_health() when player has no websockets.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- *... and 1 more nodes in this community*

## Relationships

- [[Connection Health Monitor]] (3 shared connections)

## Source Files

- `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
