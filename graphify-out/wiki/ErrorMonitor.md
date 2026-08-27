# ErrorMonitor

> 29 nodes

## Key Concepts

- **EventBusProcessingMixin** (17 connections) — `server/events/event_bus_processing.py`
- **._handle_event_async()** (8 connections) — `server/events/event_bus_processing.py`
- **BaseEvent** (8 connections)
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
- **Exception** (1 connections)
- **Execute sync subscribers sequentially with error isolation. Sync subscribers…** (1 connections) — `server/events/event_bus_processing.py`
- **Create asyncio tasks for async event subscribers and track their lifecycle.…** (1 connections) — `server/events/event_bus_processing.py`
- **Wait for all async subscriber tasks to complete and handle their results. Uses…** (1 connections) — `server/events/event_bus_processing.py`
- **Handle a single event by calling all registered subscribers with structured…** (1 connections) — `server/events/event_bus_processing.py`
- **Mixin: queue loop, subscriber dispatch, publish, and inject.** (1 connections) — `server/events/event_bus_processing.py`
- **Handle async task completion with proper exception extraction.** (1 connections) — `server/events/event_bus_processing.py`
- **Invoke one subscriber in test mode (direct call or create_task).** (1 connections) — `server/events/event_bus_processing.py`
- **Process subscribers synchronously when tests have no running EventBus loop.** (1 connections) — `server/events/event_bus_processing.py`
- **Log a processing error, falling back if Unicode encoding fails.** (1 connections) — `server/events/event_bus_processing.py`
- *... and 4 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)

## Source Files

- `server/events/event_bus_processing.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*