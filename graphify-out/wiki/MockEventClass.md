# MockEventClass

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

- [test_event_bus.py](test_event_bus.py.md) (8 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [Community 1843](Community_1843.md) (1 shared connections)
- [test_validate_permission_viewer_limited](test_validate_permission_viewer_limited.md) (1 shared connections)
- [test_event_bus_publish](test_event_bus_publish.md) (1 shared connections)
- [test_has_permission_superuser](test_has_permission_superuser.md) (1 shared connections)
- [test_validate_permission_superuser_all_actions](test_validate_permission_superuser_all_actions.md) (1 shared connections)
- [test_get_active_sessions_filters_expired](test_get_active_sessions_filters_expired.md) (1 shared connections)
- [test_cleanup_expired_sessions_no_expired](test_cleanup_expired_sessions_no_expired.md) (1 shared connections)
- [test_validate_permission_logs_audit](test_validate_permission_logs_audit.md) (1 shared connections)
- [test_get_username_dict_without_username](test_get_username_dict_without_username.md) (1 shared connections)
- [test_cleanup_expired_sessions](test_cleanup_expired_sessions.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 29 (50%)
- INFERRED: 29 (50%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*