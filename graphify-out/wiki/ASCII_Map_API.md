# ASCII Map API

> 44 nodes · cohesion 0.17

## Key Concepts

- **maps.py** (51 connections) — `server/api/maps.py`
- **MapZoneContext** (39 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (17 connections) — `server/api/maps.py`
- **AsciiMapResponse** (16 connections) — `server/api/maps.py`
- **AsciiMinimapResponse** (16 connections) — `server/api/maps.py`
- **CoordinateRecalculationResponse** (16 connections) — `server/api/maps.py`
- **MapOriginSetResponse** (16 connections) — `server/api/maps.py`
- **User** (15 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (14 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **AsyncSession** (13 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (12 connections) — `server/api/maps.py`
- **Any** (12 connections) — `server/api/maps.py`
- **ExplorationService** (12 connections) — `server/api/maps.py`
- **Request** (12 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **get_ascii_map()** (11 connections) — `server/api/maps.py`
- **RoomService** (11 connections) — `server/api/maps.py`
- **UUID** (11 connections) — `server/api/maps.py`
- **set_map_origin()** (10 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **recalculate_coordinates()** (9 connections) — `server/api/maps.py`
- **SetOriginRequest** (9 connections) — `server/api/maps.py`
- **MapZoneContext** (9 connections) — `server/api/maps.py`
- **_get_minimap_player_and_room_id()** (7 connections) — `server/api/maps.py`
- *... and 19 more nodes in this community*

## Relationships

- [[Maps API Endpoints]] (25 shared connections)
- [[NPC Admin API]] (17 shared connections)
- [[Map Room Helpers]] (16 shared connections)
- [[Minimap Fallback Helpers]] (5 shared connections)
- [[Zone Coordinate Generator]] (5 shared connections)
- [[Schemas Maps Map]] (4 shared connections)
- [[Container Exception Handlers]] (3 shared connections)
- [[NPC Definition Admin API]] (3 shared connections)
- [[Migrate Async Persistence]] (1 shared connections)
- [[Admin NPC Schemas]] (1 shared connections)
- [[API Test Fixtures]] (1 shared connections)
- [[Async Persistence Layer]] (1 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/services/coordinate_validator.py`

## Audit Trail

- EXTRACTED: 257 (63%)
- INFERRED: 154 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
