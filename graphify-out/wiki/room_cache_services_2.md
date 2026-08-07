# room cache services

> 15 nodes

## Key Concepts

- **__init__.py** (10 connections) — `server/schemas/maps/__init__.py`
- **map.py** (9 connections) — `server/schemas/maps/map.py`
- **BaseModel** (7 connections)
- **AsciiMapResponse** (7 connections) — `server/schemas/maps/map.py`
- **CoordinateRecalculationResponse** (7 connections) — `server/schemas/maps/map.py`
- **ViewportInfo** (4 connections) — `server/schemas/maps/map.py`
- **CoordinateGenerationResponse** (4 connections) — `server/schemas/maps/map.py`
- **CoordinateValidationResponse** (4 connections) — `server/schemas/maps/map.py`
- **Maps domain schemas: map API responses.** (1 connections) — `server/schemas/maps/__init__.py`
- **Map API response schemas for MythosMUD server.  This module provides Pydantic mo** (1 connections) — `server/schemas/maps/map.py`
- **Viewport information for map rendering.** (1 connections) — `server/schemas/maps/map.py`
- **Response model for ASCII map endpoint.** (1 connections) — `server/schemas/maps/map.py`
- **Response model for coordinate generation endpoint.** (1 connections) — `server/schemas/maps/map.py`
- **Response model for coordinate validation endpoint.** (1 connections) — `server/schemas/maps/map.py`
- **Response model for coordinate recalculation endpoint.** (1 connections) — `server/schemas/maps/map.py`

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (10 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (3 shared connections)

## Source Files

- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*