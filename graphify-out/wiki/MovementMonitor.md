# MovementMonitor

> 22 nodes

## Key Concepts

- **MovementMonitor** (22 connections) — `server/game/movement_monitor.py`
- **.get_alerts()** (6 connections) — `server/game/movement_monitor.py`
- **.get_metrics()** (6 connections) — `server/game/movement_monitor.py`
- **.get_performance_summary()** (5 connections) — `server/game/movement_monitor.py`
- **.validate_room_integrity()** (5 connections) — `server/game/movement_monitor.py`
- **.log_performance_summary()** (4 connections) — `server/game/movement_monitor.py`
- **Any** (4 connections)
- **._collect_room_player_map()** (3 connections) — `server/game/movement_monitor.py`
- **.__init__()** (3 connections) — `server/game/movement_monitor.py`
- **.record_integrity_check()** (3 connections) — `server/game/movement_monitor.py`
- **.record_concurrent_movement()** (2 connections) — `server/game/movement_monitor.py`
- **.reset_metrics()** (2 connections) — `server/game/movement_monitor.py`
- **Record concurrent movement count.** (1 connections) — `server/game/movement_monitor.py`
- **Record an integrity check result.** (1 connections) — `server/game/movement_monitor.py`
- **Validate players are not in multiple rooms.** (1 connections) — `server/game/movement_monitor.py`
- **Get comprehensive movement metrics.** (1 connections) — `server/game/movement_monitor.py`
- **Get current alerts based on thresholds.** (1 connections) — `server/game/movement_monitor.py`
- **Comprehensive monitoring system for the movement system. This class provides: -…** (1 connections) — `server/game/movement_monitor.py`
- **Reset all metrics (useful for testing).** (1 connections) — `server/game/movement_monitor.py`
- **Get a formatted performance summary for API responses. This method encapsulates…** (1 connections) — `server/game/movement_monitor.py`
- **Log a comprehensive performance summary.** (1 connections) — `server/game/movement_monitor.py`
- **Initialize the movement monitor with empty metrics.** (1 connections) — `server/game/movement_monitor.py`

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [._check_alerts](_check_alerts.md) (3 shared connections)
- [test_movement_monitor.py](test_movement_monitor.py.md) (1 shared connections)
- [movement_monitor](movement_monitor.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/game/movement_monitor.py`

## Audit Trail

- EXTRACTED: 40 (91%)
- INFERRED: 4 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*