# Movement Performance Monitor

> 20 nodes

## Key Concepts

- **MovementMonitor** (22 connections) — `server/game/movement_monitor.py`
- **.get_metrics()** (6 connections) — `server/game/movement_monitor.py`
- **.get_alerts()** (6 connections) — `server/game/movement_monitor.py`
- **.validate_room_integrity()** (5 connections) — `server/game/movement_monitor.py`
- **.get_performance_summary()** (5 connections) — `server/game/movement_monitor.py`
- **Any** (4 connections)
- **.log_performance_summary()** (4 connections) — `server/game/movement_monitor.py`
- **.__init__()** (3 connections) — `server/game/movement_monitor.py`
- **.record_integrity_check()** (3 connections) — `server/game/movement_monitor.py`
- **._collect_room_player_map()** (3 connections) — `server/game/movement_monitor.py`
- **.record_concurrent_movement()** (2 connections) — `server/game/movement_monitor.py`
- **Comprehensive monitoring system for the movement system.      This class provi** (1 connections) — `server/game/movement_monitor.py`
- **Initialize the movement monitor with empty metrics.** (1 connections) — `server/game/movement_monitor.py`
- **Record concurrent movement count.** (1 connections) — `server/game/movement_monitor.py`
- **Record an integrity check result.** (1 connections) — `server/game/movement_monitor.py`
- **Validate players are not in multiple rooms.** (1 connections) — `server/game/movement_monitor.py`
- **Get comprehensive movement metrics.** (1 connections) — `server/game/movement_monitor.py`
- **Get current alerts based on thresholds.** (1 connections) — `server/game/movement_monitor.py`
- **Get a formatted performance summary for API responses.          This method en** (1 connections) — `server/game/movement_monitor.py`
- **Log a comprehensive performance summary.** (1 connections) — `server/game/movement_monitor.py`

## Relationships

- [Monitoring Response Models](Monitoring_Response_Models.md) (7 shared connections)
- [Schemas Unified Room](Schemas_Unified_Room.md) (3 shared connections)
- [Development 5 Scripts](Development_5_Scripts.md) (1 shared connections)
- [Cursor Subagents Docs](Cursor_Subagents_Docs.md) (1 shared connections)
- [test_profession_meets_stat_requirements_invalid_json](test_profession_meets_stat_requirements_invalid_json.md) (1 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/game/movement_monitor.py`

## Audit Trail

- EXTRACTED: 72 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*