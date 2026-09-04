# Test Follow Service

> 82 nodes

## Key Concepts

- **FollowService** (70 connections) — `server/game/follow_service.py`
- **test_follow_service.py** (50 connections) — `server/tests/unit/game/test_follow_service.py`
- **asyncio** (20 connections)
- **follow_service()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_npc_entered_room_moves_followers()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_move_failure_auto_unfollow()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_moves_followers()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_entered_room_no_from_room_id_skips_propagation()** (5 connections) — `server/tests/unit/game/test_follow_service.py`
- **fixture** (5 connections)
- **test_accept_follow_invalid_request_id()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_accept_follow_success()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_decline_follow_success()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_already_standing()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_fails_to_stand()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_ensure_follower_standing_sitting_stands()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_expire_pending_requests_removes_stale()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_follow_request_event_envelope_shape()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_following_npc()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_following_player_resolves_name()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_get_following_display_not_following()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_on_player_disconnect_cancels_pending_requests()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_already_following_rejected()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_npc_immediate()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_player_creates_pending()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_request_follow_player_muted_auto_decline()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- *... and 57 more nodes in this community*

## Relationships

- [Follow Service](Follow_Service.md) (33 shared connections)
- [Test Player Event Handlers Room](Test_Player_Event_Handlers_Room.md) (5 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (5 shared connections)
- [Test Player Position Service](Test_Player_Position_Service.md) (2 shared connections)
- [Test Follow Flow](Test_Follow_Flow.md) (2 shared connections)
- [Test Logout Commands](Test_Logout_Commands.md) (2 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)
- [Test Quest Events](Test_Quest_Events.md) (1 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (1 shared connections)
- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (1 shared connections)
- [Test Websocket Helpers](Test_Websocket_Helpers.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 145 (76%)
- INFERRED: 46 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*