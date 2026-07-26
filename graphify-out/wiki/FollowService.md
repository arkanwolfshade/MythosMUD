# FollowService

> 28 nodes · cohesion 0.14

## Key Concepts

- **FollowService** (36 connections) — `server/game/follow_service.py`
- **UUID** (14 connections)
- **_str_id()** (13 connections) — `server/game/follow_service.py`
- **.request_follow()** (9 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/follow_service.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **Any** (7 connections)
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (5 connections) — `server/game/follow_service.py`
- **.on_player_disconnect()** (4 connections) — `server/game/follow_service.py`
- **Send a command_response-style message to a single player.** (1 connections) — `server/game/follow_service.py`
- **Request to follow a player (pending acceptance) or start following an NPC immedi** (1 connections) — `server/game/follow_service.py`
- **Send follow_request event to the target player only.** (1 connections) — `server/game/follow_service.py`
- **Accept a follow request. Target is the player who accepted (the followee).** (1 connections) — `server/game/follow_service.py`
- **Decline a follow request.** (1 connections) — `server/game/follow_service.py`
- **Return list of follower player IDs (for movement propagation).** (1 connections) — `server/game/follow_service.py`
- **Return (target_id, target_type) if following someone, else None.** (1 connections) — `server/game/follow_service.py`
- **Return stored display name when following an NPC, else None. For players, resolv** (1 connections) — `server/game/follow_service.py`
- **Format who you follow and who follows you for /following output.** (1 connections) — `server/game/follow_service.py`
- **Normalize ID to string for dict keys.** (1 connections) — `server/game/follow_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [._handle_npc_follower_move](_handle_npc_follower_move.md) (20 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [__init__.py](__init__.py.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [MovementService](MovementService.md) (1 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [UserManager](UserManager.md) (1 shared connections)
- [follow_service](follow_service.md) (1 shared connections)
- [_is_npc_follow_value](_is_npc_follow_value.md) (1 shared connections)
- [send_game_event](send_game_event.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`

## Audit Trail

- EXTRACTED: 144 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*