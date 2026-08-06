# party service game

> 142 nodes

## Key Concepts

- **test_follow_service.py** (47 connections) — `server/tests/unit/game/test_follow_service.py`
- **FollowService** (39 connections) — `server/game/follow_service.py`
- **follow_service.py** (25 connections) — `server/game/follow_service.py`
- **_str_id()** (15 connections) — `server/game/follow_service.py`
- **UUID** (14 connections)
- **test_follow_flow.py** (13 connections) — `server/tests/integration/test_follow_flow.py`
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
- *... and 117 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (22 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (5 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (5 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (5 shared connections)
- [validator room toolkit](validator_room_toolkit.md) (4 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (3 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (2 shared connections)
- [position player service](position_player_service.md) (2 shared connections)
- [services user manager](services_user_manager.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [add used user](add_used_user.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 460 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*