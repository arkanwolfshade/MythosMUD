# event bus events

> 23 nodes

## Key Concepts

- **test_event_bus.py** (57 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_init()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts_empty()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown_idempotent()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_invalid_event_type()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_invalid_event()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_ensure_processing_started()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_same_events_integration()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_active_task_details_and_lifecycle_metrics()** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_set_main_loop_and_ensure_processing()** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_signal_shutdown_and_cancel_helpers()** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_active_task_details_includes_exception()** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_ensure_async_processing_no_loop_logs()** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Unit tests for event bus.  Tests the EventBus class.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus initialization.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() stops processing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_all_subscriber_counts() with no subscribers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() is idempotent.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test unsubscribe() raises error for invalid event type.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test publish() raises error for invalid event.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _ensure_processing_started() calls _ensure_async_processing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Integration test: Multiple services subscribing to same events and cleanup.** (1 connections) — `server/tests/unit/events/test_event_bus.py`

## Relationships

- [room conftest toolkit](room_conftest_toolkit.md) (11 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [services ascii map](services_ascii_map.md) (2 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (1 shared connections)
- [tsconfig build DOM](tsconfig_build_DOM.md) (1 shared connections)
- [realtime player presence](realtime_player_presence.md) (1 shared connections)
- [liability types call](liability_types_call.md) (1 shared connections)
- [tsconfig app DOM](tsconfig_app_DOM.md) (1 shared connections)
- [combat npc services](combat_npc_services.md) (1 shared connections)
- [logging utilities structured](logging_utilities_structured.md) (1 shared connections)
- [holiday services service](holiday_services_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 87 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*