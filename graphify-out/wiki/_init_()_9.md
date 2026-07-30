# . init ()

> 52 nodes

## Key Concepts

- **FollowService** (37 connections) — `server/game/follow_service.py`
- **UUID** (14 connections)
- **_str_id()** (13 connections) — `server/game/follow_service.py`
- **.request_follow()** (9 connections) — `server/game/follow_service.py`
- **._handle_player_follower_move()** (9 connections) — `server/game/follow_service.py`
- **._handle_npc_follower_move()** (9 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (8 connections) — `server/game/follow_service.py`
- **.unfollow()** (8 connections) — `server/game/follow_service.py`
- **Any** (7 connections)
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **._ensure_follower_standing()** (6 connections) — `server/game/follow_service.py`
- **._on_player_entered_room()** (6 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (5 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- **._on_npc_entered_room()** (5 connections) — `server/game/follow_service.py`
- **._send_result_and_player_update()** (4 connections) — `server/game/follow_service.py`
- **.on_player_disconnect()** (4 connections) — `server/game/follow_service.py`
- **follow_service()** (3 connections) — `server/tests/integration/test_follow_flow.py`
- *... and 27 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (15 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (4 shared connections)
- [Any](Any.md) (4 shared connections)
- [test command service](test_command_service.md) (3 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (3 shared connections)
- [real time](real_time.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 224 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*