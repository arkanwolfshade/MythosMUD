# Movement Performance Monitor

> 39 nodes · cohesion 0.07

## Key Concepts

- **MovementMonitor** (27 connections) — `server/game/movement_monitor.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **movement_monitor.py** (9 connections) — `server/game/movement_monitor.py`
- **reset_movement_monitor()** (8 connections) — `server/game/movement_monitor.py`
- **._handle_movement_error()** (7 connections) — `server/game/movement_service.py`
- **.get_alerts()** (6 connections) — `server/game/movement_monitor.py`
- **.get_metrics()** (6 connections) — `server/game/movement_monitor.py`
- **.get_performance_summary()** (5 connections) — `server/game/movement_monitor.py`
- **._check_alerts()** (4 connections) — `server/game/movement_monitor.py`
- **.log_performance_summary()** (4 connections) — `server/game/movement_monitor.py`
- **.record_movement_attempt()** (4 connections) — `server/game/movement_monitor.py`
- **.validate_room_integrity()** (4 connections) — `server/game/movement_monitor.py`
- **test_reset_movement_monitor()** (4 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **.record_integrity_check()** (3 connections) — `server/game/movement_monitor.py`
- **.reset_metrics()** (3 connections) — `server/game/movement_monitor.py`
- **movement_monitor()** (3 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_get_movement_monitor_returns_singleton()** (3 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **Any** (3 connections) — `server/game/movement_monitor.py`
- **Exception** (3 connections) — `server/game/movement_service.py`
- **.record_concurrent_movement()** (2 connections) — `server/game/movement_monitor.py`
- **UUID** (2 connections) — `server/game/movement_monitor.py`
- **Movement monitoring and validation system for MythosMUD.  This module provides c** (1 connections) — `server/game/movement_monitor.py`
- **Record concurrent movement count.** (1 connections) — `server/game/movement_monitor.py`
- **Record an integrity check result.** (1 connections) — `server/game/movement_monitor.py`
- **Validate room data integrity.          Returns a dictionary with validation resu** (1 connections) — `server/game/movement_monitor.py`
- *... and 14 more nodes in this community*

## Relationships

- [[Monitoring API Endpoints]] (12 shared connections)
- [[NPC Admin API]] (7 shared connections)
- [[Player Movement Service]] (6 shared connections)
- [[Movement Monitor Tests]] (6 shared connections)
- [[Distributed Event Bus]] (2 shared connections)
- [[Game Service Bundle]] (1 shared connections)

## Source Files

- `server/game/movement_monitor.py`
- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 135 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
