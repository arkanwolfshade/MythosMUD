# _apply_exploration_filter_if_needed

> 18 nodes

## Key Concepts

- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **test_rooms_exploration_filter.py** (13 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **RoomDictList** (5 connections)
- **sample_rooms()** (4 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **asyncio** (4 connections)
- **Any** (1 connections)
- **fixture** (1 connections)
- **Apply exploration filter to rooms if requested and user is not admin. Args:…** (1 connections) — `server/api/rooms.py`
- **Tests for room list exploration filtering vs admin bypass (server.api.rooms).…** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Non-admin with player record gets filter_rooms_by_exploration(stable room rows).** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **If user has no linked player, exploration cannot run; unknown rooms list…** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Two stable room dict rows (stable_id, name) for filter tests.** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Superuser bypass matches admin: full room list without exploration intersection.** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Admin / superuser bypasses exploration filter; room_service is not called.** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`

## Relationships

- [pydantic.md](pydantic.md.md) (10 shared connections)
- [ExplorationService](ExplorationService.md) (7 shared connections)
- [User](User.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 40 (83%)
- INFERRED: 8 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*