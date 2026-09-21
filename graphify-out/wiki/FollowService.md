# FollowService

> 98 nodes

## Key Concepts

- **FollowService** (81 connections) — `server/game/follow_service.py`
- **test_follow_service.py** (55 connections) — `server/tests/unit/game/test_follow_service.py`
- **asyncio** (22 connections)
- **PendingFollowRequest** (7 connections) — `server/game/follow_types.py`
- **test_follow_request_event_envelope_shape()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_npc_entered_room_moves_followers()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_move_failure_auto_unfollow()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_moves_followers()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_no_from_room_id_skips_propagation()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **fixture** (5 connections)
- **follow_service()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_accept_follow_invalid_request_id()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_accept_follow_success()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_decline_follow_success()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_already_standing()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_fails_to_stand()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_sitting_stands()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_expire_pending_requests_removes_stale()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_following_npc()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_following_player_resolves_name()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_not_following()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_disconnect_cancels_pending_requests()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_already_following_rejected()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_npc_immediate()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_player_creates_pending()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- *... and 73 more nodes in this community*

## Relationships

- [follow_service.py](follow_service.py.md) (34 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (6 shared connections)
- [event_types.py](event_types.py.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (3 shared connections)
- [test_follow_flow.py](test_follow_flow.py.md) (2 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [MovementService](MovementService.md) (1 shared connections)
- [UserManager](UserManager.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/game/follow_types.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 167 (76%)
- INFERRED: 53 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*