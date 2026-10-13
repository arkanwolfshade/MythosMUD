# Community 1168

> 11 nodes

## Key Concepts

- **UUID** (10 connections)
- **.check_all_connections_health()** (6 connections) — `server/realtime/monitoring/health_monitor.py`
- **.periodic_health_check_task()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **._cleanup_stale_connections()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **.start_periodic_checks()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **Clean up stale connections.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check health of all connections and clean up stale/dead ones. This method: -…** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Periodic health check task that runs continuously. This task: - Runs health…** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Start the periodic health check task. This should be called during application…** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Initialize the health monitor. Args: is_websocket_open_callback: Callback to…** (1 connections) — `server/realtime/monitoring/health_monitor.py`

## Relationships

- [Community 982](Community_982.md) (7 shared connections)
- [Community 1221](Community_1221.md) (3 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/health_monitor.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*