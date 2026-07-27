# Realtime Health Monitor

> 7 nodes · cohesion 0.29

## Key Concepts

- **.check_player_connection_health()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._wait_for_task_cancellation()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **.stop_periodic_checks()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **Any** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **Stop the periodic health check task.          This should be called during appli** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Wait for a task to be cancelled, with timeout.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check the health of all connections for a player.          Args:             pla** (1 connections) — `server/realtime/monitoring/health_monitor.py`

## Relationships

- [[Connection Health Monitor]] (4 shared connections)
- [[Realtime Performance Tracker]] (1 shared connections)

## Source Files

- `server/realtime/monitoring/health_monitor.py`

## Audit Trail

- EXTRACTED: 16 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
