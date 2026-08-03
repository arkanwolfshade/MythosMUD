# schemas player rationale

> 17 nodes

## Key Concepts

- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (10 connections) — `server/api/rooms.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **RoomDictList** (5 connections)
- **AsyncSession** (4 connections)
- **sample_rooms()** (3 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Any** (1 connections)
- **Apply exploration filter to rooms if requested and user is not admin.      Args:** (1 connections) — `server/api/rooms.py`
- **List rooms filtered by plane, zone, and optionally sub_zone.      Returns room d** (1 connections) — `server/api/rooms.py`
- **Two stable room dict rows (stable_id, name) for filter tests.** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Superuser bypass matches admin: full room list without exploration intersection.** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Admin / superuser bypasses exploration filter; room_service is not called.** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Non-admin with player record gets filter_rooms_by_exploration(stable room rows).** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **If user has no linked player, exploration cannot run; unknown rooms list returne** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`

## Relationships

- [respawn player handlers](respawn_player_handlers.md) (6 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (6 shared connections)
- [corpse lifecycle service](corpse_lifecycle_service.md) (6 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (6 shared connections)
- [auth users rationale](auth_users_rationale.md) (2 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 59 (88%)
- INFERRED: 8 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*