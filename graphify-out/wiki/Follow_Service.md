# Follow Service

> 75 nodes

## Key Concepts

- **follow_service.py** (25 connections) — `server/game/follow_service.py`
- **FollowActionResult** (15 connections) — `server/game/follow_types.py`
- **str_id()** (15 connections) — `server/game/follow_types.py`
- **FollowPersistence** (12 connections) — `server/game/follow_types.py`
- **follow_types.py** (12 connections) — `server/game/follow_types.py`
- **FollowStatePayload** (11 connections) — `server/game/follow_types.py`
- **.request_follow()** (10 connections) — `server/game/follow_service.py`
- **UUID** (9 connections)
- **FollowPlayerView** (8 connections) — `server/game/follow_types.py`
- **.get_following_display()** (8 connections) — `server/game/follow_service.py`
- **is_npc_follow_value()** (8 connections) — `server/game/follow_types.py`
- **PendingFollowRequest** (7 connections) — `server/game/follow_types.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **.__init__()** (7 connections) — `server/game/follow_service.py`
- **._create_pending_follow_request()** (6 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (6 connections) — `server/game/follow_service.py`
- **._resolve_follow_target_label()** (6 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (6 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (6 connections) — `server/game/follow_service.py`
- **.unfollow()** (6 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- **._schedule_coro()** (5 connections) — `server/game/follow_service.py`
- **._start_following_npc()** (5 connections) — `server/game/follow_service.py`
- *... and 50 more nodes in this community*

## Relationships

- [Test Follow Service](Test_Follow_Service.md) (33 shared connections)
- [Follow Movement](Follow_Movement.md) (13 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (4 shared connections)
- [Test Player Position Service](Test_Player_Position_Service.md) (3 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (3 shared connections)
- [Test Player Event Handlers Room](Test_Player_Event_Handlers_Room.md) (1 shared connections)
- [Connection Manager Api](Connection_Manager_Api.md) (1 shared connections)
- [Test Movement Service](Test_Movement_Service.md) (1 shared connections)
- [Test Follow Flow](Test_Follow_Flow.md) (1 shared connections)

## Source Files

- `server/game/follow_movement.py`
- `server/game/follow_service.py`
- `server/game/follow_types.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 163 (93%)
- INFERRED: 13 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*