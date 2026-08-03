# event realtime publisher

> 28 nodes

## Key Concepts

- **UUID** (9 connections)
- **._process_single_connection()** (8 connections) — `server/realtime/monitoring/health_monitor.py`
- **.check_all_connections_health()** (6 connections) — `server/realtime/monitoring/health_monitor.py`
- **.periodic_health_check_task()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.start_periodic_checks()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.check_player_connection_health()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._find_player_id_for_cleanup()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._cleanup_stale_connections()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._wait_for_task_cancellation()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_connection_stale()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_websocket_open()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._validate_and_update_token()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **.stop_periodic_checks()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **Any** (2 connections)
- **Initialize the health monitor.          Args:             is_websocket_open_call** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check the health of all connections for a player.          Args:             pla** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Find player_id for cleanup when metadata is missing.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check if connection is stale based on timeout.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check if WebSocket is actually open.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Validate token and update last validation time if needed.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Process health check for a single connection.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Clean up stale connections.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check health of all connections and clean up stale/dead ones.          This meth** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Periodic health check task that runs continuously.          This task:         -** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- *... and 3 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (14 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/health_monitor.py`

## Audit Trail

- EXTRACTED: 79 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*