# party service game

> 132 nodes

## Key Concepts

- **test_follow_service.py** (47 connections) — `server/tests/unit/game/test_follow_service.py`
- **FollowService** (39 connections) — `server/game/follow_service.py`
- **follow_service.py** (25 connections) — `server/game/follow_service.py`
- **_str_id()** (15 connections) — `server/game/follow_service.py`
- **UUID** (14 connections)
- **.__init__()** (10 connections) — `server/game/follow_service.py`
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
- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **._ensure_follower_standing()** (6 connections) — `server/game/follow_service.py`
- **._on_player_entered_room()** (6 connections) — `server/game/follow_service.py`
- **._send_result_and_player_update()** (5 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (5 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- *... and 107 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (19 shared connections)
- [Error Conversion](Error_Conversion.md) (7 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (5 shared connections)
- [Room Broadcast](Room_Broadcast.md) (4 shared connections)
- [skill game service](skill_game_service.md) (4 shared connections)
- [message nats handler](message_nats_handler.md) (3 shared connections)
- [position player service](position_player_service.md) (3 shared connections)
- [target resolution service](target_resolution_service.md) (3 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (3 shared connections)
- [room look commands](room_look_commands.md) (2 shared connections)
- [services user manager](services_user_manager.md) (2 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 438 (98%)
- INFERRED: 11 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*