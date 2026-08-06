# panels monitoringPanelTestFixtures Monit

> 14 nodes

## Key Concepts

- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **RoomDictList** (5 connections)
- **sample_rooms()** (3 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Any** (1 connections)
- **Apply exploration filter to rooms if requested and user is not admin.      Args:** (1 connections) — `server/api/rooms.py`
- **Two stable room dict rows (stable_id, name) for filter tests.** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Superuser bypass matches admin: full room list without exploration intersection.** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Admin / superuser bypasses exploration filter; room_service is not called.** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Non-admin with player record gets filter_rooms_by_exploration(stable room rows).** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **If user has no linked player, exploration cannot run; unknown rooms list returne** (1 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`

## Relationships

- [database helpers infrastructure](database_helpers_infrastructure.md) (6 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (5 shared connections)
- [corpse lifecycle service](corpse_lifecycle_service.md) (5 shared connections)
- [room game service](room_game_service.md) (2 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 44 (85%)
- INFERRED: 8 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*