# Follow Movement

> 38 nodes

## Key Concepts

- **follow_movement.py** (27 connections) — `server/game/follow_movement.py`
- **_FollowMovementHost** (18 connections) — `server/game/follow_movement.py`
- **test_follow_movement.py** (15 connections) — `server/tests/unit/game/test_follow_movement.py`
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
- **test_propagate_exception_drops_follower()** (5 connections) — `server/tests/unit/game/test_follow_movement.py`
- **drop_follower()** (4 connections) — `server/game/follow_movement.py`
- **test_ensure_follower_standing_swallows_lookup_errors()** (4 connections) — `server/tests/unit/game/test_follow_movement.py`
- **test_follower_already_in_room_missing_persistence()** (4 connections) — `server/tests/unit/game/test_follow_movement.py`
- **test_follower_already_in_room_true_and_false()** (4 connections) — `server/tests/unit/game/test_follow_movement.py`
- **test_propagate_skips_when_already_in_room()** (4 connections) — `server/tests/unit/game/test_follow_movement.py`
- **test_propagate_unfollow_when_cannot_stand()** (4 connections) — `server/tests/unit/game/test_follow_movement.py`
- **test_stand_follower_no_position_service_returns_true()** (4 connections) — `server/tests/unit/game/test_follow_movement.py`
- **.unfollow()** (3 connections) — `server/game/follow_movement.py`
- **test_follower_needs_stand_rejects_non_string_position()** (2 connections) — `server/tests/unit/game/test_follow_movement.py`
- **UUID** (2 connections)
- **.get_followers()** (1 connections) — `server/game/follow_movement.py`
- *... and 13 more nodes in this community*

## Relationships

- [Follow Service](Follow_Service.md) (13 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (6 shared connections)
- [Test Player Position Service](Test_Player_Position_Service.md) (3 shared connections)
- [Posture Notify](Posture_Notify.md) (3 shared connections)
- [Test Player Event Handlers Room](Test_Player_Event_Handlers_Room.md) (2 shared connections)
- [Test Websocket Handler Validation Errors](Test_Websocket_Handler_Validation_Errors.md) (1 shared connections)
- [Test Movement Service](Test_Movement_Service.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/game/follow_movement.py`
- `server/tests/unit/game/test_follow_movement.py`

## Audit Trail

- EXTRACTED: 97 (91%)
- INFERRED: 10 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*