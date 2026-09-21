# EventBus

> 306 nodes

## Key Concepts

- **EventBus** (225 connections) — `server/events/event_bus.py`
- **BaseEvent** (99 connections) — `server/events/event_types.py`
- **test_event_bus.py** (59 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (28 connections)
- **test_event_bus_lifecycle.py** (24 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **DistributedEventBus** (21 connections) — `server/events/distributed_event_bus.py`
- **MockEventClass** (19 connections) — `server/tests/unit/events/test_event_bus.py`
- **event_serialization.py** (19 connections) — `server/events/event_serialization.py`
- **EventBusProcessingMixin** (18 connections) — `server/events/event_bus_processing.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **test_distributed_event_bus.py** (15 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (14 connections) — `server/tests/unit/events/test_event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **distributed_event_bus.py** (11 connections) — `server/events/distributed_event_bus.py`
- **asyncio** (11 connections)
- **._handle_event_async()** (8 connections) — `server/events/event_bus_processing.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **_ExperienceEventBus** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **test_handle_event_async_async_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 281 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (67 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (24 shared connections)
- [NPCBase](NPCBase.md) (22 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (15 shared connections)
- [combat_service.py](combat_service.py.md) (15 shared connections)
- [PartyService](PartyService.md) (7 shared connections)
- [NPCDied](NPCDied.md) (4 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (4 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [async_persistence.py](async_persistence.py.md) (3 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (3 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_bus_processing.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/events/test_distributed_event_bus.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/events/test_event_bus_lifecycle.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/time/tick_scheduler.py`

## Audit Trail

- EXTRACTED: 635 (82%)
- INFERRED: 136 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*