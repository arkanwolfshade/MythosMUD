# test_lifespan_event_subscriptions.py

> 35 nodes

## Key Concepts

- **test_lifespan_event_subscriptions.py** (17 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **.event_bus()** (14 connections) — `server/realtime/connection_manager.py`
- **lifespan_event_subscriptions.py** (14 connections) — `server/app/lifespan_event_subscriptions.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **subscribe_quest_events()** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **subscribe_room_occupants_refresh()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **assert_event_envelope()** (9 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **test_quest_log_updated_event_envelope_shape()** (6 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **._move_with_integration()** (5 connections) — `server/npc/npc_base.py`
- **asyncio** (5 connections)
- **envelope_assertions.py** (5 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **test_quest_completed_invalid_player_id_logs_warning()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_quest_completed_missing_services_skips_push()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_subscribe_room_occupants_refresh_broadcasts_on_event()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **._is_npc_in_combat()** (3 connections) — `server/npc/npc_base.py`
- **._move_simple()** (3 connections) — `server/npc/npc_base.py`
- **test_room_occupants_refresh_no_running_loop_returns_silently()** (3 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_subscribe_room_occupants_refresh_skips_without_event_bus()** (2 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **Any** (1 connections)
- **Event subscription setup for application startup. Extracted from…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Subscribe to room events for quest triggers and progress (start on enter,…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Event fired when a quest instance is completed (rewards applied, state set to…** (1 connections) — `server/events/event_types.py`
- *... and 10 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (9 shared connections)
- [event_types.py](event_types.py.md) (8 shared connections)
- [EventBus](EventBus.md) (7 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [FollowService](FollowService.md) (3 shared connections)
- [QuestService](QuestService.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (2 shared connections)
- [test_party_service.py](test_party_service.py.md) (2 shared connections)
- [quest_service.py](quest_service.py.md) (1 shared connections)
- [._bind_event_type](_bind_event_type.md) (1 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/event_types.py`
- `server/npc/npc_base.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/realtime/envelope_assertions.py`

## Audit Trail

- EXTRACTED: 89 (83%)
- INFERRED: 18 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*