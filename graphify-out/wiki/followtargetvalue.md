# followtargetvalue

> 174 nodes

## Key Concepts

- **test_follow_service.py** (48 connections) — `server/tests/unit/game/test_follow_service.py`
- **FollowService** (39 connections) — `server/game/follow_service.py`
- **send_game_event()** (29 connections) — `server/realtime/connection_manager_api.py`
- **asyncio** (20 connections)
- **_str_id()** (15 connections) — `server/game/follow_service.py`
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **resolve_lazy_attr()** (11 connections) — `server/realtime/connection_manager_lazy.py`
- **test_connection_manager_api.py** (11 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **.request_follow()** (10 connections) — `server/game/follow_service.py`
- **UUID** (10 connections)
- **._send_follow_state_to_player()** (9 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (9 connections) — `server/game/follow_service.py`
- **._handle_npc_follower_move()** (8 connections) — `server/game/follow_service.py`
- **._handle_player_follower_move()** (8 connections) — `server/game/follow_service.py`
- **.__init__()** (8 connections) — `server/game/follow_service.py`
- **.unfollow()** (8 connections) — `server/game/follow_service.py`
- **_require_manager()** (8 connections) — `server/realtime/connection_manager_api.py`
- **Any** (8 connections)
- **connection_manager_lazy.py** (8 connections) — `server/realtime/connection_manager_lazy.py`
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **._schedule_coro()** (7 connections) — `server/game/follow_service.py`
- *... and 149 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (34 shared connections)
- [server container main get container](server_container_main_get_container.md) (6 shared connections)
- [server game magic mp regeneration](server_game_magic_mp_regeneration.md) (4 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (3 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (3 shared connections)
- [server game magic magic service](server_game_magic_magic_service.md) (3 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [server tests integration test follow](server_tests_integration_test_follow.md) (2 shared connections)
- [moduletype](moduletype.md) (2 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (2 shared connections)
- [server services player position service](server_services_player_position_service.md) (2 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_lazy.py`
- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/realtime/test_connection_manager_api.py`

## Audit Trail

- EXTRACTED: 344 (94%)
- INFERRED: 23 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*