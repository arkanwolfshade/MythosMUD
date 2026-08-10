# NPC Utility Functions

> 132 nodes

## Key Concepts

- **test_follow_service.py** (38 connections) — `server/tests/unit/game/test_follow_service.py`
- **FollowService** (36 connections) — `server/game/follow_service.py`
- **follow_service.py** (24 connections) — `server/game/follow_service.py`
- **UUID** (14 connections)
- **_str_id()** (13 connections) — `server/game/follow_service.py`
- **test_follow_flow.py** (13 connections) — `server/tests/integration/test_follow_flow.py`
- **.__init__()** (10 connections) — `server/game/follow_service.py`
- **.request_follow()** (9 connections) — `server/game/follow_service.py`
- **._handle_player_follower_move()** (9 connections) — `server/game/follow_service.py`
- **._handle_npc_follower_move()** (9 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (8 connections) — `server/game/follow_service.py`
- **.unfollow()** (8 connections) — `server/game/follow_service.py`
- **Any** (7 connections)
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **._ensure_follower_standing()** (6 connections) — `server/game/follow_service.py`
- **._on_player_entered_room()** (6 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (5 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- *... and 107 more nodes in this community*

## Relationships

- [Level and XP Curve](Level_and_XP_Curve.md) (17 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (11 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (5 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (4 shared connections)
- [Combat Client Crash Report](Combat_Client_Crash_Report.md) (3 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (3 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (3 shared connections)
- [Player Mute Persistence](Player_Mute_Persistence.md) (2 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (1 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 424 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*