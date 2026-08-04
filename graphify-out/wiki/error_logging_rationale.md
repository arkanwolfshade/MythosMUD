# error logging rationale

> 5 nodes

## Key Concepts

- **exception_metrics.py** (4 connections) — `server/monitoring/exception_metrics.py`
- **get_summary()** (3 connections) — `server/monitoring/exception_metrics.py`
- **Any** (1 connections)
- **Exception metrics tracking for monitoring.  This module provides thread-safe exc** (1 connections) — `server/monitoring/exception_metrics.py`
- **Get a summary of exception counts.      Returns:         dict[str, Any]: Diction** (1 connections) — `server/monitoring/exception_metrics.py`

## Relationships

- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_metrics.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*