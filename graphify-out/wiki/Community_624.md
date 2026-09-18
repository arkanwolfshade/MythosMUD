# Community 624

> 27 nodes

## Key Concepts

- **test_lifespan_event_subscriptions.py** (16 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **RoomOccupantsRefreshRequested** (14 connections) — `server/events/event_types.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **lifespan_event_subscriptions.py** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **subscribe_quest_events()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **subscribe_room_occupants_refresh()** (9 connections) — `server/app/lifespan_event_subscriptions.py`
- **assert_event_envelope()** (9 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **test_quest_log_updated_event_envelope_shape()** (6 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **asyncio** (5 connections)
- **envelope_assertions.py** (5 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **._handle_npc_entered_room()** (4 connections) — `server/npc/lifecycle_manager.py`
- **test_quest_completed_invalid_player_id_logs_warning()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_quest_completed_missing_services_skips_push()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_subscribe_room_occupants_refresh_broadcasts_on_event()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_room_occupants_refresh_no_running_loop_returns_silently()** (3 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_subscribe_room_occupants_refresh_skips_without_event_bus()** (2 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **Any** (1 connections)
- **Event subscription setup for application startup. Extracted from…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Subscribe to room events for quest triggers and progress (start on enter,…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Event requesting that room occupants be broadcast to clients. Used after NPC…** (1 connections) — `server/events/event_types.py`
- **Event fired when a quest instance is completed (rewards applied, state set to…** (1 connections) — `server/events/event_types.py`
- **Handle NPC entering a room.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Unit tests for lifespan event subscription producers.** (1 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **quest_log_updated producer emits a build_event-shaped envelope with player_id.** (1 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- *... and 2 more nodes in this community*

## Relationships

- [NPC Event Types](NPC_Event_Types.md) (5 shared connections)
- [Community 35](Community_35.md) (5 shared connections)
- [NPC Follow System](NPC_Follow_System.md) (4 shared connections)
- [Community 122](Community_122.md) (3 shared connections)
- [Community 93](Community_93.md) (3 shared connections)
- [Community 215](Community_215.md) (3 shared connections)
- [Event Bus](Event_Bus.md) (2 shared connections)
- [Community 669](Community_669.md) (2 shared connections)
- [Community 62](Community_62.md) (2 shared connections)
- [Community 222](Community_222.md) (2 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (2 shared connections)
- [Community 1420](Community_1420.md) (1 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/event_types.py`
- `server/npc/lifecycle_manager.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/realtime/envelope_assertions.py`

## Audit Trail

- EXTRACTED: 75 (89%)
- INFERRED: 9 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*