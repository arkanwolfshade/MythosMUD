# Player Death Service Tests

> 4 nodes · cohesion 0.04

## Key Concepts

- **UUID** (20 connections) — `server/services/lucidity_service.py`
- **Any** (8 connections) — `server/commands/debrief_command.py`
- **datetime** (4 connections) — `server/services/active_lucidity_service.py`
- **AsyncSession** (3 connections) — `server/services/active_lucidity_service.py`

## Relationships

- [Lucidity State Models](Lucidity_State_Models.md) (1 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/services/active_lucidity_service.py`
- `server/services/lucidity_service.py`

## Audit Trail

- EXTRACTED: 24 (69%)
- INFERRED: 11 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*