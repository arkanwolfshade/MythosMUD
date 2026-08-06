# room cache services

> 22 nodes

## Key Concepts

- **set_map_origin()** (14 connections) — `server/api/maps.py`
- **CoordinateValidator** (9 connections) — `server/services/coordinate_validator.py`
- **SetOriginRequest** (8 connections) — `server/api/maps.py`
- **coordinate_validator.py** (6 connections) — `server/services/coordinate_validator.py`
- **test_coordinate_validator.py** (6 connections) — `server/tests/unit/services/test_coordinate_validator.py`
- **test_set_map_origin_requires_auth()** (4 connections) — `server/tests/unit/api/test_maps.py`
- **test_set_map_origin_success()** (4 connections) — `server/tests/unit/api/test_maps.py`
- **.__init__()** (3 connections) — `server/services/coordinate_validator.py`
- **.validate_coordinates()** (3 connections) — `server/services/coordinate_validator.py`
- **validator()** (2 connections) — `server/tests/unit/services/test_coordinate_validator.py`
- **BaseModel** (1 connections)
- **Request model for setting map origin.** (1 connections) — `server/api/maps.py`
- **Set a room as the map origin for its zone/subzone (admin only).      Triggers co** (1 connections) — `server/api/maps.py`
- **AsyncSession** (1 connections)
- **Any** (1 connections)
- **Coordinate validation service for ASCII maps.  This module provides conflict det** (1 connections) — `server/services/coordinate_validator.py`
- **Validates room coordinates and detects conflicts.      A conflict occurs when mu** (1 connections) — `server/services/coordinate_validator.py`
- **Initialize coordinate validator.          Args:             session: Database se** (1 connections) — `server/services/coordinate_validator.py`
- **Validate coordinates for rooms in a zone/subzone and detect conflicts.** (1 connections) — `server/services/coordinate_validator.py`
- **test_validate_coordinates_no_conflicts()** (1 connections) — `server/tests/unit/services/test_coordinate_validator.py`
- **test_validate_coordinates_reports_conflicts()** (1 connections) — `server/tests/unit/services/test_coordinate_validator.py`
- **Unit tests for coordinate validation.** (1 connections) — `server/tests/unit/services/test_coordinate_validator.py`

## Relationships

- [persistence container rationale](persistence_container_rationale.md) (7 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (6 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (2 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (1 shared connections)
- [coordinate services generator](coordinate_services_generator.md) (1 shared connections)

## Source Files

- `server/api/maps.py`
- `server/services/coordinate_validator.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/services/test_coordinate_validator.py`

## Audit Trail

- EXTRACTED: 68 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*