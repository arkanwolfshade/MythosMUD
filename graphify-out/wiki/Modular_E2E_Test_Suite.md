# Modular E2E Test Suite

> 7 nodes

## Key Concepts

- **.__init__()** (6 connections) — `server/models/lucidity.py`
- **.__init__()** (5 connections) — `server/models/lucidity.py`
- **.__init__()** (5 connections) — `server/models/lucidity.py`
- **Any** (3 connections)
- **Initialize LucidityAdjustmentLog with defaults.** (1 connections) — `server/models/lucidity.py`
- **Initialize LucidityExposureState with defaults.** (1 connections) — `server/models/lucidity.py`
- **Initialize PlayerLucidity with defaults.** (1 connections) — `server/models/lucidity.py`

## Relationships

- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (3 shared connections)

## Source Files

- `server/models/lucidity.py`

## Audit Trail

- EXTRACTED: 11 (79%)
- INFERRED: 3 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*