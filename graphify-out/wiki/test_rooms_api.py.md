# test_rooms_api.py

> 47 nodes

## Key Concepts

- **test_rooms_api.py** (24 connections) — `server/tests/unit/api/test_rooms_api.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (10 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (10 connections) — `server/api/rooms.py`
- **asyncio** (8 connections)
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **RoomPositionUpdate** (6 connections) — `server/api/rooms.py`
- **_invalidate_room_cache()** (6 connections) — `server/api/rooms.py`
- **test_update_room_position_room_missing()** (6 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_get_room_not_found()** (5 connections) — `server/tests/unit/api/test_rooms_api.py`
- **RoomDictList** (5 connections)
- **Request** (5 connections)
- **test_get_room_success()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_invalidate_room_cache()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_list_rooms_success()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_update_room_position_in_db_not_found()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_validate_room_position_update_requires_auth()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **sample_rooms()** (4 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **AsyncSession** (4 connections)
- *... and 22 more nodes in this community*

## Relationships

- [ExplorationService](ExplorationService.md) (21 shared connections)
- [get_logger](get_logger.md) (18 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (10 shared connections)
- [User](User.md) (4 shared connections)
- [rooms/room.py](rooms-room.py.md) (3 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (2 shared connections)
- [PostgresCursor](PostgresCursor.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/tests/unit/api/test_rooms_api.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 122 (87%)
- INFERRED: 19 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*