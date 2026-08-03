# party service game

> 76 nodes

## Key Concepts

- **test_follow_service.py** (47 connections) — `server/tests/unit/game/test_follow_service.py`
- **follow_service()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_moves_followers()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_move_failure_auto_unfollow()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_npc_entered_room_moves_followers()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_no_from_room_id_skips_propagation()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_expire_pending_requests_removes_stale()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_str_id_accepts_uuid()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **event_bus()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **movement_service()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **user_manager()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **connection_manager()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_self_rejected()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_npc_immediate()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_player_muted_auto_decline()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_player_creates_pending()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_already_following_rejected()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_accept_follow_success()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_decline_follow_success()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_accept_follow_invalid_request_id()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_unfollow_was_following()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_unfollow_was_not_following()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_followers_empty()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_followers_multiple()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_none()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- *... and 51 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (7 shared connections)
- [follow game service](follow_game_service.md) (5 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)

## Source Files

- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 166 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*