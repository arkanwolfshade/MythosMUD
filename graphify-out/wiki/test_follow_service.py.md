# test_follow_service.py

> 151 nodes

## Key Concepts

- **test_follow_service.py** (48 connections) — `server/tests/unit/game/test_follow_service.py`
- **FollowService** (39 connections) — `server/game/follow_service.py`
- **follow_service.py** (26 connections) — `server/game/follow_service.py`
- **asyncio** (20 connections)
- **_str_id()** (15 connections) — `server/game/follow_service.py`
- **test_follow_flow.py** (15 connections) — `server/tests/integration/test_follow_flow.py`
- **.request_follow()** (10 connections) — `server/game/follow_service.py`
- **UUID** (10 connections)
- **._send_follow_state_to_player()** (9 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (9 connections) — `server/game/follow_service.py`
- **._handle_npc_follower_move()** (8 connections) — `server/game/follow_service.py`
- **._handle_player_follower_move()** (8 connections) — `server/game/follow_service.py`
- **.__init__()** (8 connections) — `server/game/follow_service.py`
- **.unfollow()** (8 connections) — `server/game/follow_service.py`
- **Any** (8 connections)
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **._schedule_coro()** (7 connections) — `server/game/follow_service.py`
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **._on_player_entered_room()** (6 connections) — `server/game/follow_service.py`
- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **._ensure_follower_standing()** (5 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- *... and 126 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (21 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [EventBus](EventBus.md) (5 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (4 shared connections)
- [GameBundle](GameBundle.md) (3 shared connections)
- [MovementService](MovementService.md) (3 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (3 shared connections)
- [TargetType](TargetType.md) (3 shared connections)
- [assert_event_envelope](assert_event_envelope.md) (3 shared connections)
- [UserManager](UserManager.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 285 (94%)
- INFERRED: 18 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*