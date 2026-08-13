# PlayerEnteredRoom

> 154 nodes

## Key Concepts

- **PlayerEnteredRoom** (56 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (43 connections) — `server/events/event_types.py`
- **test_follow_service.py** (38 connections) — `server/tests/unit/game/test_follow_service.py`
- **FollowService** (36 connections) — `server/game/follow_service.py`
- **follow_service.py** (24 connections) — `server/game/follow_service.py`
- **asyncio** (19 connections)
- **test_follow_flow.py** (14 connections) — `server/tests/integration/test_follow_flow.py`
- **_str_id()** (13 connections) — `server/game/follow_service.py`
- **UUID** (10 connections)
- **.request_follow()** (9 connections) — `server/game/follow_service.py`
- **._handle_npc_follower_move()** (8 connections) — `server/game/follow_service.py`
- **._handle_player_follower_move()** (8 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (8 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/follow_service.py`
- **.unfollow()** (8 connections) — `server/game/follow_service.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **Any** (7 connections)
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **._on_player_entered_room()** (6 connections) — `server/game/follow_service.py`
- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **._ensure_follower_standing()** (5 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- *... and 129 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (34 shared connections)
- [event_types.py](event_types.py.md) (19 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (15 shared connections)
- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (8 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_player_event_handlers.py](test_player_event_handlers.py.md) (4 shared connections)
- [send_game_event](send_game_event.md) (4 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [TargetMatch](TargetMatch.md) (3 shared connections)
- [.__post_init__](__post_init__.md) (2 shared connections)
- [quest_events.py](quest_events.py.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/movement_integration.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/realtime/event_handler.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/npc/test_population_control.py`

## Audit Trail

- EXTRACTED: 347 (95%)
- INFERRED: 20 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*