# .__post_init__

> 62 nodes

## Key Concepts

- **.__post_init__()** (21 connections) — `server/events/event_types.py`
- **test_lifespan_event_subscriptions.py** (17 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **RoomOccupantsRefreshRequested** (14 connections) — `server/events/event_types.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **subscribe_quest_events()** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **subscribe_room_occupants_refresh()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **assert_event_envelope()** (9 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **test_quest_log_updated_event_envelope_shape()** (6 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **asyncio** (5 connections)
- **envelope_assertions.py** (5 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **test_quest_completed_invalid_player_id_logs_warning()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_quest_completed_missing_services_skips_push()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_subscribe_room_occupants_refresh_broadcasts_on_event()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- *... and 37 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (17 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (8 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (4 shared connections)
- [QuestService](QuestService.md) (3 shared connections)
- [FollowService](FollowService.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_party_service.py](test_party_service.py.md) (2 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (1 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/event_types.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/realtime/envelope_assertions.py`

## Audit Trail

- EXTRACTED: 126 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*