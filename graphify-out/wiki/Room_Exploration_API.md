# Room Exploration API

> 37 nodes · cohesion 0.12

## Key Concepts

- **update_room_position()** (14 connections) — `server/api/rooms.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (10 connections) — `server/api/rooms.py`
- **RoomListResponse** (10 connections) — `server/api/rooms.py`
- **RoomPositionUpdateResponse** (10 connections) — `server/api/rooms.py`
- **RoomResponse** (10 connections) — `server/api/rooms.py`
- **test_rooms_exploration_filter.py** (9 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Request** (8 connections) — `server/api/rooms.py`
- **RoomService** (8 connections) — `server/api/rooms.py`
- **get_room()** (7 connections) — `server/api/rooms.py`
- **RoomPositionUpdate** (7 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (7 connections) — `server/api/rooms.py`
- **RoomDictList** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **AsyncSession** (7 connections) — `server/api/rooms.py`
- **User** (7 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (6 connections) — `server/api/rooms.py`
- **ExplorationService** (5 connections) — `server/api/rooms.py`
- **_invalidate_room_cache()** (4 connections) — `server/api/rooms.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (4 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (4 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (4 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (4 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Any** (4 connections) — `server/api/rooms.py`
- **sample_rooms()** (3 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Update room position in database and verify the update succeeded.** (1 connections) — `server/api/rooms.py`
- *... and 12 more nodes in this community*

## Relationships

- [[NPC Admin API]] (8 shared connections)
- [[Container Exception Handlers]] (5 shared connections)
- [[Maps API Endpoints]] (3 shared connections)
- [[NPC Definition Admin API]] (2 shared connections)
- [[Services Exploration Service]] (2 shared connections)
- [[Admin NPC Schemas]] (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 135 (73%)
- INFERRED: 50 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
