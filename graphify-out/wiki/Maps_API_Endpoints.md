# Maps API Endpoints

> 69 nodes · cohesion 0.05

## Key Concepts

- **RoomService** (64 connections) — `server/game/room_service.py`
- **test_maps.py** (27 connections) — `server/tests/unit/api/test_maps.py`
- **.get_room()** (11 connections) — `server/game/room_service.py`
- **Any** (10 connections) — `server/game/room_service.py`
- **_get_current_room_id()** (9 connections) — `server/api/maps.py`
- **UUID** (9 connections) — `server/tests/unit/api/test_maps.py`
- **_ensure_coords_stub()** (8 connections) — `server/tests/unit/api/test_maps.py`
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **_MapRooms** (7 connections) — `server/tests/unit/api/test_maps.py`
- **MapZoneContext** (7 connections) — `server/tests/unit/api/test_maps.py`
- **_two_rooms()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **.get_adjacent_rooms()** (6 connections) — `server/game/room_service.py`
- **AsyncSession** (6 connections) — `server/tests/unit/api/test_maps.py`
- **ExplorationService** (6 connections) — `server/tests/unit/api/test_maps.py`
- **RoomService** (6 connections) — `server/tests/unit/api/test_maps.py`
- **User** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_prepare_ascii_map_context_applies_exploration_filter()** (5 connections) — `server/tests/unit/api/test_maps.py`
- **.filter_rooms_by_exploration()** (5 connections) — `server/game/room_service.py`
- **.get_local_chat_scope()** (4 connections) — `server/game/room_service.py`
- **.get_room_exits()** (4 connections) — `server/game/room_service.py`
- **.get_room_occupants()** (4 connections) — `server/game/room_service.py`
- **test_apply_exploration_filter_if_needed_calls_for_normal_user()** (3 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_skips_for_superuser()** (3 connections) — `server/tests/unit/api/test_maps.py`
- **test_filter_explored_rooms_calls_room_service()** (3 connections) — `server/tests/unit/api/test_maps.py`
- *... and 44 more nodes in this community*

## Relationships

- [[ASCII Map API]] (25 shared connections)
- [[NPC Admin API]] (15 shared connections)
- [[Time Event Consumer]] (9 shared connections)
- [[API Test Fixtures]] (8 shared connections)
- [[Services Exploration Service]] (8 shared connections)
- [[Game Service Bundle]] (7 shared connections)
- [[Room Exploration API]] (3 shared connections)
- [[Minimap Fallback Helpers]] (3 shared connections)
- [[Room Service Tests]] (2 shared connections)
- [[Dependency Injection Tests]] (2 shared connections)
- [[Dependency Injection Dependencies]] (2 shared connections)
- [[Character Stats Generator]] (2 shared connections)

## Source Files

- `server/api/maps.py`
- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 244 (79%)
- INFERRED: 64 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
