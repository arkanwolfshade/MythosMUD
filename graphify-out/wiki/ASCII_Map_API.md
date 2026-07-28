# ASCII Map API

> 93 nodes · cohesion 0.05

## Key Concepts

- **ExplorationService** (75 connections) — `server/services/exploration_service.py`
- **RoomService** (70 connections) — `server/game/room_service.py`
- **maps.py** (53 connections) — `server/api/maps.py`
- **test_maps.py** (32 connections) — `server/tests/unit/api/test_maps.py`
- **room_service.py** (21 connections) — `server/game/room_service.py`
- **MapZoneContext** (19 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (17 connections) — `server/api/maps.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **_ensure_coordinates_generated()** (14 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (13 connections) — `server/api/maps.py`
- **get_ascii_map()** (12 connections) — `server/api/maps.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **set_map_origin()** (11 connections) — `server/api/maps.py`
- **_get_current_room_id()** (10 connections) — `server/api/maps.py`
- **recalculate_coordinates()** (10 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **_ensure_coords_stub()** (9 connections) — `server/tests/unit/api/test_maps.py`
- **AsyncSession** (8 connections)
- **test_prepare_ascii_map_context_applies_exploration_filter()** (8 connections) — `server/tests/unit/api/test_maps.py`
- **_get_minimap_player_and_room_id()** (7 connections) — `server/api/maps.py`
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **Any** (7 connections)
- **Request** (7 connections)
- *... and 68 more nodes in this community*

## Relationships

- [Player Left Room Tests](Player_Left_Room_Tests.md) (37 shared connections)
- [Minimap Fallback Helpers](Minimap_Fallback_Helpers.md) (23 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (23 shared connections)
- [Room Exploration API](Room_Exploration_API.md) (17 shared connections)
- [Maps API Endpoints](Maps_API_Endpoints.md) (17 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (14 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (9 shared connections)
- [Alias Command Models](Alias_Command_Models.md) (9 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (8 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (8 shared connections)
- [Quest Instance Repository Tests](Quest_Instance_Repository_Tests.md) (8 shared connections)
- [Map Room Helpers](Map_Room_Helpers.md) (6 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/game/room_service.py`
- `server/schemas/maps/map.py`
- `server/services/coordinate_validator.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 576 (90%)
- INFERRED: 65 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*