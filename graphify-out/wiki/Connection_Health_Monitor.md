# Connection Health Monitor

> 27 nodes · cohesion 0.11

## Key Concepts

- **HealthMonitor** (23 connections) — `server/realtime/monitoring/health_monitor.py`
- **UUID** (10 connections) — `server/realtime/monitoring/health_monitor.py`
- **._process_single_connection()** (8 connections) — `server/realtime/monitoring/health_monitor.py`
- **__init__.py** (7 connections) — `server/realtime/monitoring/__init__.py`
- **.check_all_connections_health()** (6 connections) — `server/realtime/monitoring/health_monitor.py`
- **.periodic_health_check_task()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.start_periodic_checks()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **._cleanup_stale_connections()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._find_player_id_for_cleanup()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_connection_stale()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_websocket_open()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._validate_and_update_token()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **test_health_monitor_init_custom_intervals()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Find player_id for cleanup when metadata is missing.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check if connection is stale based on timeout.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check if WebSocket is actually open.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Validate token and update last validation time if needed.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Process health check for a single connection.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Clean up stale connections.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check health of all connections and clean up stale/dead ones.          This meth** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Periodic health check task that runs continuously.          This task:         -** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Start the periodic health check task.          This should be called during appl** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Monitors connection health and manages periodic health checks.      This class p** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Initialize the health monitor.          Args:             is_websocket_open_call** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- *... and 2 more nodes in this community*

## Relationships

- [[Realtime Health Monitor]] (7 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Room Occupant Events]] (4 shared connections)
- [[Realtime Performance Tracker]] (3 shared connections)
- [[Connection Statistics Aggregator]] (1 shared connections)

## Source Files

- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Audit Trail

- EXTRACTED: 98 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
