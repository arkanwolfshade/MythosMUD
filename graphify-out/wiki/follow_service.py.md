# follow_service.py

> 107 nodes

## Key Concepts

- **follow_service.py** (31 connections) — `server/game/follow_service.py`
- **follow_movement.py** (29 connections) — `server/game/follow_movement.py`
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
- **ensure_follower_standing()** (7 connections) — `server/game/follow_movement.py`
- **stand_follower_for_move()** (7 connections) — `server/game/follow_movement.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (7 connections) — `server/game/follow_service.py`
- **.unfollow()** (7 connections) — `server/game/follow_service.py`
- *... and 82 more nodes in this community*

## Relationships

- [FollowService](FollowService.md) (34 shared connections)
- [event_types.py](event_types.py.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (4 shared connections)
- [MovementService](MovementService.md) (4 shared connections)
- [send_game_event](send_game_event.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (3 shared connections)
- [TargetType](TargetType.md) (3 shared connections)
- [emit_posture_change](emit_posture_change.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)

## Source Files

- `server/game/follow_movement.py`
- `server/game/follow_service.py`
- `server/game/follow_types.py`
- `server/tests/unit/game/test_follow_movement.py`

## Audit Trail

- EXTRACTED: 264 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*