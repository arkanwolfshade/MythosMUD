# PlayerEnteredRoom

> 241 nodes

## Key Concepts

- **PlayerEnteredRoom** (87 connections) — `server/events/event_types.py`
- **FollowService** (81 connections) — `server/game/follow_service.py`
- **test_follow_service.py** (55 connections) — `server/tests/unit/game/test_follow_service.py`
- **follow_service.py** (31 connections) — `server/game/follow_service.py`
- **follow_movement.py** (29 connections) — `server/game/follow_movement.py`
- **asyncio** (22 connections)
- **_FollowMovementHost** (20 connections) — `server/game/follow_movement.py`
- **test_reaction_revival_integration.py** (17 connections) — `server/tests/unit/npc/test_reaction_revival_integration.py`
- **FollowActionResult** (15 connections) — `server/game/follow_types.py`
- **str_id()** (15 connections) — `server/game/follow_types.py`
- **test_follow_flow.py** (14 connections) — `server/tests/integration/test_follow_flow.py`
- **test_follow_movement.py** (14 connections) — `server/tests/unit/game/test_follow_movement.py`
- **FollowPersistence** (12 connections) — `server/game/follow_types.py`
- **follow_types.py** (12 connections) — `server/game/follow_types.py`
- **FollowStatePayload** (11 connections) — `server/game/follow_types.py`
- **propagate_follower_move()** (11 connections) — `server/game/follow_movement.py`
- **.request_follow()** (10 connections) — `server/game/follow_service.py`
- **_host()** (9 connections) — `server/tests/unit/game/test_follow_movement.py`
- **_shopkeeper()** (9 connections) — `server/tests/unit/npc/test_reaction_revival_integration.py`
- **UUID** (9 connections)
- **FollowPlayerView** (8 connections) — `server/game/follow_types.py`
- **.get_following_display()** (8 connections) — `server/game/follow_service.py`
- **.__init__()** (8 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/follow_service.py`
- **is_npc_follow_value()** (8 connections) — `server/game/follow_types.py`
- *... and 216 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (38 shared connections)
- [NPCBase](NPCBase.md) (22 shared connections)
- [EventBus](EventBus.md) (15 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (9 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (8 shared connections)
- [NPCDied](NPCDied.md) (7 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (6 shared connections)
- [CorruptionTier](CorruptionTier.md) (5 shared connections)
- [MovementService](MovementService.md) (5 shared connections)
- [test_player_event_handlers.py](test_player_event_handlers.py.md) (4 shared connections)
- [._bind_event_type](_bind_event_type.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/follow_movement.py`
- `server/game/follow_service.py`
- `server/game/follow_types.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_movement.py`
- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_reaction_revival_integration.py`
- `server/tests/unit/realtime/test_event_handler.py`

## Audit Trail

- EXTRACTED: 527 (86%)
- INFERRED: 89 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*