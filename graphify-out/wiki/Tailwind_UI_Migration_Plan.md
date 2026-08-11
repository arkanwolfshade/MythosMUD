# Tailwind UI Migration Plan

> 22 nodes

## Key Concepts

- **test_event_bus.py** (45 connections) — `server/tests/unit/events/test_event_bus.py`
- **event_bus()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_init()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown_idempotent()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_subscribe_invalid_event_type()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_invalid_event()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_stop_processing_not_running()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_ensure_processing_started()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_all_for_service_nonexistent()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_same_events_integration()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **Unit tests for event bus.  Tests the EventBus class.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Create an EventBus instance.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus initialization.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() stops processing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() is idempotent.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test subscribe() raises error for invalid event type.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test publish() raises error for invalid event.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _stop_processing() when not running.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _ensure_processing_started() calls _ensure_async_processing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe_all_for_service() with nonexistent service_id.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Integration test: Multiple services subscribing to same events and cleanup.** (1 connections) — `server/tests/unit/events/test_event_bus.py`

## Relationships

- [Services Rescue Service](Services_Rescue_Service.md) (8 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (5 shared connections)
- [CleanupContext](CleanupContext.md) (1 shared connections)
- [Game Quest Service](Game_Quest_Service.md) (1 shared connections)
- [.prune_stale_players](prune_stale_players.md) (1 shared connections)
- [Archive Combat Health](Archive_Combat_Health.md) (1 shared connections)
- [Nats Subject Patterns](Nats_Subject_Patterns_2.md) (1 shared connections)
- [.check_and_cleanup](check_and_cleanup.md) (1 shared connections)
- [test_setup_player_and_room_no_player](test_setup_player_and_room_no_player.md) (1 shared connections)
- [Services Player Respawn](Services_Player_Respawn.md) (1 shared connections)
- [Persistence Async Migration](Persistence_Async_Migration.md) (1 shared connections)
- [E 2 E Remaining Work](E_2_E_Remaining_Work.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 77 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*