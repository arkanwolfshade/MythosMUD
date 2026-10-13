# Community 99

> 98 nodes

## Key Concepts

- **FollowService** (74 connections) — `server/game/follow_service.py`
- **test_follow_service.py** (49 connections) — `server/tests/unit/game/test_follow_service.py`
- **asyncio** (22 connections)
- **.__init__()** (8 connections) — `server/game/follow_service.py`
- **.get_following_display()** (7 connections) — `server/game/follow_service.py`
- **._resolve_follow_target_label()** (5 connections) — `server/game/follow_service.py`
- **._followers_display_line()** (4 connections) — `server/game/follow_service.py`
- **test_accept_follow_invalid_request_id()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_accept_follow_success()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_decline_follow_success()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_already_standing()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_fails_to_stand()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_sitting_stands()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_follow_request_event_envelope_shape()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_following_npc()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_following_player_resolves_name()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_not_following()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_npc_entered_room_moves_followers()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_disconnect_cancels_pending_requests()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_move_failure_auto_unfollow()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_moves_followers()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_no_from_room_id_skips_propagation()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_already_following_rejected()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_npc_immediate()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_player_creates_pending()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- *... and 73 more nodes in this community*

## Relationships

- [Community 470](Community_470.md) (18 shared connections)
- [Community 1175](Community_1175.md) (6 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (4 shared connections)
- [Community 88](Community_88.md) (2 shared connections)
- [Community 944](Community_944.md) (2 shared connections)
- [Community 342](Community_342.md) (2 shared connections)
- [Community 85](Community_85.md) (2 shared connections)
- [Community 106](Community_106.md) (2 shared connections)
- [Community 79](Community_79.md) (2 shared connections)
- [Community 397](Community_397.md) (1 shared connections)
- [Game Event Types](Game_Event_Types.md) (1 shared connections)
- [Community 728](Community_728.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 164 (80%)
- INFERRED: 40 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*