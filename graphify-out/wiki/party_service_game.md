# party service game

> 242 nodes

## Key Concepts

- **PlayerEnteredRoom** (85 connections) — `server/events/event_types.py`
- **test_follow_service.py** (47 connections) — `server/tests/unit/game/test_follow_service.py`
- **FollowService** (39 connections) — `server/game/follow_service.py`
- **test_player_event_handlers_room.py** (37 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **follow_service.py** (25 connections) — `server/game/follow_service.py`
- **_str_id()** (15 connections) — `server/game/follow_service.py`
- **UUID** (14 connections)
- **test_follow_flow.py** (13 connections) — `server/tests/integration/test_follow_flow.py`
- **.__init__()** (10 connections) — `server/game/follow_service.py`
- **.request_follow()** (10 connections) — `server/game/follow_service.py`
- **._send_result_to_player()** (9 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (9 connections) — `server/game/follow_service.py`
- **._handle_player_follower_move()** (9 connections) — `server/game/follow_service.py`
- **._handle_npc_follower_move()** (9 connections) — `server/game/follow_service.py`
- **Any** (8 connections)
- **.unfollow()** (8 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (7 connections) — `server/game/follow_service.py`
- **._schedule_coro()** (7 connections) — `server/game/follow_service.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **.get_followers()** (6 connections) — `server/game/follow_service.py`
- **.get_following_display()** (6 connections) — `server/game/follow_service.py`
- **._ensure_follower_standing()** (6 connections) — `server/game/follow_service.py`
- **._on_player_entered_room()** (6 connections) — `server/game/follow_service.py`
- *... and 217 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (49 shared connections)
- [profession models rationale](profession_models_rationale.md) (21 shared connections)
- [player room event](player_room_event.md) (9 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (6 shared connections)
- [lucidity event services](lucidity_event_services.md) (4 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (4 shared connections)
- [message handler factory](message_handler_factory.md) (3 shared connections)
- [container events rationale](container_events_rationale.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [position player service](position_player_service.md) (3 shared connections)
- [services ascii map](services_ascii_map.md) (3 shared connections)
- [message nats handler](message_nats_handler.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/npc/population_control.py`
- `server/realtime/event_handler.py`
- `server/realtime/integration/room_event_handler.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_room.py`

## Audit Trail

- EXTRACTED: 737 (95%)
- INFERRED: 35 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*