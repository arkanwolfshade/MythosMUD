# _apply_exploration_filter_if_needed

> 21 nodes

## Key Concepts

- **CoordinateValidator** (11 connections) — `server/services/coordinate_validator.py`
- **coordinate_validator.py** (9 connections) — `server/services/coordinate_validator.py`
- **test_coordinate_validator.py** (7 connections) — `server/tests/unit/services/test_coordinate_validator.py`
- **.validate_coordinates()** (6 connections) — `server/services/coordinate_validator.py`
- **._fetch_conflicts()** (4 connections) — `server/services/coordinate_validator.py`
- **_conflict_from_row()** (3 connections) — `server/services/coordinate_validator.py`
- **.__init__()** (3 connections) — `server/services/coordinate_validator.py`
- **validator()** (3 connections) — `server/tests/unit/services/test_coordinate_validator.py`
- **Any** (3 connections)
- **._count_coordinated_rooms()** (2 connections) — `server/services/coordinate_validator.py`
- **_zone_pattern()** (2 connections) — `server/services/coordinate_validator.py`
- **test_validate_coordinates_no_conflicts()** (2 connections) — `server/tests/unit/services/test_coordinate_validator.py`
- **test_validate_coordinates_reports_conflicts()** (2 connections) — `server/tests/unit/services/test_coordinate_validator.py`
- **asyncio** (2 connections)
- **AsyncSession** (1 connections)
- **fixture** (1 connections)
- **Coordinate validation service for ASCII maps. This module provides conflict…** (1 connections) — `server/services/coordinate_validator.py`
- **Validates room coordinates and detects conflicts. A conflict occurs when…** (1 connections) — `server/services/coordinate_validator.py`
- **Initialize coordinate validator. Args: session: Database session for coordinate…** (1 connections) — `server/services/coordinate_validator.py`
- **Validate coordinates for rooms in a zone/subzone and detect conflicts. Args:…** (1 connections) — `server/services/coordinate_validator.py`
- **Unit tests for coordinate validation.** (1 connections) — `server/tests/unit/services/test_coordinate_validator.py`

## Relationships

- [NATSServicePoolMixin](NATSServicePoolMixin.md) (4 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)

## Source Files

- `server/services/coordinate_validator.py`
- `server/tests/unit/services/test_coordinate_validator.py`

## Audit Trail

- EXTRACTED: 36 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*