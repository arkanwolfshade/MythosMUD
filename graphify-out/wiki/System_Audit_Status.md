# System Audit Status

> 14 nodes · cohesion 0.19

## Key Concepts

- **HealthMonitor** (23 connections) — `server/realtime/monitoring/health_monitor.py`
- **._process_single_connection()** (8 connections) — `server/realtime/monitoring/health_monitor.py`
- **._find_player_id_for_cleanup()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_connection_stale()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_websocket_open()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._validate_and_update_token()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **health_monitor()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Find player_id for cleanup when metadata is missing.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check if connection is stale based on timeout.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Check if WebSocket is actually open.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Validate token and update last validation time if needed.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Process health check for a single connection.** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Monitors connection health and manages periodic health checks.      This class p** (1 connections) — `server/realtime/monitoring/health_monitor.py`
- **Create a HealthMonitor instance.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Relationships

- [Connection Health Monitor](Connection_Health_Monitor.md) (8 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Community 1551](Community_1551.md) (3 shared connections)
- [Environmental Container Scenario](Environmental_Container_Scenario.md) (2 shared connections)
- [Whisper Reply Command Tests](Whisper_Reply_Command_Tests.md) (1 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (1 shared connections)
- [Cursor Agents Readme](Cursor_Agents_Readme.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/health_monitor.py`
- `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Audit Trail

- EXTRACTED: 53 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*