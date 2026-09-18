# NPC Follow System

> 197 nodes

## Key Concepts

- **FollowService** (65 connections) — `server/game/follow_service.py`
- **test_follow_service.py** (50 connections) — `server/tests/unit/game/test_follow_service.py`
- **NPCEnteredRoom** (35 connections) — `server/events/event_types.py`
- **follow_movement.py** (29 connections) — `server/game/follow_movement.py`
- **_FollowMovementHost** (20 connections) — `server/game/follow_movement.py`
- **asyncio** (20 connections)
- **test_follow_movement.py** (14 connections) — `server/tests/unit/game/test_follow_movement.py`
- **follow_types.py** (12 connections) — `server/game/follow_types.py`
- **propagate_follower_move()** (11 connections) — `server/game/follow_movement.py`
- **.request_follow()** (9 connections) — `server/game/follow_service.py`
- **_host()** (9 connections) — `server/tests/unit/game/test_follow_movement.py`
- **UUID** (9 connections)
- **FollowPlayerView** (8 connections) — `server/game/follow_types.py`
- **FollowStatePayload** (8 connections) — `server/game/follow_types.py`
- **.__init__()** (8 connections) — `server/game/follow_service.py`
- **asyncio** (8 connections)
- **ensure_follower_standing()** (7 connections) — `server/game/follow_movement.py`
- **stand_follower_for_move()** (7 connections) — `server/game/follow_movement.py`
- **.get_following_display()** (7 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (7 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (7 connections) — `server/game/follow_service.py`
- **FollowActionResult** (7 connections)
- **FollowActionResult** (6 connections) — `server/game/follow_types.py`
- **FollowPersistence** (6 connections) — `server/game/follow_types.py`
- **follower_already_in_room()** (6 connections) — `server/game/follow_movement.py`
- *... and 172 more nodes in this community*

## Relationships

- [NPC Event Types](NPC_Event_Types.md) (14 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (10 shared connections)
- [Community 165](Community_165.md) (6 shared connections)
- [Community 35](Community_35.md) (5 shared connections)
- [Event Bus](Event_Bus.md) (4 shared connections)
- [Community 624](Community_624.md) (4 shared connections)
- [Community 260](Community_260.md) (4 shared connections)
- [Community 92](Community_92.md) (3 shared connections)
- [Community 80](Community_80.md) (3 shared connections)
- [Community 184](Community_184.md) (3 shared connections)
- [Community 41](Community_41.md) (2 shared connections)
- [NPC Population Control](NPC_Population_Control.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/follow_movement.py`
- `server/game/follow_service.py`
- `server/game/follow_types.py`
- `server/tests/unit/game/test_follow_movement.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 365 (86%)
- INFERRED: 60 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*