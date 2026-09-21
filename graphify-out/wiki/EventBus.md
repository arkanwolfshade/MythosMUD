# EventBus

> 130 nodes

## Key Concepts

- **EventBus** (225 connections) — `server/events/event_bus.py`
- **BaseEvent** (99 connections) — `server/events/event_types.py`
- **test_event_bus.py** (59 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (28 connections)
- **MockEventClass** (19 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_async_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_queue_depth_grows_when_consumer_blocked()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **._publish_in_test_mode()** (5 connections) — `server/events/event_bus_processing.py`
- **test_async_subscriber_error_isolation()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_inject_dispatches_to_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_multiple_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_no_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_no_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_same_events_integration()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_service_shutdown_removes_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_shutdown_cleans_up_service_subscriptions()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **._invoke_test_mode_subscriber()** (4 connections) — `server/events/event_bus_processing.py`
- **.publish()** (4 connections) — `server/events/event_bus_processing.py`
- **event_bus()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts_multiple_types()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 105 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (37 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (26 shared connections)
- [get_logger](get_logger.md) (23 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (21 shared connections)
- [NPCDefinition](NPCDefinition.md) (15 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (14 shared connections)
- [event_serialization.py](event_serialization.py.md) (11 shared connections)
- [CombatService](CombatService.md) (10 shared connections)
- [PartyService](PartyService.md) (8 shared connections)
- [DistributedEventBus](DistributedEventBus.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (4 shared connections)

## Source Files

- `server/events/event_bus.py`
- `server/events/event_bus_processing.py`
- `server/events/event_types.py`
- `server/realtime/connection_manager.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 367 (75%)
- INFERRED: 123 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*