# Test Lifespan Event Subscriptions

> 33 nodes

## Key Concepts

- **test_lifespan_event_subscriptions.py** (17 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **RoomOccupantsRefreshRequested** (14 connections) — `server/events/event_types.py`
- **.event_bus()** (14 connections) — `server/realtime/connection_manager.py`
- **lifespan_event_subscriptions.py** (14 connections) — `server/app/lifespan_event_subscriptions.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **subscribe_quest_events()** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **subscribe_room_occupants_refresh()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **._init_quest_service()** (7 connections) — `server/container/bundles/game.py`
- **assert_event_envelope()** (7 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **test_quest_log_updated_event_envelope_shape()** (6 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **asyncio** (5 connections)
- **envelope_assertions.py** (5 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **._handle_npc_entered_room()** (4 connections) — `server/npc/lifecycle_manager.py`
- **test_quest_completed_invalid_player_id_logs_warning()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_quest_completed_missing_services_skips_push()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_subscribe_room_occupants_refresh_broadcasts_on_event()** (4 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **._get_event_bus()** (3 connections) — `server/realtime/connection_manager.py`
- **test_room_occupants_refresh_no_running_loop_returns_silently()** (3 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_subscribe_room_occupants_refresh_skips_without_event_bus()** (2 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **Get the event bus from connection manager.** (2 connections) — `server/realtime/connection_manager.py`
- **Any** (1 connections)
- **Event subscription setup for application startup. Extracted from…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- **Subscribe to room events for quest triggers and progress (start on enter,…** (1 connections) — `server/app/lifespan_event_subscriptions.py`
- *... and 8 more nodes in this community*

## Relationships

- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (7 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (7 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (4 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (4 shared connections)
- [Quest Service](Quest_Service.md) (3 shared connections)
- [Test Quest Events](Test_Quest_Events.md) (3 shared connections)
- [Test Party Service](Test_Party_Service.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Event Types](Event_Types.md) (2 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (2 shared connections)
- [Test Envelope](Test_Envelope.md) (2 shared connections)
- [Test Websocket Room Updates](Test_Websocket_Room_Updates.md) (2 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/container/bundles/game.py`
- `server/events/event_types.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/npc_base.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/realtime/envelope_assertions.py`

## Audit Trail

- EXTRACTED: 95 (83%)
- INFERRED: 19 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*