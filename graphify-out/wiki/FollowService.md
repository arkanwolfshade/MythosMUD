# FollowService

> 154 nodes

## Key Concepts

- **FollowService** (74 connections) — `server/game/follow_service.py`
- **test_follow_service.py** (51 connections) — `server/tests/unit/game/test_follow_service.py`
- **follow_service.py** (32 connections) — `server/game/follow_service.py`
- **asyncio** (20 connections)
- **FollowActionResult** (15 connections) — `server/game/follow_types.py`
- **str_id()** (15 connections) — `server/game/follow_types.py`
- **FollowPersistence** (12 connections) — `server/game/follow_types.py`
- **follow_types.py** (12 connections) — `server/game/follow_types.py`
- **FollowStatePayload** (11 connections) — `server/game/follow_types.py`
- **.request_follow()** (10 connections) — `server/game/follow_service.py`
- **UUID** (9 connections)
- **FollowPlayerView** (8 connections) — `server/game/follow_types.py`
- **.get_following_display()** (8 connections) — `server/game/follow_service.py`
- **.__init__()** (8 connections) — `server/game/follow_service.py`
- **is_npc_follow_value()** (8 connections) — `server/game/follow_types.py`
- **PendingFollowRequest** (7 connections) — `server/game/follow_types.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (7 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (7 connections) — `server/game/follow_service.py`
- **._create_pending_follow_request()** (6 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (6 connections) — `server/game/follow_service.py`
- **._resolve_follow_target_label()** (6 connections) — `server/game/follow_service.py`
- **.unfollow()** (6 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- *... and 129 more nodes in this community*

## Relationships

- [follow_movement.py](follow_movement.py.md) (13 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [event_types.py](event_types.py.md) (8 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (7 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (4 shared connections)
- [test_follow_flow.py](test_follow_flow.py.md) (3 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [MovementService](MovementService.md) (3 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (3 shared connections)
- [.__post_init__](__post_init__.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [UserManager](UserManager.md) (2 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/game/follow_types.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 294 (84%)
- INFERRED: 55 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*