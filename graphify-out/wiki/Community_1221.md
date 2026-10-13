# Community 1221

> 10 nodes

## Key Concepts

- **._process_single_connection()** (8 connections) — `server/realtime/monitoring/health_monitor.py`
- **._find_player_id_for_cleanup()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_connection_stale()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_websocket_open()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._validate_and_update_token()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **Find player_id for cleanup when metadata is missing.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check if connection is stale based on timeout.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check if WebSocket is actually open.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Validate token and update last validation time if needed.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Process health check for a single connection.** (1 connections) — `server/realtime/monitoring/health_monitor.py`

## Relationships

- [Community 982](Community_982.md) (5 shared connections)
- [Community 1168](Community_1168.md) (3 shared connections)

## Source Files

- `server/realtime/monitoring/health_monitor.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*