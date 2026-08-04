# message realtime messaging

> 17 nodes

## Key Concepts

- **test_lifespan_event_subscriptions.py** (15 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **subscribe_quest_events()** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **lifespan_event_subscriptions.py** (12 connections) — `server/app/lifespan_event_subscriptions.py`
- **subscribe_room_occupants_refresh()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **test_quest_log_updated_event_envelope_shape()** (5 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_subscribe_room_occupants_refresh_broadcasts_on_event()** (3 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_room_occupants_refresh_no_running_loop_returns_silently()** (3 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_quest_completed_invalid_player_id_logs_warning()** (3 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_quest_completed_missing_services_skips_push()** (3 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_subscribe_room_occupants_refresh_skips_without_event_bus()** (2 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **Event subscription setup for application startup.  Extracted from lifespan_start** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Subscribe to room events for quest triggers and progress (start on enter, comple** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Event fired when a quest instance is completed (rewards applied, state set to co** (1 connections) — `server/events/event_types.py`
- **Unit tests for lifespan event subscription producers.** (1 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **quest_log_updated producer emits a build_event-shaped envelope with player_id.** (1 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (9 shared connections)
- [nats services service](nats_services_service.md) (5 shared connections)
- [skill game service](skill_game_service.md) (3 shared connections)
- [room look commands](room_look_commands.md) (2 shared connections)
- [command models moderation](command_models_moderation.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [quest game service](quest_game_service.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [item models rationale](item_models_rationale.md) (1 shared connections)
- [command service commands](command_service_commands.md) (1 shared connections)
- [collect inventory game](collect_inventory_game.md) (1 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/event_types.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`

## Audit Trail

- EXTRACTED: 84 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*