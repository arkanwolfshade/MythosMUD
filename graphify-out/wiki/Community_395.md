# Community 395

> 44 nodes

## Key Concepts

- **follow_movement.py** (23 connections) — `server/game/follow_movement.py`
- **_FollowMovementHost** (17 connections) — `server/game/follow_movement.py`
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
- **._send_follow_state_to_player()** (2 connections) — `server/game/follow_movement.py`
- **test_follower_needs_stand_rejects_non_string_position()** (2 connections) — `server/tests/unit/game/test_follow_movement.py`
- **FollowPlayerView** (2 connections)
- *... and 19 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (4 shared connections)
- [Community 144](Community_144.md) (3 shared connections)
- [Community 79](Community_79.md) (2 shared connections)
- [Community 106](Community_106.md) (2 shared connections)
- [Community 342](Community_342.md) (2 shared connections)
- [NPC Room Lifecycle](NPC_Room_Lifecycle.md) (2 shared connections)
- [Game Event Types](Game_Event_Types.md) (2 shared connections)
- [Community 728](Community_728.md) (1 shared connections)

## Source Files

- `server/game/follow_movement.py`
- `server/tests/unit/game/test_follow_movement.py`

## Audit Trail

- EXTRACTED: 97 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*