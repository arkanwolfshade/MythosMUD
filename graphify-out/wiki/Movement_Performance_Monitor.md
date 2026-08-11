# Movement Performance Monitor

> 19 nodes

## Key Concepts

- **.get_metrics()** (6 connections) — `server/game/movement_monitor.py`
- **.get_alerts()** (6 connections) — `server/game/movement_monitor.py`
- **.validate_room_integrity()** (5 connections) — `server/game/movement_monitor.py`
- **.get_performance_summary()** (5 connections) — `server/game/movement_monitor.py`
- **.record_movement_attempt()** (4 connections) — `server/game/movement_monitor.py`
- **Any** (4 connections)
- **._check_alerts()** (4 connections) — `server/game/movement_monitor.py`
- **.log_performance_summary()** (4 connections) — `server/game/movement_monitor.py`
- **.record_integrity_check()** (3 connections) — `server/game/movement_monitor.py`
- **._collect_room_player_map()** (3 connections) — `server/game/movement_monitor.py`
- **UUID** (2 connections)
- **Record a movement attempt with metrics.** (1 connections) — `server/game/movement_monitor.py`
- **Record an integrity check result.** (1 connections) — `server/game/movement_monitor.py`
- **Validate players are not in multiple rooms.** (1 connections) — `server/game/movement_monitor.py`
- **Get comprehensive movement metrics.** (1 connections) — `server/game/movement_monitor.py`
- **Get current alerts based on thresholds.** (1 connections) — `server/game/movement_monitor.py`
- **Check for alerts and log them.** (1 connections) — `server/game/movement_monitor.py`
- **Get a formatted performance summary for API responses.          This method en** (1 connections) — `server/game/movement_monitor.py`
- **Log a comprehensive performance summary.** (1 connections) — `server/game/movement_monitor.py`

## Relationships

- [Command Field Validators](Command_Field_Validators.md) (10 shared connections)

## Source Files

- `server/game/movement_monitor.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*