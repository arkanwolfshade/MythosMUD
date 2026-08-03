# combat models rationale

> 3 nodes

## Key Concepts

- **.validate_coordinates()** (3 connections) — `server/services/coordinate_validator.py`
- **Any** (1 connections)
- **Validate coordinates for rooms in a zone/subzone and detect conflicts.** (1 connections) — `server/services/coordinate_validator.py`

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (1 shared connections)

## Source Files

- `server/services/coordinate_validator.py`

## Audit Trail

- EXTRACTED: 5 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*