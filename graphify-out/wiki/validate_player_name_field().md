# .validate player name field()

> 164 nodes

## Key Concepts

- **PlayerEnteredRoom** (71 connections) — `server/events/event_types.py`
- **test_follow_service.py** (41 connections) — `server/tests/unit/game/test_follow_service.py`
- **FollowService** (37 connections) — `server/game/follow_service.py`
- **follow_service.py** (24 connections) — `server/game/follow_service.py`
- **UUID** (14 connections)
- **_str_id()** (13 connections) — `server/game/follow_service.py`
- **test_follow_flow.py** (13 connections) — `server/tests/integration/test_follow_flow.py`
- **.__init__()** (10 connections) — `server/game/follow_service.py`
- **RoomEventHandler** (10 connections) — `server/realtime/integration/room_event_handler.py`
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
- **.player_entered_room_greeting()** (7 connections) — `server/npc/event_reaction_system.py`
- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **._ensure_follower_standing()** (6 connections) — `server/game/follow_service.py`
- **._on_player_entered_room()** (6 connections) — `server/game/follow_service.py`
- *... and 139 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (40 shared connections)
- [world](world.md) (8 shared connections)
- [. call ()](_call_%28%29.md) (8 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (6 shared connections)
- [UUID](UUID.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [Any](Any.md) (4 shared connections)
- [circuit breaker](circuit_breaker.md) (4 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (4 shared connections)
- [combat initialization](combat_initialization.md) (3 shared connections)
- [personal interest 4()](personal_interest_4%28%29.md) (3 shared connections)
- [Test exception tracking functionality.](Test_exception_tracking_functionality.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/npc/event_reaction_system.py`
- `server/realtime/integration/room_event_handler.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`

## Audit Trail

- EXTRACTED: 558 (94%)
- INFERRED: 33 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*