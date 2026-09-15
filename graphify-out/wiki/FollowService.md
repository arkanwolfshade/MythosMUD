# FollowService

> 197 nodes

## Key Concepts

- **FollowService** (74 connections) — `server/game/follow_service.py`
- **test_follow_service.py** (50 connections) — `server/tests/unit/game/test_follow_service.py`
- **NPCEnteredRoom** (49 connections) — `server/events/event_types.py`
- **follow_service.py** (31 connections) — `server/game/follow_service.py`
- **follow_movement.py** (29 connections) — `server/game/follow_movement.py`
- **_FollowMovementHost** (20 connections) — `server/game/follow_movement.py`
- **asyncio** (20 connections)
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
- **is_npc_follow_value()** (8 connections) — `server/game/follow_types.py`
- **asyncio** (8 connections)
- **PendingFollowRequest** (7 connections) — `server/game/follow_types.py`
- **ensure_follower_standing()** (7 connections) — `server/game/follow_movement.py`
- **stand_follower_for_move()** (7 connections) — `server/game/follow_movement.py`
- *... and 172 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (18 shared connections)
- [EventBus](EventBus.md) (8 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (7 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (7 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (6 shared connections)
- [NPCDefinition](NPCDefinition.md) (6 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (6 shared connections)
- [event_handler.py](event_handler.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [send_game_event](send_game_event.md) (4 shared connections)
- [test_follow_flow.py](test_follow_flow.py.md) (3 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/follow_movement.py`
- `server/game/follow_service.py`
- `server/game/follow_types.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/game/test_follow_movement.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 414 (85%)
- INFERRED: 72 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*