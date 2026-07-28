# Movement Performance Monitor

> 36 nodes · cohesion 0.08

## Key Concepts

- **MovementMonitor** (21 connections) — `server/game/movement_monitor.py`
- **movement_monitor.py** (12 connections) — `server/game/movement_monitor.py`
- **reset_movement_monitor()** (8 connections) — `server/game/movement_monitor.py`
- **.get_alerts()** (6 connections) — `server/game/movement_monitor.py`
- **.get_metrics()** (6 connections) — `server/game/movement_monitor.py`
- **.get_performance_summary()** (5 connections) — `server/game/movement_monitor.py`
- **._check_alerts()** (4 connections) — `server/game/movement_monitor.py`
- **.log_performance_summary()** (4 connections) — `server/game/movement_monitor.py`
- **.record_movement_attempt()** (4 connections) — `server/game/movement_monitor.py`
- **.validate_room_integrity()** (4 connections) — `server/game/movement_monitor.py`
- **test_reset_movement_monitor()** (4 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **.__init__()** (3 connections) — `server/game/movement_monitor.py`
- **.record_integrity_check()** (3 connections) — `server/game/movement_monitor.py`
- **.reset_metrics()** (3 connections) — `server/game/movement_monitor.py`
- **Any** (3 connections)
- **test_get_system_alerts_returns_counts()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_validate_room_integrity_builds_room_map()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **movement_monitor()** (3 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **.record_concurrent_movement()** (2 connections) — `server/game/movement_monitor.py`
- **UUID** (2 connections)
- **Movement monitoring and validation system for MythosMUD.  This module provides c** (1 connections) — `server/game/movement_monitor.py`
- **Record concurrent movement count.** (1 connections) — `server/game/movement_monitor.py`
- **Record an integrity check result.** (1 connections) — `server/game/movement_monitor.py`
- **Validate room data integrity.          Returns a dictionary with validation resu** (1 connections) — `server/game/movement_monitor.py`
- **Get comprehensive movement metrics.** (1 connections) — `server/game/movement_monitor.py`
- *... and 11 more nodes in this community*

## Relationships

- [Monitoring Response Models](Monitoring_Response_Models.md) (13 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [Admin Status Commands](Admin_Status_Commands.md) (5 shared connections)

## Source Files

- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 119 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*