# Follow Service Tests

> 66 nodes · cohesion 0.03

## Key Concepts

- **test_follow_service.py** (36 connections) — `server/tests/unit/game/test_follow_service.py`
- **follow_service()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_npc_entered_room_moves_followers()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_move_failure_auto_unfollow()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_moves_followers()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_no_from_room_id_skips_propagation()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **connection_manager()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **event_bus()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **movement_service()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_accept_follow_invalid_request_id()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_accept_follow_success()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_decline_follow_success()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_already_standing()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_fails_to_stand()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_sitting_stands()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_follow_request_ttl_constant()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_followers_empty()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_followers_multiple()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_following_npc()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_following_player_resolves_name()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_not_following()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_none()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_returns_tuple()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_disconnect_cancels_pending_requests()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_disconnect_clears_follow_state()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- *... and 41 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (8 shared connections)

## Source Files

- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 138 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
