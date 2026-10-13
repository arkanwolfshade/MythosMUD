# Community 982

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

- [Community 1168](Community_1168.md) (7 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (5 shared connections)
- [Community 1221](Community_1221.md) (5 shared connections)
- [Community 638](Community_638.md) (2 shared connections)
- [Connection Manager Broadcast](Connection_Manager_Broadcast.md) (1 shared connections)
- [Community 1180](Community_1180.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/health_monitor.py`
- `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Audit Trail

- EXTRACTED: 40 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*