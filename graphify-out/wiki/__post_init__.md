# .__post_init__

> 61 nodes

## Key Concepts

- **.__post_init__()** (21 connections) — `server/events/event_types.py`
- **test_lifespan_event_subscriptions.py** (17 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **RoomOccupantsRefreshRequested** (14 connections) — `server/events/event_types.py`
- **lifespan_event_subscriptions.py** (14 connections) — `server/app/lifespan_event_subscriptions.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **subscribe_quest_events()** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **subscribe_room_occupants_refresh()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **test_quest_log_updated_event_envelope_shape()** (6 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
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
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- *... and 36 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (27 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (6 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [QuestService](QuestService.md) (3 shared connections)
- [NPCDied](NPCDied.md) (3 shared connections)
- [assert_event_envelope](assert_event_envelope.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [combat_integration.py](combat_integration.py.md) (1 shared connections)
- [party_service.py](party_service.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/event_types.py`
- `server/npc/lifecycle_manager.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`

## Audit Trail

- EXTRACTED: 126 (92%)
- INFERRED: 11 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*