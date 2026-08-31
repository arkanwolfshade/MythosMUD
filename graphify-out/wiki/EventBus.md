# EventBus

> 195 nodes

## Key Concepts

- **EventBus** (210 connections) — `server/events/event_bus.py`
- **BaseEvent** (96 connections) — `server/events/event_types.py`
- **test_event_bus.py** (60 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (28 connections)
- **test_event_bus_lifecycle.py** (25 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **MockEventClass** (19 connections) — `server/tests/unit/events/test_event_bus.py`
- **distributed_event_bus.py** (12 connections) — `server/events/distributed_event_bus.py`
- **asyncio** (11 connections)
- **test_handle_event_async_async_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_queue_depth_grows_when_consumer_blocked()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **._publish_in_test_mode()** (5 connections) — `server/events/event_bus_processing.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_async_subscriber_error_isolation()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_inject_dispatches_to_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_multiple_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_no_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_no_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_same_events_integration()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_service_shutdown_removes_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_shutdown_cleans_up_service_subscriptions()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 170 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (46 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (34 shared connections)
- [NPCBase](NPCBase.md) (15 shared connections)
- [PlayerXPAwardEvent](PlayerXPAwardEvent.md) (13 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (11 shared connections)
- [PartyService](PartyService.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [DistributedEventBus](DistributedEventBus.md) (7 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (6 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (4 shared connections)
- [._handle_event_async](_handle_event_async.md) (4 shared connections)
- [test_event_reaction_speech.py](test_event_reaction_speech.py.md) (4 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_bus_processing.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/events/test_event_bus_lifecycle.py`

## Audit Trail

- EXTRACTED: 436 (78%)
- INFERRED: 123 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*