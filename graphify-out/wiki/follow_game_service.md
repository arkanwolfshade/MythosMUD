# follow game service

> 48 nodes

## Key Concepts

- **FollowService** (39 connections) — `server/game/follow_service.py`
- **_str_id()** (15 connections) — `server/game/follow_service.py`
- **UUID** (14 connections)
- **.request_follow()** (10 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (9 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (9 connections) — `server/game/follow_service.py`
- **._handle_player_follower_move()** (9 connections) — `server/game/follow_service.py`
- **._handle_npc_follower_move()** (9 connections) — `server/game/follow_service.py`
- **Any** (8 connections)
- **.unfollow()** (8 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **._schedule_coro()** (7 connections) — `server/game/follow_service.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **._ensure_follower_standing()** (6 connections) — `server/game/follow_service.py`
- **._on_player_entered_room()** (6 connections) — `server/game/follow_service.py`
- **._send_result_and_player_update()** (5 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (5 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- **._on_npc_entered_room()** (5 connections) — `server/game/follow_service.py`
- **.on_player_disconnect()** (4 connections) — `server/game/follow_service.py`
- **follow_service()** (3 connections) — `server/tests/integration/test_follow_flow.py`
- *... and 23 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (11 shared connections)
- [combat services messaging](combat_services_messaging.md) (8 shared connections)
- [party service game](party_service_game.md) (5 shared connections)
- [holiday service services](holiday_service_services.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [schedule services service](schedule_services_service.md) (1 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)
- [position player service](position_player_service.md) (1 shared connections)
- [services user manager](services_user_manager.md) (1 shared connections)
- [admin services auth](admin_services_auth.md) (1 shared connections)
- [command parser rationale](command_parser_rationale.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/tests/integration/test_follow_flow.py`

## Audit Trail

- EXTRACTED: 228 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*