# Minimap Fallback Helpers

> 121 nodes

## Key Concepts

- **maps.py** (63 connections) — `server/api/maps.py`
- **MapZoneContext** (22 connections) — `server/api/map_helpers.py`
- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **get_ascii_map()** (13 connections) — `server/api/maps.py`
- **_run_set_map_origin()** (13 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (12 connections) — `server/api/maps.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **_run_coordinate_recalculation()** (11 connections) — `server/api/maps.py`
- **AsyncSession** (10 connections)
- **_build_ascii_minimap_response()** (10 connections) — `server/api/maps.py`
- **__init__.py** (10 connections) — `server/schemas/maps/__init__.py`
- **_resolve_current_room_for_minimap()** (9 connections) — `server/api/map_minimap.py`
- **_apply_minimap_fallback_coordinates()** (9 connections) — `server/api/map_minimap.py`
- **Request** (9 connections)
- **_build_ascii_map_response()** (9 connections) — `server/api/maps.py`
- **set_map_origin()** (9 connections) — `server/api/maps.py`
- **map.py** (9 connections) — `server/schemas/maps/map.py`
- **CoordinateValidator** (9 connections) — `server/services/coordinate_validator.py`
- **_append_room_with_fallback_coords_if_needed()** (8 connections) — `server/api/map_minimap.py`
- **recalculate_coordinates()** (8 connections) — `server/api/maps.py`
- **AsciiMapResponse** (8 connections) — `server/schemas/maps/map.py`
- **AsciiMinimapResponse** (8 connections) — `server/schemas/maps/map.py`
- **CoordinateRecalculationResponse** (8 connections) — `server/schemas/maps/map.py`
- *... and 96 more nodes in this community*

## Relationships

- [Container Persistence Ops](Container_Persistence_Ops.md) (27 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (15 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (10 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (10 shared connections)
- [Map Room Helpers](Map_Room_Helpers.md) (9 shared connections)
- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (8 shared connections)
- [ASCII Map Renderer](ASCII_Map_Renderer.md) (6 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (3 shared connections)
- [Zone Coordinate Generator](Zone_Coordinate_Generator.md) (3 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (2 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (1 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/api/maps.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/coordinate_validator.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`

## Audit Trail

- EXTRACTED: 554 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*