# test_lifespan_event_subscriptions.py

> 21 nodes

## Key Concepts

- **test_lifespan_event_subscriptions.py** (17 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **lifespan_event_subscriptions.py** (14 connections) — `server/app/lifespan_event_subscriptions.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **subscribe_quest_events()** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **subscribe_room_occupants_refresh()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **._init_quest_service()** (7 connections) — `server/container/bundles/game.py`
- **test_quest_log_updated_event_envelope_shape()** (6 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **asyncio** (5 connections)
- **test_quest_completed_invalid_player_id_logs_warning()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_quest_completed_missing_services_skips_push()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_subscribe_room_occupants_refresh_broadcasts_on_event()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_room_occupants_refresh_no_running_loop_returns_silently()** (3 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_subscribe_room_occupants_refresh_skips_without_event_bus()** (2 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **Event subscription setup for application startup. Extracted from…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Subscribe to room events for quest triggers and progress (start on enter,…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Event fired when a quest instance is completed (rewards applied, state set to…** (1 connections) — `server/events/event_types.py`
- **Get the event bus from connection manager.** (1 connections) — `server/realtime/connection_manager.py`
- **Unit tests for lifespan event subscription producers.** (1 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **quest_log_updated producer emits a build_event-shaped envelope with player_id.** (1 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`

## Relationships

- [NPCDefinition](NPCDefinition.md) (8 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (4 shared connections)
- [QuestService](QuestService.md) (3 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (3 shared connections)
- [assert_event_envelope](assert_event_envelope.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [quest_service.py](quest_service.py.md) (1 shared connections)
- [.__post_init__](__post_init__.md) (1 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/container/bundles/game.py`
- `server/events/event_types.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`

## Audit Trail

- EXTRACTED: 69 (81%)
- INFERRED: 16 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*