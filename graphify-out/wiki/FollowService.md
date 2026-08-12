# FollowService

> 44 nodes

## Key Concepts

- **FollowService** (36 connections) — `server/game/follow_service.py`
- **_str_id()** (13 connections) — `server/game/follow_service.py`
- **UUID** (10 connections)
- **.request_follow()** (9 connections) — `server/game/follow_service.py`
- **._handle_npc_follower_move()** (8 connections) — `server/game/follow_service.py`
- **._handle_player_follower_move()** (8 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (8 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/follow_service.py`
- **.unfollow()** (8 connections) — `server/game/follow_service.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **Any** (7 connections)
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **._on_player_entered_room()** (6 connections) — `server/game/follow_service.py`
- **._ensure_follower_standing()** (5 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- **._on_npc_entered_room()** (5 connections) — `server/game/follow_service.py`
- **.on_player_disconnect()** (4 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (4 connections) — `server/game/follow_service.py`
- **._send_result_and_player_update()** (4 connections) — `server/game/follow_service.py`
- **Send a command_response-style message to a single player.** (1 connections) — `server/game/follow_service.py`
- **Send command_response with result message and optional player_update (e.g.…** (1 connections) — `server/game/follow_service.py`
- *... and 19 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [send_game_event](send_game_event.md) (3 shared connections)
- [GameBundle](GameBundle.md) (2 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [fixture](fixture.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [MovementService](MovementService.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [Player Mute Persistence](Player_Mute_Persistence.md) (1 shared connections)
- [_is_npc_follow_value](_is_npc_follow_value.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`

## Audit Trail

- EXTRACTED: 198 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*