# NPC Combat Integration

> 52 nodes · cohesion 0.04

## Key Concepts

- **test_follow_service.py** (38 connections) — `server/tests/unit/game/test_follow_service.py`
- **follow_service()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_npc_entered_room_moves_followers()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_move_failure_auto_unfollow()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_no_from_room_id_skips_propagation()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **connection_manager()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **event_bus()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **movement_service()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_accept_follow_invalid_request_id()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_decline_follow_success()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_already_standing()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_fails_to_stand()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_followers_empty()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_followers_multiple()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_following_npc()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_not_following()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_none()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_disconnect_cancels_pending_requests()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_disconnect_clears_follow_state()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_already_following_rejected()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_npc_immediate()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_player_creates_pending()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_player_muted_auto_decline()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_unfollow_was_following()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_unfollow_was_not_following()** (2 connections) — `server/tests/unit/game/test_follow_service.py`
- *... and 27 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (7 shared connections)
- [Map Editing Hooks](Map_Editing_Hooks.md) (2 shared connections)
- [Cursor Agents Readme](Cursor_Agents_Readme.md) (1 shared connections)
- [Archive Planning Cursor](Archive_Planning_Cursor.md) (1 shared connections)
- [Cursor Skills Bolder](Cursor_Skills_Bolder.md) (1 shared connections)
- [Archive Planning Chat](Archive_Planning_Chat.md) (1 shared connections)
- [Cursor Skills Animate](Cursor_Skills_Animate.md) (1 shared connections)
- [Archive Fixture Optimization](Archive_Fixture_Optimization.md) (1 shared connections)
- [Components Map Performance](Components_Map_Performance.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 118 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*