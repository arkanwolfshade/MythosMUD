# force_memory_cleanup

> 10 nodes

## Key Concepts

- **force_memory_cleanup()** (10 connections) — `server/api/monitoring.py`
- **reset_metrics()** (10 connections) — `server/api/monitoring.py`
- **reset_movement_monitor()** (7 connections) — `server/game/movement_monitor.py`
- **test_reset_movement_monitor()** (4 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **MessageResponse** (2 connections)
- **post** (2 connections)
- **Reset all movement metrics (admin only).** (1 connections) — `server/api/monitoring.py`
- **Force immediate memory cleanup (admin only).** (1 connections) — `server/api/monitoring.py`
- **Reset the global movement monitor (useful for testing).** (1 connections) — `server/game/movement_monitor.py`
- **Test reset_movement_monitor() resets global monitor.** (1 connections) — `server/tests/unit/game/test_movement_monitor.py`

## Relationships

- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (8 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [MovementMonitor](MovementMonitor.md) (2 shared connections)
- [test_movement_monitor.py](test_movement_monitor.py.md) (2 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/game/movement_monitor.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 27 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*