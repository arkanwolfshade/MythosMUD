# BaseEvent

> 151 nodes

## Key Concepts

- **BaseEvent** (99 connections) — `server/events/event_types.py`
- **test_event_bus.py** (59 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (28 connections)
- **MockEventClass** (19 connections) — `server/tests/unit/events/test_event_bus.py`
- **EventBusProcessingMixin** (18 connections) — `server/events/event_bus_processing.py`
- **._handle_event_async()** (8 connections) — `server/events/event_bus_processing.py`
- **_ExperienceEventBus** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **test_handle_event_async_async_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_queue_depth_grows_when_consumer_blocked()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **Any** (6 connections)
- **._create_async_subscriber_tasks()** (5 connections) — `server/events/event_bus_processing.py`
- **.publish()** (5 connections) — `server/events/event_bus_processing.py`
- **._publish_in_test_mode()** (5 connections) — `server/events/event_bus_processing.py`
- **test_async_subscriber_error_isolation()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_inject_dispatches_to_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_multiple_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_no_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_no_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_same_events_integration()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_service_shutdown_removes_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 126 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (75 shared connections)
- [event_serialization.py](event_serialization.py.md) (13 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (10 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (5 shared connections)
- [DistributedEventBus](DistributedEventBus.md) (4 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (2 shared connections)
- [ValueError](ValueError.md) (2 shared connections)
- [_PlayerCombatClearing](_PlayerCombatClearing.md) (1 shared connections)
- [MythosTimeEventConsumer](MythosTimeEventConsumer.md) (1 shared connections)

## Source Files

- `server/events/event_bus.py`
- `server/events/event_bus_processing.py`
- `server/events/event_types.py`
- `server/npc/event_reaction_system.py`
- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 283 (77%)
- INFERRED: 84 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*