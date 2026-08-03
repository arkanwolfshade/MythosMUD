# follow game service

> 52 nodes

## Key Concepts

- **FollowService** (37 connections) — `server/game/follow_service.py`
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
- **._on_npc_entered_room()** (5 connections) — `server/game/follow_service.py`
- **._send_result_and_player_update()** (4 connections) — `server/game/follow_service.py`
- *... and 27 more nodes in this community*

## Relationships

- [item models rationale](item_models_rationale.md) (11 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [Room Broadcast](Room_Broadcast.md) (4 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (4 shared connections)
- [position player service](position_player_service.md) (3 shared connections)
- [services user manager](services_user_manager.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [persistence services combat](persistence_services_combat.md) (3 shared connections)
- [party service game](party_service_game.md) (3 shared connections)
- [target resolution service](target_resolution_service.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)

## Source Files

- `server/game/follow_service.py`

## Audit Trail

- EXTRACTED: 250 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*