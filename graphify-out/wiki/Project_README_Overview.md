# Project README Overview

> 16 nodes · cohesion 0.12

## Key Concepts

- **MockEventClass** (29 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts_multiple_types()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_subscriber_count_none()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe_not_found()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_shutdown_cleans_up_service_subscriptions()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_all_for_service_partial_cleanup()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_all_subscriber_counts() with multiple event types.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Mock event class for testing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _handle_task_result_async() with task that raises error.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe_all_for_service() only removes tracked handlers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() automatically cleans up all service subscriptions.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe() when handler not found.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_subscriber_count() returns 0 for no subscribers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_all_subscriber_counts() returns all counts.** (1 connections) — `server/tests/unit/events/test_event_bus.py`

## Relationships

- [Realtime Event Handlers](Realtime_Event_Handlers.md) (8 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Community 1843](Community_1843.md) (1 shared connections)
- [Lucidity Utc Now](Lucidity_Utc_Now.md) (1 shared connections)
- [E 2 E Scenario Template](E_2_E_Scenario_Template.md) (1 shared connections)
- [Persistence Item Repositories](Persistence_Item_Repositories.md) (1 shared connections)
- [E 2 E Scenarios Lucidity](E_2_E_Scenarios_Lucidity.md) (1 shared connections)
- [Services Service Lucidity](Services_Service_Lucidity.md) (1 shared connections)
- [Setup Dompurifytestwindow Localstorageshim](Setup_Dompurifytestwindow_Localstorageshim.md) (1 shared connections)
- [Room Toolkit Validator](Room_Toolkit_Validator.md) (1 shared connections)
- [Game Profession Service](Game_Profession_Service.md) (1 shared connections)
- [Room Services Validator](Room_Services_Validator.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 29 (50%)
- INFERRED: 29 (50%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*