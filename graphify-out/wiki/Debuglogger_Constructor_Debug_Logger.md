# Debuglogger Constructor Debug Logger

> 14 nodes

## Key Concepts

- **CoordinateValidator** (9 connections) — `server/services/coordinate_validator.py`
- **coordinate_validator.py** (7 connections) — `server/services/coordinate_validator.py`
- **.validate_coordinates()** (6 connections) — `server/services/coordinate_validator.py`
- **._fetch_conflicts()** (4 connections) — `server/services/coordinate_validator.py`
- **_conflict_from_row()** (3 connections) — `server/services/coordinate_validator.py`
- **Any** (3 connections)
- **.__init__()** (3 connections) — `server/services/coordinate_validator.py`
- **_zone_pattern()** (2 connections) — `server/services/coordinate_validator.py`
- **._count_coordinated_rooms()** (2 connections) — `server/services/coordinate_validator.py`
- **AsyncSession** (1 connections)
- **Coordinate validation service for ASCII maps.  This module provides conflict det** (1 connections) — `server/services/coordinate_validator.py`
- **Validates room coordinates and detects conflicts.      A conflict occurs when mu** (1 connections) — `server/services/coordinate_validator.py`
- **Initialize coordinate validator.          Args:             session: Database se** (1 connections) — `server/services/coordinate_validator.py`
- **Validate coordinates for rooms in a zone/subzone and detect conflicts.** (1 connections) — `server/services/coordinate_validator.py`

## Relationships

- [Container Persistence Ops](Container_Persistence_Ops.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)

## Source Files

- `server/services/coordinate_validator.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*