# Player Respawn Handlers

> 28 nodes

## Key Concepts

- **FollowService** (36 connections) — `server/game/follow_service.py`
- **UUID** (14 connections)
- **_str_id()** (13 connections) — `server/game/follow_service.py`
- **.request_follow()** (9 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/follow_service.py`
- **Any** (7 connections)
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (5 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- **.on_player_disconnect()** (4 connections) — `server/game/follow_service.py`
- **Normalize ID to string for dict keys.** (1 connections) — `server/game/follow_service.py`
- **In-memory follow state and movement propagation.      Subscribes to PlayerEntere** (1 connections) — `server/game/follow_service.py`
- **Remove expired pending requests and notify requestors.** (1 connections) — `server/game/follow_service.py`
- **Send a command_response-style message to a single player.** (1 connections) — `server/game/follow_service.py`
- **Request to follow a player (pending acceptance) or start following an NPC immedi** (1 connections) — `server/game/follow_service.py`
- **Send follow_request event to the target player only.** (1 connections) — `server/game/follow_service.py`
- **Accept a follow request. Target is the player who accepted (the followee).** (1 connections) — `server/game/follow_service.py`
- **Decline a follow request.** (1 connections) — `server/game/follow_service.py`
- **Return list of follower player IDs (for movement propagation).** (1 connections) — `server/game/follow_service.py`
- **Return (target_id, target_type) if following someone, else None.** (1 connections) — `server/game/follow_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [Architecture Review Plan](Architecture_Review_Plan.md) (20 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (2 shared connections)
- [Room Map Viewer UI](Room_Map_Viewer_UI.md) (1 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (1 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (1 shared connections)
- [Player Mute Persistence](Player_Mute_Persistence.md) (1 shared connections)
- [test_setup_connection_metadata_no_session_token](test_setup_connection_metadata_no_session_token.md) (1 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (1 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`

## Audit Trail

- EXTRACTED: 144 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*