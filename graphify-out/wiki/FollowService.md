# FollowService

> 275 nodes

## Key Concepts

- **FollowService** (74 connections) — `server/game/follow_service.py`
- **test_follow_service.py** (51 connections) — `server/tests/unit/game/test_follow_service.py`
- **PlayerPositionService** (50 connections) — `server/services/player_position_service.py`
- **follow_service.py** (32 connections) — `server/game/follow_service.py`
- **follow_movement.py** (29 connections) — `server/game/follow_movement.py`
- **test_player_position_service.py** (28 connections) — `server/tests/unit/services/test_player_position_service.py`
- **_FollowMovementHost** (20 connections) — `server/game/follow_movement.py`
- **asyncio** (20 connections)
- **player_position_service.py** (18 connections) — `server/services/player_position_service.py`
- **FollowActionResult** (15 connections) — `server/game/follow_types.py`
- **str_id()** (15 connections) — `server/game/follow_types.py`
- **test_follow_movement.py** (15 connections) — `server/tests/unit/game/test_follow_movement.py`
- **PositionPlayer** (13 connections) — `server/services/player_position_service.py`
- **FollowPersistence** (12 connections) — `server/game/follow_types.py`
- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **follow_types.py** (12 connections) — `server/game/follow_types.py`
- **asyncio** (12 connections)
- **FollowStatePayload** (11 connections) — `server/game/follow_types.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **propagate_follower_move()** (11 connections) — `server/game/follow_movement.py`
- **.request_follow()** (10 connections) — `server/game/follow_service.py`
- **_host()** (9 connections) — `server/tests/unit/game/test_follow_movement.py`
- **UUID** (9 connections)
- **FollowPlayerView** (8 connections) — `server/game/follow_types.py`
- **.get_following_display()** (8 connections) — `server/game/follow_service.py`
- *... and 250 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (14 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (9 shared connections)
- [position_commands.py](position_commands.py.md) (9 shared connections)
- [MovementService](MovementService.md) (6 shared connections)
- [build_event](build_event.md) (6 shared connections)
- [event_types.py](event_types.py.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [test_follow_flow.py](test_follow_flow.py.md) (3 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (3 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/follow_movement.py`
- `server/game/follow_service.py`
- `server/game/follow_types.py`
- `server/services/player_position_service.py`
- `server/tests/unit/game/test_follow_movement.py`
- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 540 (88%)
- INFERRED: 77 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*