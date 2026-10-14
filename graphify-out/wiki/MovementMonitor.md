# MovementMonitor

> 35 nodes

## Key Concepts

- **MovementMonitor** (22 connections) — `server/game/movement_monitor.py`
- **asyncio** (15 connections)
- **.get_alerts()** (6 connections) — `server/game/movement_monitor.py`
- **.get_metrics()** (6 connections) — `server/game/movement_monitor.py`
- **.get_performance_summary()** (5 connections) — `server/game/movement_monitor.py`
- **.validate_room_integrity()** (5 connections) — `server/game/movement_monitor.py`
- **._check_alerts()** (4 connections) — `server/game/movement_monitor.py`
- **.log_performance_summary()** (4 connections) — `server/game/movement_monitor.py`
- **.record_movement_attempt()** (4 connections) — `server/game/movement_monitor.py`
- **test_get_movement_metrics_logged_http_on_failure()** (4 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_movement_metrics_uses_monitor()** (4 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_system_alerts_returns_counts()** (4 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_validate_room_integrity_builds_room_map()** (4 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Any** (4 connections)
- **._collect_room_player_map()** (3 connections) — `server/game/movement_monitor.py`
- **.__init__()** (3 connections) — `server/game/movement_monitor.py`
- **.record_integrity_check()** (3 connections) — `server/game/movement_monitor.py`
- **test_get_performance_summary_delegates_to_monitor()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_task_metrics_from_registry()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_reset_movement_metrics_calls_reset()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **.record_concurrent_movement()** (2 connections) — `server/game/movement_monitor.py`
- **.reset_metrics()** (2 connections) — `server/game/movement_monitor.py`
- **UUID** (2 connections)
- **Record concurrent movement count.** (1 connections) — `server/game/movement_monitor.py`
- **Record an integrity check result.** (1 connections) — `server/game/movement_monitor.py`
- *... and 10 more nodes in this community*

## Relationships

- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (16 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (10 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_movement_monitor.py](test_movement_monitor.py.md) (2 shared connections)

## Source Files

- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 74 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*