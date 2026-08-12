# _apply_exploration_filter_if_needed

> 16 nodes

## Key Concepts

- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **RoomDictList** (5 connections)
- **sample_rooms()** (4 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **asyncio** (4 connections)
- **Any** (1 connections)
- **fixture** (1 connections)
- **Apply exploration filter to rooms if requested and user is not admin. Args:…** (1 connections) — `server/api/rooms.py`
- **Non-admin with player record gets filter_rooms_by_exploration(stable room rows).** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **If user has no linked player, exploration cannot run; unknown rooms list…** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Two stable room dict rows (stable_id, name) for filter tests.** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Superuser bypass matches admin: full room list without exploration intersection.** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Admin / superuser bypasses exploration filter; room_service is not called.** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`

## Relationships

- [RoomService](RoomService.md) (7 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (3 shared connections)
- [User](User.md) (1 shared connections)
- [ExplorationService](ExplorationService.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*