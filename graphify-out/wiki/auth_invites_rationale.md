# auth invites rationale

> 7 nodes

## Key Concepts

- **.__init__()** (5 connections) — `server/models/lucidity.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **Any** (3 connections)
- **Initialize PlayerLucidity with defaults.** (1 connections) — `server/models/lucidity.py`
- **Initialize LucidityAdjustmentLog with defaults.** (1 connections) — `server/models/lucidity.py`
- **Initialize LucidityExposureState with defaults.** (1 connections) — `server/models/lucidity.py`

## Relationships

- [world models rationale](world_models_rationale.md) (2 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (1 shared connections)

## Source Files

- `server/models/lucidity.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*