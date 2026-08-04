# party service game

> 137 nodes

## Key Concepts

- **test_follow_service.py** (47 connections) — `server/tests/unit/game/test_follow_service.py`
- **FollowService** (39 connections) — `server/game/follow_service.py`
- **_str_id()** (15 connections) — `server/game/follow_service.py`
- **UUID** (14 connections)
- **assert_event_envelope()** (11 connections) — `server/tests/unit/realtime/envelope_assertions.py`
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
- **envelope_assertions.py** (6 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **._send_result_and_player_update()** (5 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (5 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- *... and 112 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (24 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (3 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (3 shared connections)
- [command parser rationale](command_parser_rationale.md) (3 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (3 shared connections)
- [combat messaging services](combat_messaging_services.md) (3 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)
- [position player service](position_player_service.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/realtime/envelope_assertions.py`
- `server/tests/unit/services/test_combat_messaging_integration.py`

## Audit Trail

- EXTRACTED: 432 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*