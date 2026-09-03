# Health Monitor

> 7 nodes

## Key Concepts

- **.check_player_connection_health()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._wait_for_task_cancellation()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **.stop_periodic_checks()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **Any** (2 connections)
- **Stop the periodic health check task. This should be called during application…** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Wait for a task to be cancelled, with timeout.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check the health of all connections for a player. Args: player_id: The player's…** (1 connections) — `server/realtime/monitoring/health_monitor.py`

## Relationships

- [Health Monitor](Health_Monitor.md) (4 shared connections)

## Source Files

- `server/realtime/monitoring/health_monitor.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*