# Health Check Models

> 66 nodes

## Key Concepts

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
- **._on_npc_entered_room()** (5 connections) — `server/game/follow_service.py`
- *... and 41 more nodes in this community*

## Relationships

- [Commands Look Item](Commands_Look_Item.md) (15 shared connections)
- [Client Event Store](Client_Event_Store.md) (11 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (6 shared connections)
- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (4 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (4 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (3 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (3 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (3 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (3 shared connections)
- [Player Mute Persistence](Player_Mute_Persistence.md) (2 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/tests/integration/test_follow_flow.py`

## Audit Trail

- EXTRACTED: 284 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*