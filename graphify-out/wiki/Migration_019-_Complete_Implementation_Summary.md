# Migration 019: Complete Implementation Summary

> 27 nodes

## Key Concepts

- **MovementMonitor** (18 connections) — `server/game/movement_monitor.py`
- **.get_alerts()** (6 connections) — `server/game/movement_monitor.py`
- **.get_metrics()** (6 connections) — `server/game/movement_monitor.py`
- **.get_performance_summary()** (5 connections) — `server/game/movement_monitor.py`
- **.validate_room_integrity()** (5 connections) — `server/game/movement_monitor.py`
- **._check_alerts()** (4 connections) — `server/game/movement_monitor.py`
- **.log_performance_summary()** (4 connections) — `server/game/movement_monitor.py`
- **.record_movement_attempt()** (4 connections) — `server/game/movement_monitor.py`
- **Any** (4 connections)
- **._collect_room_player_map()** (3 connections) — `server/game/movement_monitor.py`
- **.__init__()** (3 connections) — `server/game/movement_monitor.py`
- **.record_integrity_check()** (3 connections) — `server/game/movement_monitor.py`
- **.record_concurrent_movement()** (2 connections) — `server/game/movement_monitor.py`
- **.reset_metrics()** (2 connections) — `server/game/movement_monitor.py`
- **UUID** (2 connections)
- **Record concurrent movement count.** (1 connections) — `server/game/movement_monitor.py`
- **Record an integrity check result.** (1 connections) — `server/game/movement_monitor.py`
- **Validate players are not in multiple rooms.** (1 connections) — `server/game/movement_monitor.py`
- **Get comprehensive movement metrics.** (1 connections) — `server/game/movement_monitor.py`
- **Get current alerts based on thresholds.** (1 connections) — `server/game/movement_monitor.py`
- **Comprehensive monitoring system for the movement system. This class provides: -…** (1 connections) — `server/game/movement_monitor.py`
- **Check for alerts and log them.** (1 connections) — `server/game/movement_monitor.py`
- **Reset all metrics (useful for testing).** (1 connections) — `server/game/movement_monitor.py`
- **Get a formatted performance summary for API responses. This method encapsulates…** (1 connections) — `server/game/movement_monitor.py`
- **Log a comprehensive performance summary.** (1 connections) — `server/game/movement_monitor.py`
- *... and 2 more nodes in this community*

## Relationships

- [test_skill_service.py](test_skill_service.py.md) (4 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)

## Source Files

- `server/game/movement_monitor.py`

## Audit Trail

- EXTRACTED: 44 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*