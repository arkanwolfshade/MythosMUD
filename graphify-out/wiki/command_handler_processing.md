# command handler processing

> 31 nodes

## Key Concepts

- **set_map_origin()** (11 connections) — `server/api/maps.py`
- **recalculate_coordinates()** (10 connections) — `server/api/maps.py`
- **__init__.py** (10 connections) — `server/schemas/maps/__init__.py`
- **map.py** (9 connections) — `server/schemas/maps/map.py`
- **BaseModel** (7 connections)
- **AsciiMapResponse** (7 connections) — `server/schemas/maps/map.py`
- **AsciiMinimapResponse** (7 connections) — `server/schemas/maps/map.py`
- **CoordinateRecalculationResponse** (7 connections) — `server/schemas/maps/map.py`
- **MapOriginSetResponse** (7 connections) — `server/schemas/maps/map.py`
- **CoordinateValidator** (7 connections) — `server/services/coordinate_validator.py`
- **ViewportInfo** (4 connections) — `server/schemas/maps/map.py`
- **CoordinateGenerationResponse** (4 connections) — `server/schemas/maps/map.py`
- **CoordinateValidationResponse** (4 connections) — `server/schemas/maps/map.py`
- **.__init__()** (3 connections) — `server/services/coordinate_validator.py`
- **.validate_coordinates()** (3 connections) — `server/services/coordinate_validator.py`
- **Trigger coordinate recalculation for a zone/subzone (admin only).      Returns l** (1 connections) — `server/api/maps.py`
- **Set a room as the map origin for its zone/subzone (admin only).      Triggers co** (1 connections) — `server/api/maps.py`
- **Maps domain schemas: map API responses.** (1 connections) — `server/schemas/maps/__init__.py`
- **Map API response schemas for MythosMUD server.  This module provides Pydantic mo** (1 connections) — `server/schemas/maps/map.py`
- **Viewport information for map rendering.** (1 connections) — `server/schemas/maps/map.py`
- **Response model for ASCII map endpoint.** (1 connections) — `server/schemas/maps/map.py`
- **Response model for ASCII minimap endpoint.** (1 connections) — `server/schemas/maps/map.py`
- **Response model for coordinate generation endpoint.** (1 connections) — `server/schemas/maps/map.py`
- **Response model for coordinate validation endpoint.** (1 connections) — `server/schemas/maps/map.py`
- **Response model for coordinate recalculation endpoint.** (1 connections) — `server/schemas/maps/map.py`
- *... and 6 more nodes in this community*

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (14 shared connections)
- [admin auth service](admin_auth_service.md) (7 shared connections)
- [Exception Containers](Exception_Containers.md) (2 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (2 shared connections)
- [coordinate services generator](coordinate_services_generator.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/api/maps.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/coordinate_validator.py`

## Audit Trail

- EXTRACTED: 116 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*