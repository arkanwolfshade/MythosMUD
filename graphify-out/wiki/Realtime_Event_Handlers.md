# Realtime Event Handlers

> 22 nodes · cohesion 0.09

## Key Concepts

- **test_event_bus.py** (45 connections) — `server/tests/unit/events/test_event_bus.py`
- **event_bus()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_ensure_processing_started()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_init()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown_idempotent()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_same_events_integration()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_invalid_event()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_stop_processing_not_running()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_subscribe_invalid_event_type()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_all_for_service_nonexistent()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **Unit tests for event bus.  Tests the EventBus class.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() stops processing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() is idempotent.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test subscribe() raises error for invalid event type.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test publish() raises error for invalid event.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _stop_processing() when not running.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Create an EventBus instance.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _ensure_processing_started() calls _ensure_async_processing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus initialization.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe_all_for_service() with nonexistent service_id.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Integration test: Multiple services subscribing to same events and cleanup.** (1 connections) — `server/tests/unit/events/test_event_bus.py`

## Relationships

- [Project README Overview](Project_README_Overview.md) (8 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [Components Map Roommapeditor](Components_Map_Roommapeditor.md) (1 shared connections)
- [Community 1843](Community_1843.md) (1 shared connections)
- [Lucidity Utc Now](Lucidity_Utc_Now.md) (1 shared connections)
- [E 2 E Scenario Template](E_2_E_Scenario_Template.md) (1 shared connections)
- [Persistence Item Repositories](Persistence_Item_Repositories.md) (1 shared connections)
- [E 2 E Scenarios Lucidity](E_2_E_Scenarios_Lucidity.md) (1 shared connections)
- [E 2 E Whisper System](E_2_E_Whisper_System.md) (1 shared connections)
- [Services Service Lucidity](Services_Service_Lucidity.md) (1 shared connections)
- [Setup Dompurifytestwindow Localstorageshim](Setup_Dompurifytestwindow_Localstorageshim.md) (1 shared connections)
- [Room Toolkit Validator](Room_Toolkit_Validator.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 77 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*