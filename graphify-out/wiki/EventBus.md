# EventBus

> 217 nodes

## Key Concepts

- **EventBus** (210 connections) — `server/events/event_bus.py`
- **BaseEvent** (96 connections) — `server/events/event_types.py`
- **test_event_bus.py** (60 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (28 connections)
- **test_event_bus_lifecycle.py** (25 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **MockEventClass** (19 connections) — `server/tests/unit/events/test_event_bus.py`
- **EventBusProcessingMixin** (18 connections) — `server/events/event_bus_processing.py`
- **asyncio** (11 connections)
- **EventBusMixinBase** (10 connections) — `server/events/event_bus_base.py`
- **._handle_event_async()** (8 connections) — `server/events/event_bus_processing.py`
- **test_handle_event_async_async_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_queue_depth_grows_when_consumer_blocked()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **._create_async_subscriber_tasks()** (5 connections) — `server/events/event_bus_processing.py`
- **._publish_in_test_mode()** (5 connections) — `server/events/event_bus_processing.py`
- **test_async_subscriber_error_isolation()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_inject_dispatches_to_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_multiple_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_no_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_no_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_same_events_integration()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 192 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (56 shared connections)
- [NPCBase](NPCBase.md) (28 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (19 shared connections)
- [CombatService](CombatService.md) (12 shared connections)
- [DistributedEventBus](DistributedEventBus.md) (11 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [test_party_flow.py](test_party_flow.py.md) (5 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (4 shared connections)
- [NPCEventReaction](NPCEventReaction.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (3 shared connections)
- [FollowService](FollowService.md) (3 shared connections)

## Source Files

- `server/events/event_bus.py`
- `server/events/event_bus_base.py`
- `server/events/event_bus_processing.py`
- `server/events/event_types.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/events/test_event_bus_lifecycle.py`

## Audit Trail

- EXTRACTED: 461 (79%)
- INFERRED: 123 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*