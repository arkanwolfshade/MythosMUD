# ._handle_npc_follower_move

> 16 nodes · cohesion 0.15

## Key Concepts

- **._handle_npc_follower_move()** (9 connections) — `server/game/follow_service.py`
- **._handle_player_follower_move()** (9 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (8 connections) — `server/game/follow_service.py`
- **.unfollow()** (8 connections) — `server/game/follow_service.py`
- **._ensure_follower_standing()** (6 connections) — `server/game/follow_service.py`
- **._on_player_entered_room()** (6 connections) — `server/game/follow_service.py`
- **._on_npc_entered_room()** (5 connections) — `server/game/follow_service.py`
- **._send_result_and_player_update()** (4 connections) — `server/game/follow_service.py`
- **Send command_response with result message and optional player_update (e.g. posit** (1 connections) — `server/game/follow_service.py`
- **Send follow_state event so client can update title panel (who I am following).** (1 connections) — `server/game/follow_service.py`
- **Stop following. Returns result message.** (1 connections) — `server/game/follow_service.py`
- **If follower is sitting or prone, try to stand them so they can move.         Ret** (1 connections) — `server/game/follow_service.py`
- **Move followers when the followed player moves.** (1 connections) — `server/game/follow_service.py`
- **Move followers when the followed NPC moves.** (1 connections) — `server/game/follow_service.py`
- **Handle movement propagation for a single follower of a player.          This hel** (1 connections) — `server/game/follow_service.py`
- **Handle movement propagation for a single follower of an NPC.          Extracted** (1 connections) — `server/game/follow_service.py`

## Relationships

- [FollowService](FollowService.md) (20 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [send_game_event](send_game_event.md) (2 shared connections)
- [quest_events.py](quest_events.py.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`

## Audit Trail

- EXTRACTED: 62 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*