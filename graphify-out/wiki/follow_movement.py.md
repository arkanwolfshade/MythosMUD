# follow_movement.py

> 38 nodes

## Key Concepts

- **follow_movement.py** (29 connections) — `server/game/follow_movement.py`
- **_FollowMovementHost** (20 connections) — `server/game/follow_movement.py`
- **test_follow_movement.py** (14 connections) — `server/tests/unit/game/test_follow_movement.py`
- **propagate_follower_move()** (11 connections) — `server/game/follow_movement.py`
- **_host()** (9 connections) — `server/tests/unit/game/test_follow_movement.py`
- **asyncio** (8 connections)
- **ensure_follower_standing()** (7 connections) — `server/game/follow_movement.py`
- **stand_follower_for_move()** (7 connections) — `server/game/follow_movement.py`
- **follower_already_in_room()** (6 connections) — `server/game/follow_movement.py`
- **on_npc_entered_room()** (6 connections) — `server/game/follow_movement.py`
- **follower_needs_stand()** (5 connections) — `server/game/follow_movement.py`
- **on_player_entered_room()** (5 connections) — `server/game/follow_movement.py`
- **test_on_npc_entered_room_skips_without_movement_service()** (5 connections) — `server/tests/unit/game/test_follow_movement.py`
- **drop_follower()** (4 connections) — `server/game/follow_movement.py`
- **test_ensure_follower_standing_swallows_lookup_errors()** (4 connections) — `server/tests/unit/game/test_follow_movement.py`
- **test_follower_already_in_room_missing_persistence()** (4 connections) — `server/tests/unit/game/test_follow_movement.py`
- **test_follower_already_in_room_true_and_false()** (4 connections) — `server/tests/unit/game/test_follow_movement.py`
- **test_propagate_exception_drops_follower()** (4 connections) — `server/tests/unit/game/test_follow_movement.py`
- **test_propagate_skips_when_already_in_room()** (4 connections) — `server/tests/unit/game/test_follow_movement.py`
- **test_propagate_unfollow_when_cannot_stand()** (4 connections) — `server/tests/unit/game/test_follow_movement.py`
- **test_stand_follower_no_position_service_returns_true()** (4 connections) — `server/tests/unit/game/test_follow_movement.py`
- **.unfollow()** (3 connections) — `server/game/follow_movement.py`
- **test_follower_needs_stand_rejects_non_string_position()** (2 connections) — `server/tests/unit/game/test_follow_movement.py`
- **UUID** (2 connections)
- **.get_followers()** (1 connections) — `server/game/follow_movement.py`
- *... and 13 more nodes in this community*

## Relationships

- [follow_service.py](follow_service.py.md) (13 shared connections)
- [event_types.py](event_types.py.md) (6 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (3 shared connections)
- [emit_posture_change](emit_posture_change.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [MovementService](MovementService.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/game/follow_movement.py`
- `server/tests/unit/game/test_follow_movement.py`

## Audit Trail

- EXTRACTED: 98 (90%)
- INFERRED: 11 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*