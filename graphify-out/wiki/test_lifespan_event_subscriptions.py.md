# test_lifespan_event_subscriptions.py

> 21 nodes

## Key Concepts

- **test_lifespan_event_subscriptions.py** (16 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **subscribe_quest_events()** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **subscribe_room_occupants_refresh()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **assert_event_envelope()** (11 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **test_quest_log_updated_event_envelope_shape()** (6 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **envelope_assertions.py** (6 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **asyncio** (5 connections)
- **test_quest_completed_invalid_player_id_logs_warning()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_quest_completed_missing_services_skips_push()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_subscribe_room_occupants_refresh_broadcasts_on_event()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_room_occupants_refresh_no_running_loop_returns_silently()** (3 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_subscribe_room_occupants_refresh_skips_without_event_bus()** (2 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **Any** (1 connections)
- **Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Subscribe to room events for quest triggers and progress (start on enter,…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Event fired when a quest instance is completed (rewards applied, state set to…** (1 connections) — `server/events/event_types.py`
- **Unit tests for lifespan event subscription producers.** (1 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **quest_log_updated producer emits a build_event-shaped envelope with player_id.** (1 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **Shared contract assertions for realtime event envelopes produced via…** (1 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **Assert a fan-out producer event matches the build_event envelope shape.** (1 connections) — `server/tests/unit/realtime/envelope_assertions.py`

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [QuestService](QuestService.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [test_party_service.py](test_party_service.py.md) (2 shared connections)
- [test_combat_messaging_integration.py](test_combat_messaging_integration.py.md) (2 shared connections)
- [MythosTimeEventConsumer](MythosTimeEventConsumer.md) (1 shared connections)
- [NPCDied](NPCDied.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [asyncio](asyncio.md) (1 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/event_types.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/realtime/envelope_assertions.py`

## Audit Trail

- EXTRACTED: 61 (87%)
- INFERRED: 9 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*