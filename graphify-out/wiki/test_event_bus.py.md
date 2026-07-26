# test_event_bus.py

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

- [MockEventClass](MockEventClass.md) (8 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_get_user_id_from_user_object](test_get_user_id_from_user_object.md) (1 shared connections)
- [Community 1843](Community_1843.md) (1 shared connections)
- [test_validate_permission_viewer_limited](test_validate_permission_viewer_limited.md) (1 shared connections)
- [test_event_bus_publish](test_event_bus_publish.md) (1 shared connections)
- [test_has_permission_superuser](test_has_permission_superuser.md) (1 shared connections)
- [test_validate_permission_superuser_all_actions](test_validate_permission_superuser_all_actions.md) (1 shared connections)
- [test_get_username_from_user_object](test_get_username_from_user_object.md) (1 shared connections)
- [test_get_active_sessions_filters_expired](test_get_active_sessions_filters_expired.md) (1 shared connections)
- [test_cleanup_expired_sessions_no_expired](test_cleanup_expired_sessions_no_expired.md) (1 shared connections)
- [test_validate_permission_logs_audit](test_validate_permission_logs_audit.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 77 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*