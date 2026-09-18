# Event Bus

> 216 nodes

## Key Concepts

- **EventBus** (161 connections) — `server/events/event_bus.py`
- **BaseEvent** (99 connections) — `server/events/event_types.py`
- **test_event_bus.py** (59 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (28 connections)
- **test_event_bus_lifecycle.py** (24 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **MockEventClass** (19 connections) — `server/tests/unit/events/test_event_bus.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **distributed_event_bus.py** (11 connections) — `server/events/distributed_event_bus.py`
- **asyncio** (11 connections)
- **test_nats_event_bridge.py** (9 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **_ExperienceEventBus** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **test_handle_event_async_async_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_queue_depth_grows_when_consumer_blocked()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_async_subscriber_error_isolation()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_inject_dispatches_to_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_multiple_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_no_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 191 more nodes in this community*

## Relationships

- [NPC Event Types](NPC_Event_Types.md) (25 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (24 shared connections)
- [Community 503](Community_503.md) (14 shared connections)
- [Community 443](Community_443.md) (13 shared connections)
- [Combat Events](Combat_Events.md) (11 shared connections)
- [Community 35](Community_35.md) (9 shared connections)
- [Community 515](Community_515.md) (9 shared connections)
- [NPC Population Control](NPC_Population_Control.md) (8 shared connections)
- [Community 926](Community_926.md) (5 shared connections)
- [NPC Follow System](NPC_Follow_System.md) (4 shared connections)
- [Combat Cleanup & Results](Combat_Cleanup_&_Results.md) (3 shared connections)
- [Community 112](Community_112.md) (3 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/events/test_event_bus_lifecycle.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 434 (78%)
- INFERRED: 123 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*