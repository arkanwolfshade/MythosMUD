# Distributed Event Bus (NATS)

> 305 nodes

## Key Concepts

- **EventBus** (182 connections) — `server/events/event_bus.py`
- **BaseEvent** (85 connections) — `server/events/event_types.py`
- **test_event_bus.py** (59 connections) — `server/tests/unit/events/test_event_bus.py`
- **event_bus.py** (40 connections) — `server/events/event_bus.py`
- **asyncio** (28 connections)
- **test_event_bus_lifecycle.py** (24 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **DistributedEventBus** (21 connections) — `server/events/distributed_event_bus.py`
- **MockEventClass** (19 connections) — `server/tests/unit/events/test_event_bus.py`
- **EventBusProcessingMixin** (18 connections) — `server/events/event_bus_processing.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **test_distributed_event_bus.py** (15 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **test_party_flow.py** (13 connections) — `server/tests/integration/test_party_flow.py`
- **distributed_event_bus.py** (11 connections) — `server/events/distributed_event_bus.py`
- **asyncio** (11 connections)
- **event_bus_processing.py** (9 connections) — `server/events/event_bus_processing.py`
- **test_nats_event_bridge.py** (9 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **EventBusMixinBase** (8 connections) — `server/events/event_bus_base.py`
- **PartyUpdated** (8 connections) — `server/events/event_types.py`
- **._handle_event_async()** (8 connections) — `server/events/event_bus_processing.py`
- **test_handle_event_async_async_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 280 more nodes in this community*

## Relationships

- [NPC Behavior Engine](NPC_Behavior_Engine.md) (51 shared connections)
- [Game Event Types](Game_Event_Types.md) (30 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (17 shared connections)
- [Community 65](Community_65.md) (10 shared connections)
- [NPC Room Lifecycle](NPC_Room_Lifecycle.md) (9 shared connections)
- [Community 53](Community_53.md) (6 shared connections)
- [Community 254](Community_254.md) (6 shared connections)
- [Community 318](Community_318.md) (5 shared connections)
- [Community 497](Community_497.md) (5 shared connections)
- [Community 451](Community_451.md) (4 shared connections)
- [Community 48](Community_48.md) (4 shared connections)
- [Community 92](Community_92.md) (4 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_bus_base.py`
- `server/events/event_bus_lifecycle.py`
- `server/events/event_bus_processing.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/tests/integration/test_party_flow.py`
- `server/tests/unit/events/test_distributed_event_bus.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/events/test_event_bus_lifecycle.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 607 (83%)
- INFERRED: 127 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*