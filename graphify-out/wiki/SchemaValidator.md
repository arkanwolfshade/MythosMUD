# SchemaValidator

> 81 nodes · cohesion 0.04

## Key Concepts

- **FollowService** (81 connections) — `server/game/follow_service.py`
- **test_follow_service.py** (55 connections) — `server/tests/unit/game/test_follow_service.py`
- **asyncio** (22 connections)
- **test_follow_request_event_envelope_shape()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_npc_entered_room_moves_followers()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_move_failure_auto_unfollow()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_moves_followers()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_no_from_room_id_skips_propagation()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_accept_follow_invalid_request_id()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_accept_follow_success()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_decline_follow_success()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_already_standing()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_fails_to_stand()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_sitting_stands()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_expire_pending_requests_removes_stale()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_following_npc()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_following_player_resolves_name()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_not_following()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_disconnect_cancels_pending_requests()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_already_following_rejected()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_npc_immediate()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_player_creates_pending()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_player_muted_auto_decline()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_self_rejected()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_send_unfollow_notice_falls_back_to_id_without_persistence()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- *... and 56 more nodes in this community*

## Relationships

- [ManualPage.tsx](ManualPage.tsx.md) (20 shared connections)
- [_CombatServiceDeps](_CombatServiceDeps.md) (16 shared connections)
- [analyze_file](analyze_file.md) (6 shared connections)
- [BaseEvent](BaseEvent.md) (6 shared connections)
- [CombatInstance](CombatInstance.md) (4 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [LogAggregator](LogAggregator.md) (3 shared connections)
- [Petersen's Abominations.md](Petersen's_Abominations.md.md) (2 shared connections)
- [SpellLearningService](SpellLearningService.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [_find_item_in_equipped](_find_item_in_equipped.md) (1 shared connections)
- [asyncio](asyncio.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 150 (74%)
- INFERRED: 52 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*