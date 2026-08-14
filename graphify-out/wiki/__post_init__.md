# .__post_init__

> 66 nodes

## Key Concepts

- **.__post_init__()** (21 connections) — `server/events/event_types.py`
- **RoomOccupantsRefreshRequested** (16 connections) — `server/events/event_types.py`
- **test_lifespan_event_subscriptions.py** (16 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **QuestCompleted** (12 connections) — `server/events/event_types.py`
- **subscribe_quest_events()** (12 connections) — `server/app/lifespan_event_subscriptions.py`
- **lifespan_event_subscriptions.py** (12 connections) — `server/app/lifespan_event_subscriptions.py`
- **assert_event_envelope()** (11 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **subscribe_room_occupants_refresh()** (10 connections) — `server/app/lifespan_event_subscriptions.py`
- **test_quest_log_updated_event_envelope_shape()** (6 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **envelope_assertions.py** (6 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **asyncio** (5 connections)
- **._handle_npc_entered_room()** (4 connections) — `server/npc/lifecycle_manager.py`
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
- *... and 41 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (21 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (8 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (4 shared connections)
- [QuestService](QuestService.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [test_quest_events.py](test_quest_events.py.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [test_party_service.py](test_party_service.py.md) (2 shared connections)
- [test_combat_messaging_integration.py](test_combat_messaging_integration.py.md) (2 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/event_types.py`
- `server/npc/lifecycle_manager.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/realtime/envelope_assertions.py`

## Audit Trail

- EXTRACTED: 142 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*