# Lizard Complexity Findings

> 12 nodes

## Key Concepts

- **CoordinateValidator** (9 connections) — `server/services/coordinate_validator.py`
- **.validate_coordinates()** (6 connections) — `server/services/coordinate_validator.py`
- **._fetch_conflicts()** (4 connections) — `server/services/coordinate_validator.py`
- **_conflict_from_row()** (3 connections) — `server/services/coordinate_validator.py`
- **Any** (3 connections)
- **.__init__()** (3 connections) — `server/services/coordinate_validator.py`
- **_zone_pattern()** (2 connections) — `server/services/coordinate_validator.py`
- **._count_coordinated_rooms()** (2 connections) — `server/services/coordinate_validator.py`
- **AsyncSession** (1 connections)
- **Validates room coordinates and detects conflicts.      A conflict occurs when mu** (1 connections) — `server/services/coordinate_validator.py`
- **Initialize coordinate validator.          Args:             session: Database se** (1 connections) — `server/services/coordinate_validator.py`
- **Validate coordinates for rooms in a zone/subzone and detect conflicts.** (1 connections) — `server/services/coordinate_validator.py`

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (6 shared connections)

## Source Files

- `server/services/coordinate_validator.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*