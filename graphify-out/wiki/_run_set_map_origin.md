# _run_set_map_origin

> 37 nodes

## Key Concepts

- **_run_set_map_origin()** (13 connections) — `server/api/maps.py`
- **set_map_origin()** (13 connections) — `server/api/maps.py`
- **recalculate_coordinates()** (12 connections) — `server/api/maps.py`
- **_run_coordinate_recalculation()** (11 connections) — `server/api/maps.py`
- **maps/__init__.py** (11 connections) — `server/schemas/maps/__init__.py`
- **AsyncSession** (10 connections)
- **map.py** (10 connections) — `server/schemas/maps/map.py`
- **SetOriginRequest** (9 connections) — `server/api/maps.py`
- **Request** (9 connections)
- **AsciiMapResponse** (8 connections) — `server/schemas/maps/map.py`
- **AsciiMinimapResponse** (8 connections) — `server/schemas/maps/map.py`
- **CoordinateRecalculationResponse** (8 connections) — `server/schemas/maps/map.py`
- **MapOriginSetResponse** (8 connections) — `server/schemas/maps/map.py`
- **BaseModel** (7 connections)
- **_persist_map_origin()** (6 connections) — `server/api/maps.py`
- **test_set_map_origin_requires_auth()** (5 connections) — `server/tests/unit/api/test_maps.py`
- **test_set_map_origin_success()** (5 connections) — `server/tests/unit/api/test_maps.py`
- **CoordinateGenerationResponse** (4 connections) — `server/schemas/maps/map.py`
- **CoordinateValidationResponse** (4 connections) — `server/schemas/maps/map.py`
- **ViewportInfo** (4 connections) — `server/schemas/maps/map.py`
- **post** (2 connections)
- **BaseModel** (1 connections)
- **Admin-only coordinate regenerate + validate for a zone.** (1 connections) — `server/api/maps.py`
- **Trigger coordinate recalculation for a zone/subzone (admin only).** (1 connections) — `server/api/maps.py`
- **Request model for setting map origin.** (1 connections) — `server/api/maps.py`
- *... and 12 more nodes in this community*

## Relationships

- [ExplorationService](ExplorationService.md) (35 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [User](User.md) (5 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (2 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (2 shared connections)
- [CoordinateValidator](CoordinateValidator.md) (2 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/api/maps.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 116 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*