# HealthMonitor

> 34 nodes

## Key Concepts

- **HealthMonitor** (21 connections) — `server/realtime/monitoring/health_monitor.py`
- **UUID** (9 connections)
- **._process_single_connection()** (8 connections) — `server/realtime/monitoring/health_monitor.py`
- **.check_all_connections_health()** (6 connections) — `server/realtime/monitoring/health_monitor.py`
- **.periodic_health_check_task()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.check_player_connection_health()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._find_player_id_for_cleanup()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._cleanup_stale_connections()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **.start_periodic_checks()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._wait_for_task_cancellation()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **health_monitor()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_health_monitor_init_custom_intervals()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_connection_stale()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_websocket_open()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._validate_and_update_token()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **.stop_periodic_checks()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **Any** (2 connections)
- **Create a HealthMonitor instance.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Test HealthMonitor initialization with custom intervals.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Monitors connection health and manages periodic health checks.      This class p** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Initialize the health monitor.          Args:             is_websocket_open_call** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check the health of all connections for a player.          Args:             pla** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Find player_id for cleanup when metadata is missing.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check if connection is stale based on timeout.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- *... and 9 more nodes in this community*

## Relationships

- [health monitor](health_monitor.md) (3 shared connections)
- [test health monitor](test_health_monitor.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)

## Source Files

- `server/realtime/monitoring/health_monitor.py`
- `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Audit Trail

- EXTRACTED: 108 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*