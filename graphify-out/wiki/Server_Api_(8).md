# Server Api (8)

> 64 nodes

## Key Concepts

- **maps.py** (53 connections) — `server/api/maps.py`
- **MapZoneContext** (19 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (17 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (14 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (13 connections) — `server/api/maps.py`
- **get_ascii_map()** (12 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **set_map_origin()** (11 connections) — `server/api/maps.py`
- **recalculate_coordinates()** (10 connections) — `server/api/maps.py`
- **__init__.py** (10 connections) — `server/schemas/maps/__init__.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **map.py** (9 connections) — `server/schemas/maps/map.py`
- **AsyncSession** (8 connections)
- **Request** (7 connections)
- **Any** (7 connections)
- **_get_minimap_player_and_room_id()** (7 connections) — `server/api/maps.py`
- **BaseModel** (7 connections)
- **AsciiMapResponse** (7 connections) — `server/schemas/maps/map.py`
- **AsciiMinimapResponse** (7 connections) — `server/schemas/maps/map.py`
- **CoordinateRecalculationResponse** (7 connections) — `server/schemas/maps/map.py`
- **MapOriginSetResponse** (7 connections) — `server/schemas/maps/map.py`
- **CoordinateValidator** (7 connections) — `server/services/coordinate_validator.py`
- **UUID** (6 connections)
- **_handle_ascii_map_error()** (6 connections) — `server/api/maps.py`
- *... and 39 more nodes in this community*

## Relationships

- [Server Game (8)](Server_Game_%288%29.md) (36 shared connections)
- [Server Admin](Server_Admin.md) (26 shared connections)
- [Server Api (10)](Server_Api_%2810%29.md) (10 shared connections)
- [Server Api](Server_Api.md) (6 shared connections)
- [Server Api (11)](Server_Api_%2811%29.md) (5 shared connections)
- [Server Services (57)](Server_Services_%2857%29.md) (5 shared connections)
- [Server Commands](Server_Commands.md) (4 shared connections)
- [Server Services (14)](Server_Services_%2814%29.md) (3 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (1 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (1 shared connections)
- [Server Persistence](Server_Persistence.md) (1 shared connections)
- [Server Middleware](Server_Middleware.md) (1 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/coordinate_validator.py`

## Audit Trail

- EXTRACTED: 341 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*