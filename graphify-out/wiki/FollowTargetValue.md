# FollowTargetValue

> 132 nodes

## Key Concepts

- **NPCEnteredRoom** (51 connections) — `server/events/event_types.py`
- **test_follow_service.py** (38 connections) — `server/tests/unit/game/test_follow_service.py`
- **FollowService** (36 connections) — `server/game/follow_service.py`
- **follow_service.py** (24 connections) — `server/game/follow_service.py`
- **UUID** (14 connections)
- **_str_id()** (13 connections) — `server/game/follow_service.py`
- **.__init__()** (10 connections) — `server/game/follow_service.py`
- **.request_follow()** (9 connections) — `server/game/follow_service.py`
- **._handle_player_follower_move()** (9 connections) — `server/game/follow_service.py`
- **._handle_npc_follower_move()** (9 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (8 connections) — `server/game/follow_service.py`
- **.unfollow()** (8 connections) — `server/game/follow_service.py`
- **Any** (7 connections)
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **._ensure_follower_standing()** (6 connections) — `server/game/follow_service.py`
- **._on_player_entered_room()** (6 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (5 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- *... and 107 more nodes in this community*

## Relationships

- [Any](Any.md) (33 shared connections)
- [.initialize()](initialize%28%29.md) (11 shared connections)
- [. repr ()](_repr_%28%29.md) (10 shared connections)
- [main()](main%28%29.md) (8 shared connections)
- [UUID](UUID.md) (8 shared connections)
- [test npc event handlers](test_npc_event_handlers.md) (6 shared connections)
- [Player](Player.md) (3 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (3 shared connections)
- [combat taunt](combat_taunt.md) (3 shared connections)
- [spawn defaults](spawn_defaults.md) (2 shared connections)
- [.get population stats()](get_population_stats%28%29.md) (2 shared connections)
- [. post init ()](_post_init_%28%29.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/models/room.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/realtime/event_handler.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/realtime/test_event_handler.py`

## Audit Trail

- EXTRACTED: 452 (94%)
- INFERRED: 30 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*