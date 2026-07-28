# Server Game (8)

> 87 nodes

## Key Concepts

- **ExplorationService** (72 connections) — `server/services/exploration_service.py`
- **RoomService** (67 connections) — `server/game/room_service.py`
- **test_maps.py** (32 connections) — `server/tests/unit/api/test_maps.py`
- **room_service.py** (21 connections) — `server/game/room_service.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **.get_room()** (11 connections) — `server/game/room_service.py`
- **_get_current_room_id()** (10 connections) — `server/api/maps.py`
- **Any** (10 connections)
- **_ensure_coords_stub()** (9 connections) — `server/tests/unit/api/test_maps.py`
- **test_prepare_ascii_map_context_applies_exploration_filter()** (8 connections) — `server/tests/unit/api/test_maps.py`
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **.get_adjacent_rooms()** (6 connections) — `server/game/room_service.py`
- **_two_rooms()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_skips_for_superuser()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_calls_for_normal_user()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **.filter_rooms_by_exploration()** (5 connections) — `server/game/room_service.py`
- **UUID** (5 connections)
- **test_filter_explored_rooms_calls_room_service()** (5 connections) — `server/tests/unit/api/test_maps.py`
- *... and 62 more nodes in this community*

## Relationships

- [Server Services (23)](Server_Services_%2823%29.md) (37 shared connections)
- [Server Api (8)](Server_Api_%288%29.md) (36 shared connections)
- [Server Admin](Server_Admin.md) (28 shared connections)
- [Server Api (10)](Server_Api_%2810%29.md) (12 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (12 shared connections)
- [Server Services (81)](Server_Services_%2881%29.md) (8 shared connections)
- [Server Persistence](Server_Persistence.md) (7 shared connections)
- [Server Commands](Server_Commands.md) (5 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (4 shared connections)
- [Server Game (5)](Server_Game_%285%29.md) (3 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (1 shared connections)
- [Server Caching (2)](Server_Caching_%282%29.md) (1 shared connections)

## Source Files

- `server/api/maps.py`
- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 416 (88%)
- INFERRED: 58 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*