# server app lifespan event subscriptions

> 50 nodes

## Key Concepts

- **.__post_init__()** (21 connections) — `server/events/event_types.py`
- **Initialize the event with proper type.** (18 connections) — `server/events/event_types.py`
- **test_lifespan_event_subscriptions.py** (17 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **RoomOccupantsRefreshRequested** (14 connections) — `server/events/event_types.py`
- **lifespan_event_subscriptions.py** (14 connections) — `server/app/lifespan_event_subscriptions.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **subscribe_quest_events()** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **subscribe_room_occupants_refresh()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **assert_event_envelope()** (11 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **test_quest_log_updated_event_envelope_shape()** (6 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **envelope_assertions.py** (6 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **asyncio** (5 connections)
- **PlayerMortallyWoundedEvent** (4 connections) — `server/events/event_types.py`
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
- *... and 25 more nodes in this community*

## Relationships

- [server events event bus](server_events_event_bus.md) (15 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (6 shared connections)
- [moduletype](moduletype.md) (5 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (4 shared connections)
- [server events event types playerleftroom](server_events_event_types_playerleftroom.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server game quest quest service](server_game_quest_quest_service.md) (2 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (2 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (2 shared connections)
- [server realtime occupant display](server_realtime_occupant_display.md) (2 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/event_types.py`
- `server/npc/lifecycle_manager.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/realtime/envelope_assertions.py`

## Audit Trail

- EXTRACTED: 141 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*