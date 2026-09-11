# EventBus

> 325 nodes

## Key Concepts

- **EventBus** (224 connections) — `server/events/event_bus.py`
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
- **EventBusMixinBase** (10 connections) — `server/events/event_bus_base.py`
- **event_bus_processing.py** (9 connections) — `server/events/event_bus_processing.py`
- **test_nats_event_bridge.py** (9 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **._handle_event_async()** (8 connections) — `server/events/event_bus_processing.py`
- **_ExperienceEventBus** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **test_handle_event_async_async_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 300 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (55 shared connections)
- [NPCBase](NPCBase.md) (31 shared connections)
- [NPCDefinition](NPCDefinition.md) (21 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (9 shared connections)
- [PartyService](PartyService.md) (7 shared connections)
- [Room](Room.md) (6 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (5 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (4 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [combat_service.py](combat_service.py.md) (3 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_bus_base.py`
- `server/events/event_bus_processing.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/events/test_distributed_event_bus.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/events/test_event_bus_lifecycle.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 661 (83%)
- INFERRED: 137 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*