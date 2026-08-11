# Mythos Time HUD

> 69 nodes

## Key Concepts

- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **room_service.py** (21 connections) — `server/game/room_service.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **_resolve_current_room_for_minimap()** (9 connections) — `server/api/map_minimap.py`
- **_apply_minimap_fallback_coordinates()** (9 connections) — `server/api/map_minimap.py`
- **_append_room_with_fallback_coords_if_needed()** (8 connections) — `server/api/map_minimap.py`
- **TestApplyMinimapFallbackCoordinates** (8 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **TestAppendRoomWithFallbackCoordsIfNeeded** (7 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_generate_minimap_html_admin_path()** (5 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_generate_minimap_html_non_admin_filters_exploration()** (5 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **RoomDictList** (5 connections)
- **Any** (4 connections)
- **AsyncSession** (3 connections)
- **.test_appends_room_unchanged_when_has_coords()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_appends_copy_with_fallback_0_0_when_coords_missing()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_appends_fallback_when_only_one_coord_missing()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- *... and 44 more nodes in this community*

## Relationships

- [Inventory Service Helpers](Inventory_Service_Helpers.md) (16 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (13 shared connections)
- [Minimap Fallback Helpers](Minimap_Fallback_Helpers.md) (12 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (12 shared connections)
- [Map Room Helpers](Map_Room_Helpers.md) (6 shared connections)
- [ASCII Map Renderer](ASCII_Map_Renderer.md) (3 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (2 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (2 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (1 shared connections)
- [E 2 E Testing Guide](E_2_E_Testing_Guide.md) (1 shared connections)
- [ASCII Map Exit Tests](ASCII_Map_Exit_Tests.md) (1 shared connections)

## Source Files

- `server/api/map_minimap.py`
- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 277 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*