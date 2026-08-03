# follow game service

> 28 nodes

## Key Concepts

- **UUID** (14 connections)
- **_str_id()** (13 connections) — `server/game/follow_service.py`
- **.request_follow()** (9 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/follow_service.py`
- **Any** (7 connections)
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (5 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- **.on_player_disconnect()** (4 connections) — `server/game/follow_service.py`
- **_FollowTargetValue** (1 connections)
- **TypeGuard** (1 connections)
- **True when v is the 3-tuple (target_id, 'npc', display_name).** (1 connections) — `server/game/follow_service.py`
- **Normalize ID to string for dict keys.** (1 connections) — `server/game/follow_service.py`
- **Remove expired pending requests and notify requestors.** (1 connections) — `server/game/follow_service.py`
- **Send a command_response-style message to a single player.** (1 connections) — `server/game/follow_service.py`
- **Request to follow a player (pending acceptance) or start following an NPC immedi** (1 connections) — `server/game/follow_service.py`
- **Send follow_request event to the target player only.** (1 connections) — `server/game/follow_service.py`
- **Accept a follow request. Target is the player who accepted (the followee).** (1 connections) — `server/game/follow_service.py`
- **Decline a follow request.** (1 connections) — `server/game/follow_service.py`
- **Return (target_id, target_type) if following someone, else None.** (1 connections) — `server/game/follow_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (26 shared connections)
- [Item Instances](Item_Instances.md) (3 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (1 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`

## Audit Trail

- EXTRACTED: 117 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*