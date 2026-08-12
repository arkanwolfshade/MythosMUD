# Movement Performance Monitor

> 33 nodes

## Key Concepts

- **MovementMonitor** (22 connections) — `server/game/movement_monitor.py`
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
- **movement_monitor()** (3 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **UUID** (2 connections)
- **.record_concurrent_movement()** (2 connections) — `server/game/movement_monitor.py`
- **Comprehensive monitoring system for the movement system.      This class provi** (1 connections) — `server/game/movement_monitor.py`
- **Initialize the movement monitor with empty metrics.** (1 connections) — `server/game/movement_monitor.py`
- **Record a movement attempt with metrics.** (1 connections) — `server/game/movement_monitor.py`
- **Record concurrent movement count.** (1 connections) — `server/game/movement_monitor.py`
- **Record an integrity check result.** (1 connections) — `server/game/movement_monitor.py`
- **Validate players are not in multiple rooms.** (1 connections) — `server/game/movement_monitor.py`
- **Get comprehensive movement metrics.** (1 connections) — `server/game/movement_monitor.py`
- *... and 8 more nodes in this community*

## Relationships

- [Command Field Validators](Command_Field_Validators.md) (11 shared connections)
- [Cursor Subagents Docs](Cursor_Subagents_Docs.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/game/movement_monitor.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 106 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*