# Movement Performance Monitor

> 44 nodes

## Key Concepts

- **MovementMonitor** (22 connections) — `server/game/movement_monitor.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **movement_monitor.py** (12 connections) — `server/game/movement_monitor.py`
- **get_movement_metrics()** (9 connections) — `server/api/monitoring.py`
- **reset_movement_monitor()** (8 connections) — `server/game/movement_monitor.py`
- **.get_metrics()** (6 connections) — `server/game/movement_monitor.py`
- **.get_alerts()** (6 connections) — `server/game/movement_monitor.py`
- **.validate_room_integrity()** (5 connections) — `server/game/movement_monitor.py`
- **.get_performance_summary()** (5 connections) — `server/game/movement_monitor.py`
- **.record_movement_attempt()** (4 connections) — `server/game/movement_monitor.py`
- **Any** (4 connections)
- **._check_alerts()** (4 connections) — `server/game/movement_monitor.py`
- **.log_performance_summary()** (4 connections) — `server/game/movement_monitor.py`
- **test_reset_movement_monitor()** (4 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **.__init__()** (3 connections) — `server/game/movement_monitor.py`
- **.record_integrity_check()** (3 connections) — `server/game/movement_monitor.py`
- **._collect_room_player_map()** (3 connections) — `server/game/movement_monitor.py`
- **.reset_metrics()** (3 connections) — `server/game/movement_monitor.py`
- **test_get_movement_metrics_uses_monitor()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_movement_metrics_logged_http_on_failure()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **movement_monitor()** (3 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_get_movement_monitor_returns_singleton()** (3 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **UUID** (2 connections)
- **.record_concurrent_movement()** (2 connections) — `server/game/movement_monitor.py`
- **MetricsResponse** (1 connections)
- *... and 19 more nodes in this community*

## Relationships

- [Command Field Validators](Command_Field_Validators.md) (16 shared connections)
- [Cursor Subagents Docs](Cursor_Subagents_Docs.md) (7 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (5 shared connections)
- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (4 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 154 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*