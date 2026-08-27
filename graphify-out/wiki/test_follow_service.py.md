# test_follow_service.py

> 168 nodes

## Key Concepts

- **test_follow_service.py** (48 connections) — `server/tests/unit/game/test_follow_service.py`
- **NPCEnteredRoom** (46 connections) — `server/events/event_types.py`
- **FollowService** (39 connections) — `server/game/follow_service.py`
- **follow_service.py** (26 connections) — `server/game/follow_service.py`
- **asyncio** (20 connections)
- **_str_id()** (15 connections) — `server/game/follow_service.py`
- **test_follow_flow.py** (15 connections) — `server/tests/integration/test_follow_flow.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.request_follow()** (10 connections) — `server/game/follow_service.py`
- **UUID** (10 connections)
- **._send_follow_state_to_player()** (9 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (9 connections) — `server/game/follow_service.py`
- **assert_event_envelope()** (9 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **._handle_npc_follower_move()** (8 connections) — `server/game/follow_service.py`
- **._handle_player_follower_move()** (8 connections) — `server/game/follow_service.py`
- **.__init__()** (8 connections) — `server/game/follow_service.py`
- **.unfollow()** (8 connections) — `server/game/follow_service.py`
- **Any** (8 connections)
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **._schedule_coro()** (7 connections) — `server/game/follow_service.py`
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **._on_player_entered_room()** (6 connections) — `server/game/follow_service.py`
- *... and 143 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (11 shared connections)
- [time.py](time.py.md) (11 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (6 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (6 shared connections)
- [EventBus](EventBus.md) (6 shared connections)
- [NPCBase](NPCBase.md) (5 shared connections)
- [Room](Room.md) (5 shared connections)
- [.__post_init__](__post_init__.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (5 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (4 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/npc/movement_integration.py`
- `server/npc/spawning_service.py`
- `server/realtime/event_handler.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/realtime/envelope_assertions.py`

## Audit Trail

- EXTRACTED: 342 (92%)
- INFERRED: 30 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*