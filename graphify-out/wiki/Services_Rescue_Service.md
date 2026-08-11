# Services Rescue Service

> 16 nodes

## Key Concepts

- **MockEventClass** (29 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe_not_found()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_subscriber_count_none()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts_multiple_types()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_all_for_service_partial_cleanup()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_shutdown_cleans_up_service_subscriptions()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **Mock event class for testing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe() when handler not found.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_subscriber_count() returns 0 for no subscribers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_all_subscriber_counts() returns all counts.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_all_subscriber_counts() with multiple event types.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _handle_task_result_async() with task that raises error.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe_all_for_service() only removes tracked handlers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() automatically cleans up all service subscriptions.** (1 connections) — `server/tests/unit/events/test_event_bus.py`

## Relationships

- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (8 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Game Quest Service](Game_Quest_Service.md) (1 shared connections)
- [.prune_stale_players](prune_stale_players.md) (1 shared connections)
- [Archive Combat Health](Archive_Combat_Health.md) (1 shared connections)
- [Nats Subject Patterns](Nats_Subject_Patterns_2.md) (1 shared connections)
- [.check_and_cleanup](check_and_cleanup.md) (1 shared connections)
- [Services Player Respawn](Services_Player_Respawn.md) (1 shared connections)
- [Persistence Async Migration](Persistence_Async_Migration.md) (1 shared connections)
- [E 2 E Remaining Work](E_2_E_Remaining_Work.md) (1 shared connections)
- [.get_strategy](get_strategy.md) (1 shared connections)
- [E 2 E Whisper System](E_2_E_Whisper_System.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 29 (50%)
- INFERRED: 29 (50%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*