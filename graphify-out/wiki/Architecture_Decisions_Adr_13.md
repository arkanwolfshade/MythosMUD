# Architecture Decisions Adr

> 2 nodes · cohesion 1.00

## Key Concepts

- **test_occupant_formatter_process_dict_occupant_for_update_fallback_name()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_dict_occupant_for_update() processes fallback na** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`

## Relationships

- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [UI Animation Testing Standards](UI_Animation_Testing_Standards.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_occupant_formatter.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*