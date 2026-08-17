# server tests unit game test

> 80 nodes

## Key Concepts

- **test_follow_service.py** (48 connections) — `server/tests/unit/game/test_follow_service.py`
- **asyncio** (20 connections)
- **test_follow_request_event_envelope_shape()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **fixture** (5 connections)
- **follow_service()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_npc_entered_room_moves_followers()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_move_failure_auto_unfollow()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_moves_followers()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_no_from_room_id_skips_propagation()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **connection_manager()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **event_bus()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **movement_service()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_accept_follow_invalid_request_id()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_accept_follow_success()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_decline_follow_success()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_already_standing()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_fails_to_stand()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_sitting_stands()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_expire_pending_requests_removes_stale()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_following_npc()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_following_player_resolves_name()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_not_following()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_disconnect_cancels_pending_requests()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_already_following_rejected()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_npc_immediate()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- *... and 55 more nodes in this community*

## Relationships

- [followtargetvalue](followtargetvalue.md) (7 shared connections)
- [server events event types playerenteredroom](server_events_event_types_playerenteredroom.md) (4 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (3 shared connections)
- [moduletype](moduletype.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [server events event bus](server_events_event_bus.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 113 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*