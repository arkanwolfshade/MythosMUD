# follow_service.py

> 71 nodes

## Key Concepts

- **follow_service.py** (31 connections) — `server/game/follow_service.py`
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
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- **._schedule_coro()** (5 connections) — `server/game/follow_service.py`
- **._start_following_npc()** (5 connections) — `server/game/follow_service.py`
- *... and 46 more nodes in this community*

## Relationships

- [FollowService](FollowService.md) (33 shared connections)
- [follow_movement.py](follow_movement.py.md) (13 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (3 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [event_types.py](event_types.py.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [MovementService](MovementService.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/game/follow_movement.py`
- `server/game/follow_service.py`
- `server/game/follow_types.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 173 (93%)
- INFERRED: 13 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*