# HealthMonitor

> 15 nodes

## Key Concepts

- **HealthMonitor** (25 connections) — `server/realtime/monitoring/health_monitor.py`
- **.check_player_connection_health()** (6 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_single_websocket_health()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **._determine_overall_health()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._wait_for_task_cancellation()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **Any** (4 connections)
- **.stop_periodic_checks()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **test_health_monitor_init_custom_intervals()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Classify overall connection health from healthy/unhealthy websocket counts.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check the health of all connections for a player. Args: player_id: The player's…** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Monitors connection health and manages periodic health checks. This class…** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Stop the periodic health check task. This should be called during application…** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Wait for a task to be cancelled, with timeout.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check one WebSocket's health, updating health_status in place and cleaning up…** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Test HealthMonitor initialization with custom intervals.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Relationships

- [UUID](UUID.md) (7 shared connections)
- [._process_single_connection](_process_single_connection.md) (5 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_health_monitor.py](test_health_monitor.py.md) (2 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (1 shared connections)
- [PerformanceTracker](PerformanceTracker.md) (1 shared connections)
- [fixture](fixture.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/health_monitor.py`
- `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Audit Trail

- EXTRACTED: 40 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*