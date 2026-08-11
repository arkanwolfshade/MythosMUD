# Minimap Fallback Helpers

> 60 nodes

## Key Concepts

- **maps.py** (63 connections) — `server/api/maps.py`
- **MapZoneContext** (22 connections) — `server/api/map_helpers.py`
- **get_ascii_map()** (13 connections) — `server/api/maps.py`
- **_run_set_map_origin()** (13 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (12 connections) — `server/api/maps.py`
- **_run_coordinate_recalculation()** (11 connections) — `server/api/maps.py`
- **AsyncSession** (10 connections)
- **_build_ascii_minimap_response()** (10 connections) — `server/api/maps.py`
- **__init__.py** (10 connections) — `server/schemas/maps/__init__.py`
- **Request** (9 connections)
- **_build_ascii_map_response()** (9 connections) — `server/api/maps.py`
- **set_map_origin()** (9 connections) — `server/api/maps.py`
- **map.py** (9 connections) — `server/schemas/maps/map.py`
- **recalculate_coordinates()** (8 connections) — `server/api/maps.py`
- **AsciiMapResponse** (8 connections) — `server/schemas/maps/map.py`
- **AsciiMinimapResponse** (8 connections) — `server/schemas/maps/map.py`
- **CoordinateRecalculationResponse** (8 connections) — `server/schemas/maps/map.py`
- **MapOriginSetResponse** (8 connections) — `server/schemas/maps/map.py`
- **_get_minimap_player_and_room_id()** (7 connections) — `server/api/maps.py`
- **_MapEndpointDeps** (7 connections) — `server/api/maps.py`
- **SetOriginRequest** (7 connections) — `server/api/maps.py`
- **BaseModel** (7 connections)
- **_handle_ascii_map_error()** (6 connections) — `server/api/maps.py`
- **_persist_map_origin()** (6 connections) — `server/api/maps.py`
- **_CoordGenCtx** (5 connections) — `server/api/maps.py`
- *... and 35 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (29 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (25 shared connections)
- [Mythos Time HUD](Mythos_Time_HUD.md) (12 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (5 shared connections)
- [Debuglogger Constructor Debug Logger](Debuglogger_Constructor_Debug_Logger.md) (4 shared connections)
- [Map Room Helpers](Map_Room_Helpers.md) (3 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (3 shared connections)
- [ASCII Map Renderer](ASCII_Map_Renderer.md) (3 shared connections)
- [Zone Coordinate Generator](Zone_Coordinate_Generator.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (2 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (2 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (1 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`

## Audit Trail

- EXTRACTED: 334 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*