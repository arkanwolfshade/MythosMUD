# FollowService

> 207 nodes

## Key Concepts

- **FollowService** (81 connections) — `server/game/follow_service.py`
- **test_follow_service.py** (55 connections) — `server/tests/unit/game/test_follow_service.py`
- **follow_service.py** (31 connections) — `server/game/follow_service.py`
- **follow_movement.py** (29 connections) — `server/game/follow_movement.py`
- **asyncio** (22 connections)
- **_FollowMovementHost** (20 connections) — `server/game/follow_movement.py`
- **FollowActionResult** (15 connections) — `server/game/follow_types.py`
- **str_id()** (15 connections) — `server/game/follow_types.py`
- **test_follow_movement.py** (14 connections) — `server/tests/unit/game/test_follow_movement.py`
- **FollowPersistence** (12 connections) — `server/game/follow_types.py`
- **follow_types.py** (12 connections) — `server/game/follow_types.py`
- **FollowStatePayload** (11 connections) — `server/game/follow_types.py`
- **propagate_follower_move()** (11 connections) — `server/game/follow_movement.py`
- **.request_follow()** (10 connections) — `server/game/follow_service.py`
- **_host()** (9 connections) — `server/tests/unit/game/test_follow_movement.py`
- **UUID** (9 connections)
- **FollowPlayerView** (8 connections) — `server/game/follow_types.py`
- **.get_following_display()** (8 connections) — `server/game/follow_service.py`
- **.__init__()** (8 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/follow_service.py`
- **is_npc_follow_value()** (8 connections) — `server/game/follow_types.py`
- **asyncio** (8 connections)
- **PendingFollowRequest** (7 connections) — `server/game/follow_types.py`
- **ensure_follower_standing()** (7 connections) — `server/game/follow_movement.py`
- **stand_follower_for_move()** (7 connections) — `server/game/follow_movement.py`
- *... and 182 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (17 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (9 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (7 shared connections)
- [MovementService](MovementService.md) (5 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [test_follow_flow.py](test_follow_flow.py.md) (3 shared connections)
- [TargetType](TargetType.md) (3 shared connections)
- [magic_service.py](magic_service.py.md) (3 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)

## Source Files

- `server/game/follow_movement.py`
- `server/game/follow_service.py`
- `server/game/follow_types.py`
- `server/tests/unit/game/test_follow_movement.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 403 (86%)
- INFERRED: 67 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*