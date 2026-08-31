# follow_movement.py

> 26 nodes

## Key Concepts

- **follow_movement.py** (28 connections) — `server/game/follow_movement.py`
- **_FollowMovementHost** (20 connections) — `server/game/follow_movement.py`
- **propagate_follower_move()** (8 connections) — `server/game/follow_movement.py`
- **ensure_follower_standing()** (6 connections) — `server/game/follow_movement.py`
- **stand_follower_for_move()** (6 connections) — `server/game/follow_movement.py`
- **on_npc_entered_room()** (5 connections) — `server/game/follow_movement.py`
- **on_player_entered_room()** (5 connections) — `server/game/follow_movement.py`
- **drop_follower()** (4 connections) — `server/game/follow_movement.py`
- **follower_already_in_room()** (4 connections) — `server/game/follow_movement.py`
- **follower_needs_stand()** (4 connections) — `server/game/follow_movement.py`
- **.unfollow()** (3 connections) — `server/game/follow_movement.py`
- **._send_follow_state_to_player()** (2 connections) — `server/game/follow_movement.py`
- **UUID** (2 connections)
- **.get_followers()** (1 connections) — `server/game/follow_movement.py`
- **._send_result_to_player()** (1 connections) — `server/game/follow_movement.py`
- **Protocol** (1 connections)
- **Follower auto-stand and movement propagation for FollowService.** (1 connections) — `server/game/follow_movement.py`
- **True when follower is already at room_id (duplicate enter events).** (1 connections) — `server/game/follow_movement.py`
- **Unfollow and notify the follower they lost their target.** (1 connections) — `server/game/follow_movement.py`
- **Stand, move, and notify one follower into the target's new room.** (1 connections) — `server/game/follow_movement.py`
- **Move followers when the followed player moves.** (1 connections) — `server/game/follow_movement.py`
- **Move followers when the followed NPC moves.** (1 connections) — `server/game/follow_movement.py`
- **FollowService surface required by movement helpers.** (1 connections) — `server/game/follow_movement.py`
- **True when follower posture is sitting or lying (must stand to move).** (1 connections) — `server/game/follow_movement.py`
- **Stand a sitting/lying follower; emit posture on success. False if stand fails.** (1 connections) — `server/game/follow_movement.py`
- *... and 1 more nodes in this community*

## Relationships

- [FollowService](FollowService.md) (13 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (3 shared connections)
- [event_types.py](event_types.py.md) (3 shared connections)
- [player_event_handlers_state.py](player_event_handlers_state.py.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [MovementService](MovementService.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/game/follow_movement.py`

## Audit Trail

- EXTRACTED: 60 (86%)
- INFERRED: 10 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*