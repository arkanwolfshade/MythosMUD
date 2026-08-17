# PlayerPositionService

> 220 nodes

## Key Concepts

- **PlayerPositionService** (48 connections) — `server/services/player_position_service.py`
- **test_follow_service.py** (48 connections) — `server/tests/unit/game/test_follow_service.py`
- **FollowService** (39 connections) — `server/game/follow_service.py`
- **test_player_position_service.py** (28 connections) — `server/tests/unit/services/test_player_position_service.py`
- **asyncio** (20 connections)
- **_str_id()** (15 connections) — `server/game/follow_service.py`
- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **asyncio** (12 connections)
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.request_follow()** (10 connections) — `server/game/follow_service.py`
- **UUID** (10 connections)
- **._send_follow_state_to_player()** (9 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (9 connections) — `server/game/follow_service.py`
- **._handle_npc_follower_move()** (8 connections) — `server/game/follow_service.py`
- **._handle_player_follower_move()** (8 connections) — `server/game/follow_service.py`
- **.__init__()** (8 connections) — `server/game/follow_service.py`
- **.unfollow()** (8 connections) — `server/game/follow_service.py`
- **Any** (8 connections)
- **Player** (8 connections)
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **._schedule_coro()** (7 connections) — `server/game/follow_service.py`
- **PositionChangeResponse** (6 connections) — `server/services/player_position_service.py`
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- *... and 195 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (28 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [position_commands.py](position_commands.py.md) (4 shared connections)
- [log_and_raise](log_and_raise.md) (3 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (3 shared connections)
- [TargetType](TargetType.md) (3 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [.__post_init__](__post_init__.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [bundles/game.py](bundles-game.py.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/follow_service.py`
- `server/services/player_position_service.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 379 (90%)
- INFERRED: 44 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*