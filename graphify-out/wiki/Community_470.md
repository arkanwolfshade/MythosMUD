# Community 470

> 38 nodes

## Key Concepts

- **.request_follow()** (9 connections) — `server/game/follow_service.py`
- **UUID** (9 connections)
- **._send_result_to_player()** (8 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (7 connections) — `server/game/follow_service.py`
- **FollowActionResult** (7 connections)
- **.accept_follow()** (6 connections) — `server/game/follow_service.py`
- **._create_pending_follow_request()** (6 connections) — `server/game/follow_service.py`
- **.decline_follow()** (6 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (6 connections) — `server/game/follow_service.py`
- **._schedule_coro()** (6 connections) — `server/game/follow_service.py`
- **.unfollow()** (6 connections) — `server/game/follow_service.py`
- **._notify_followee_of_unfollow()** (5 connections) — `server/game/follow_service.py`
- **._start_following_npc()** (5 connections) — `server/game/follow_service.py`
- **._follow_request_mute_failure()** (4 connections) — `server/game/follow_service.py`
- **.get_following()** (4 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (4 connections) — `server/game/follow_service.py`
- **._send_unfollow_notice()** (4 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (3 connections) — `server/game/follow_service.py`
- **.on_player_disconnect()** (3 connections) — `server/game/follow_service.py`
- **TargetType** (2 connections)
- **FollowStatePayload** (1 connections)
- **Fire-and-forget; close coro if no running event loop (e.g. sync unit tests).…** (1 connections) — `server/game/follow_service.py`
- **Send a command_response-style message to a single player.** (1 connections) — `server/game/follow_service.py`
- **Send follow_state event so client can update title panel (who I am following).** (1 connections) — `server/game/follow_service.py`
- **Immediately attach follow state for an NPC target.** (1 connections) — `server/game/follow_service.py`
- *... and 13 more nodes in this community*

## Relationships

- [Community 99](Community_99.md) (18 shared connections)
- [Community 233](Community_233.md) (2 shared connections)
- [Community 41](Community_41.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`

## Audit Trail

- EXTRACTED: 75 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*