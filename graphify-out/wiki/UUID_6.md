# UUID

> 11 nodes · cohesion 0.24

## Key Concepts

- **UUID** (9 connections)
- **.check_all_connections_health()** (6 connections) — `server/realtime/monitoring/health_monitor.py`
- **.periodic_health_check_task()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.start_periodic_checks()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **._cleanup_stale_connections()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **Clean up stale connections.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check health of all connections and clean up stale/dead ones.          This meth** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Periodic health check task that runs continuously.          This task:         -** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Start the periodic health check task.          This should be called during appl** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Initialize the health monitor.          Args:             is_websocket_open_call** (1 connections) — `server/realtime/monitoring/health_monitor.py`

## Relationships

- [HealthMonitor](HealthMonitor.md) (8 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [Community 1551](Community_1551.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/health_monitor.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*