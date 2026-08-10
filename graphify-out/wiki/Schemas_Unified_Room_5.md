# Schemas Unified Room

> 5 nodes

## Key Concepts

- **.record_movement_attempt()** (4 connections) — `server/game/movement_monitor.py`
- **._check_alerts()** (4 connections) — `server/game/movement_monitor.py`
- **UUID** (2 connections)
- **Record a movement attempt with metrics.** (1 connections) — `server/game/movement_monitor.py`
- **Check for alerts and log them.** (1 connections) — `server/game/movement_monitor.py`

## Relationships

- [Movement Performance Monitor](Movement_Performance_Monitor.md) (3 shared connections)
- [Monitoring Response Models](Monitoring_Response_Models.md) (1 shared connections)

## Source Files

- `server/game/movement_monitor.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*