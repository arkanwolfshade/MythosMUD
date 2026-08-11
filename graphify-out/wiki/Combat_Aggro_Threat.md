# Combat Aggro Threat

> 140 nodes

## Key Concepts

- **NPCEnteredRoom** (51 connections) — `server/events/event_types.py`
- **test_follow_service.py** (38 connections) — `server/tests/unit/game/test_follow_service.py`
- **FollowService** (36 connections) — `server/game/follow_service.py`
- **follow_service.py** (24 connections) — `server/game/follow_service.py`
- **UUID** (14 connections)
- **_str_id()** (13 connections) — `server/game/follow_service.py`
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
- *... and 115 more nodes in this community*

## Relationships

- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (21 shared connections)
- [Client Event Store](Client_Event_Store.md) (11 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (7 shared connections)
- [Archive Advanced Chat](Archive_Advanced_Chat.md) (6 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (5 shared connections)
- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (4 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (4 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (4 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (3 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (3 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 465 (94%)
- INFERRED: 28 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*