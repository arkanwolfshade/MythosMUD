# ._check_alerts

> 5 nodes

## Key Concepts

- **._check_alerts()** (4 connections) — `server/game/movement_monitor.py`
- **.record_movement_attempt()** (4 connections) — `server/game/movement_monitor.py`
- **UUID** (2 connections)
- **Check for alerts and log them.** (1 connections) — `server/game/movement_monitor.py`
- **Record a movement attempt with metrics.** (1 connections) — `server/game/movement_monitor.py`

## Relationships

- [MovementMonitor](MovementMonitor.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)

## Source Files

- `server/game/movement_monitor.py`

## Audit Trail

- EXTRACTED: 8 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*