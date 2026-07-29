# maps

> 29 nodes

## Key Concepts

- **maps.py** (53 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (13 connections) — `server/api/maps.py`
- **set_map_origin()** (11 connections) — `server/api/maps.py`
- **_get_current_room_id()** (10 connections) — `server/api/maps.py`
- **recalculate_coordinates()** (10 connections) — `server/api/maps.py`
- **Request** (7 connections)
- **_get_minimap_player_and_room_id()** (7 connections) — `server/api/maps.py`
- **CoordinateValidator** (7 connections) — `server/services/coordinate_validator.py`
- **SetOriginRequest** (5 connections) — `server/api/maps.py`
- **coordinate_validator.py** (5 connections) — `server/services/coordinate_validator.py`
- **test_get_current_room_id_none_when_persistence_errors()** (4 connections) — `server/tests/unit/api/test_maps.py`
- **.__init__()** (3 connections) — `server/services/coordinate_validator.py`
- **.validate_coordinates()** (3 connections) — `server/services/coordinate_validator.py`
- **test_get_current_room_id_from_query_param()** (3 connections) — `server/tests/unit/api/test_maps.py`
- **test_get_current_room_id_from_player()** (3 connections) — `server/tests/unit/api/test_maps.py`
- **BaseModel** (1 connections)
- **Map API endpoints for MythosMUD server.  This module handles ASCII map rendering** (1 connections) — `server/api/maps.py`
- **Get current room ID from query params or database. Returns room ID or None.** (1 connections) — `server/api/maps.py`
- **Resolve player and current_room_id for minimap. Raises LoggedHTTPException if no** (1 connections) — `server/api/maps.py`
- **Get ASCII minimap centered on player.      Returns a small ASCII map showing are** (1 connections) — `server/api/maps.py`
- **Trigger coordinate recalculation for a zone/subzone (admin only).      Returns l** (1 connections) — `server/api/maps.py`
- **Request model for setting map origin.** (1 connections) — `server/api/maps.py`
- **Set a room as the map origin for its zone/subzone (admin only).      Triggers co** (1 connections) — `server/api/maps.py`
- **AsyncSession** (1 connections)
- **Any** (1 connections)
- *... and 4 more nodes in this community*

## Relationships

- [AsyncSession](AsyncSession.md) (25 shared connections)
- [APIRouter](APIRouter.md) (15 shared connections)
- [main()](main%28%29.md) (14 shared connections)
- [init](init.md) (7 shared connections)
- [MapZoneContext](MapZoneContext.md) (6 shared connections)
- [Request](Request.md) (5 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (3 shared connections)
- [map helpers](map_helpers.md) (2 shared connections)
- [BaseUserManager](BaseUserManager.md) (2 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (2 shared connections)
- [handle ascii map error()](handle_ascii_map_error%28%29.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)

## Source Files

- `server/api/maps.py`
- `server/services/coordinate_validator.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 153 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*