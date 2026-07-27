# Events Event Bus

> 19 nodes · cohesion 0.11

## Key Concepts

- **MockEventClass** (14 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_inject_dispatches_to_subscribers()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_multiple_subscribers()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_no_subscribers()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_async_subscriber_error()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_no_subscribers()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _handle_event_async() handles sync subscriber errors.** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.publish() queues or processes event.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.publish() with no subscribers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.inject() delivers event to subscribers (used by distributed bridge** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.publish() with multiple subscribers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Mock event class for testing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _handle_event_async() when no subscribers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _handle_task_result_async() with successful task.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _handle_task_result_async() with task that raises error.** (1 connections) — `server/tests/unit/events/test_event_bus.py`

## Relationships

- [[Events Event Bus]] (10 shared connections)
- [[Distributed Event Bus]] (2 shared connections)
- [[Combat Service Bundle]] (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 49 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
