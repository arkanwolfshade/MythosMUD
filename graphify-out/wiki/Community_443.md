# Community 443

> 40 nodes

## Key Concepts

- **EventBusProcessingMixin** (18 connections) — `server/events/event_bus_processing.py`
- **EventBusMixinBase** (10 connections) — `server/events/event_bus_base.py`
- **event_bus_processing.py** (9 connections) — `server/events/event_bus_processing.py`
- **._handle_event_async()** (8 connections) — `server/events/event_bus_processing.py`
- **event_bus_base.py** (6 connections) — `server/events/event_bus_base.py`
- **._create_async_subscriber_tasks()** (5 connections) — `server/events/event_bus_processing.py`
- **._publish_in_test_mode()** (5 connections) — `server/events/event_bus_processing.py`
- **._invoke_test_mode_subscriber()** (4 connections) — `server/events/event_bus_processing.py`
- **._log_processing_failure()** (4 connections) — `server/events/event_bus_processing.py`
- **._process_events_async()** (4 connections) — `server/events/event_bus_processing.py`
- **._process_sync_subscribers()** (4 connections) — `server/events/event_bus_processing.py`
- **.publish()** (4 connections) — `server/events/event_bus_processing.py`
- **._separate_subscribers()** (4 connections) — `server/events/event_bus_processing.py`
- **._wait_for_async_subscribers()** (4 connections) — `server/events/event_bus_processing.py`
- **._handle_task_result_async()** (3 connections) — `server/events/event_bus_processing.py`
- **.inject()** (3 connections) — `server/events/event_bus_processing.py`
- **Task** (3 connections)
- **._ensure_async_processing()** (2 connections) — `server/events/event_bus_base.py`
- **._process_events_async()** (2 connections) — `server/events/event_bus_base.py`
- **.unsubscribe_all_for_service()** (2 connections) — `server/events/event_bus_base.py`
- **Exception** (1 connections)
- **Attribute stubs for EventBus mixins (mypy attr-defined). Mirrors…** (1 connections) — `server/events/event_bus_base.py`
- **Attrs/methods provided by EventBus when mixed in.** (1 connections) — `server/events/event_bus_base.py`
- **Start the async consumer. Real impl is EventBusLifecycleMixin.** (1 connections) — `server/events/event_bus_base.py`
- **Drain the event queue. Real impl is EventBusProcessingMixin.** (1 connections) — `server/events/event_bus_base.py`
- *... and 15 more nodes in this community*

## Relationships

- [Event Bus](Event_Bus.md) (13 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (6 shared connections)
- [NPC Event Types](NPC_Event_Types.md) (2 shared connections)
- [Community 561](Community_561.md) (1 shared connections)

## Source Files

- `server/events/event_bus_base.py`
- `server/events/event_bus_processing.py`

## Audit Trail

- EXTRACTED: 71 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*