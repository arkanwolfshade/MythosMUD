# followtargetvalue

> 57 nodes

## Key Concepts

- **FollowService** (39 connections) — `server/game/follow_service.py`
- **follow_service.py** (26 connections) — `server/game/follow_service.py`
- **send_game_event()** (25 connections) — `server/realtime/connection_manager_api.py`
- **_str_id()** (15 connections) — `server/game/follow_service.py`
- **.request_follow()** (10 connections) — `server/game/follow_service.py`
- **UUID** (10 connections)
- **._send_follow_state_to_player()** (9 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (9 connections) — `server/game/follow_service.py`
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
- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **._ensure_follower_standing()** (5 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- **._on_npc_entered_room()** (5 connections) — `server/game/follow_service.py`
- *... and 32 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [server realtime connection manager api](server_realtime_connection_manager_api.md) (8 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (7 shared connections)
- [server events event types playerenteredroom](server_events_event_types_playerenteredroom.md) (4 shared connections)
- [moduletype](moduletype.md) (4 shared connections)
- [server tests integration test follow](server_tests_integration_test_follow.md) (3 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (3 shared connections)
- [server game movement service movementservice](server_game_movement_service_movementservice.md) (3 shared connections)
- [server commands rest command](server_commands_rest_command.md) (3 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (3 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (3 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (2 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/realtime/connection_manager_api.py`

## Audit Trail

- EXTRACTED: 171 (93%)
- INFERRED: 13 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*