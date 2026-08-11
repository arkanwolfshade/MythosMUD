# Container Persistence Ops

> 117 nodes

## Key Concepts

- **ExplorationService** (73 connections) — `server/services/exploration_service.py`
- **test_exploration_service.py** (45 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_maps.py** (32 connections) — `server/tests/unit/api/test_maps.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_get_current_room_id()** (10 connections) — `server/api/maps.py`
- **_row_scalar_one_or_none()** (10 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (9 connections) — `server/api/maps.py`
- **test_prepare_ascii_map_context_applies_exploration_filter()** (8 connections) — `server/tests/unit/api/test_maps.py`
- **Any** (7 connections)
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **_two_rooms()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_skips_for_superuser()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_calls_for_normal_user()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **UUID** (5 connections)
- **test_filter_explored_rooms_calls_room_service()** (5 connections) — `server/tests/unit/api/test_maps.py`
- **_async_session_maker_mock()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_no_session()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **UUID** (4 connections)
- **test_get_current_room_id_none_when_persistence_errors()** (4 connections) — `server/tests/unit/api/test_maps.py`
- **test_get_player_and_exploration_returns_none_when_no_player()** (4 connections) — `server/tests/unit/api/test_maps.py`
- **_row_scalar_one()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_row_fetchall()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- *... and 92 more nodes in this community*

## Relationships

- [Minimap Fallback Helpers](Minimap_Fallback_Helpers.md) (25 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (14 shared connections)
- [Mythos Time HUD](Mythos_Time_HUD.md) (13 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (12 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (8 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (7 shared connections)
- [Map Room Helpers](Map_Room_Helpers.md) (3 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [Zone Coordinate Generator](Zone_Coordinate_Generator.md) (1 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (1 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (1 shared connections)

## Source Files

- `server/api/maps.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 466 (93%)
- INFERRED: 36 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*