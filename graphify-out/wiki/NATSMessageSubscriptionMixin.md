# NATSMessageSubscriptionMixin

> 72 nodes · cohesion 0.04

## Key Concepts

- **EventBusLifecycleMixin** (18 connections) — `server/events/event_bus_lifecycle.py`
- **EventBusProcessingMixin** (18 connections) — `server/events/event_bus_processing.py`
- **EventBusMixinBase** (10 connections) — `server/events/event_bus_base.py`
- **event_bus_processing.py** (9 connections) — `server/events/event_bus_processing.py`
- **._handle_event_async()** (8 connections) — `server/events/event_bus_processing.py`
- **event_bus_lifecycle.py** (7 connections) — `server/events/event_bus_lifecycle.py`
- **._cancel_task_quietly()** (7 connections) — `server/events/event_bus_lifecycle.py`
- **._stop_processing()** (7 connections) — `server/events/event_bus_lifecycle.py`
- **event_bus_base.py** (6 connections) — `server/events/event_bus_base.py`
- **.shutdown()** (6 connections) — `server/events/event_bus_lifecycle.py`
- **._abandon_pending_tasks()** (5 connections) — `server/events/event_bus_lifecycle.py`
- **._cancel_and_wait_for_active_tasks()** (5 connections) — `server/events/event_bus_lifecycle.py`
- **._create_async_subscriber_tasks()** (5 connections) — `server/events/event_bus_processing.py`
- **.publish()** (5 connections) — `server/events/event_bus_processing.py`
- **._publish_in_test_mode()** (5 connections) — `server/events/event_bus_processing.py`
- **._cancel_active_tasks_best_effort()** (4 connections) — `server/events/event_bus_lifecycle.py`
- **._warn_shutdown_error()** (4 connections) — `server/events/event_bus_lifecycle.py`
- **.inject()** (4 connections) — `server/events/event_bus_processing.py`
- **._invoke_test_mode_subscriber()** (4 connections) — `server/events/event_bus_processing.py`
- **._log_processing_failure()** (4 connections) — `server/events/event_bus_processing.py`
- **._process_events_async()** (4 connections) — `server/events/event_bus_processing.py`
- **._process_sync_subscribers()** (4 connections) — `server/events/event_bus_processing.py`
- **._separate_subscribers()** (4 connections) — `server/events/event_bus_processing.py`
- **._wait_for_async_subscribers()** (4 connections) — `server/events/event_bus_processing.py`
- **._cancel_processing_task()** (3 connections) — `server/events/event_bus_lifecycle.py`
- *... and 47 more nodes in this community*

## Relationships

- [get_username_from_user](get_username_from_user.md) (14 shared connections)
- [Room](Room.md) (4 shared connections)
- [CombatInstance](CombatInstance.md) (4 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)

## Source Files

- `server/events/event_bus_base.py`
- `server/events/event_bus_lifecycle.py`
- `server/events/event_bus_processing.py`

## Audit Trail

- EXTRACTED: 121 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*