# FollowService

> 49 nodes

## Key Concepts

- **FollowService** (39 connections) — `server/game/follow_service.py`
- **_str_id()** (15 connections) — `server/game/follow_service.py`
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
- **._ensure_follower_standing()** (5 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- **._on_npc_entered_room()** (5 connections) — `server/game/follow_service.py`
- **._send_result_and_player_update()** (5 connections) — `server/game/follow_service.py`
- **.on_player_disconnect()** (4 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (4 connections) — `server/game/follow_service.py`
- *... and 24 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (7 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (6 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [send_game_event](send_game_event.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [test_follow_flow.py](test_follow_flow.py.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [MovementService](MovementService.md) (2 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [UserManager](UserManager.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`

## Audit Trail

- EXTRACTED: 123 (90%)
- INFERRED: 13 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*