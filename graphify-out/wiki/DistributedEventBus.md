# DistributedEventBus

> 28 nodes

## Key Concepts

- **DistributedEventBus** (21 connections) — `server/events/distributed_event_bus.py`
- **test_distributed_event_bus.py** (16 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **asyncio** (6 connections)
- **SampleEvent** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_publish_with_nats_bridge_publishes_to_nats()** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_publish_without_nats_delegates_to_parent()** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **distributed_bus()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_set_nats_service_starts_bridge_when_loop_running()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_shutdown_bridge_stop_error_is_swallowed()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_shutdown_stops_bridge()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **.publish()** (3 connections) — `server/events/distributed_event_bus.py`
- **test_distributed_event_bus_init_without_nats()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_set_nats_service_same_reference_noop()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **.shutdown()** (2 connections) — `server/events/distributed_event_bus.py`
- **fixture** (1 connections)
- **EventBus that distributes domain events via NATS for horizontal scaling. When…** (1 connections) — `server/events/distributed_event_bus.py`
- **Publish event locally and to NATS when bridge is active.** (1 connections) — `server/events/distributed_event_bus.py`
- **Shutdown EventBus and stop NATS bridge.** (1 connections) — `server/events/distributed_event_bus.py`
- **Unit tests for DistributedEventBus.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Minimal event for distributed bus tests.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Create a DistributedEventBus without NATS.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Single-instance mode has no bridge until NATS is set.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Setting the same NATS service twice does not recreate the bridge.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Publish without NATS behaves like plain EventBus.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **When bridge is active, publish also sends to NATS.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- *... and 3 more nodes in this community*

## Relationships

- [BaseEvent](BaseEvent.md) (7 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [.set_nats_service](set_nats_service.md) (2 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/tests/unit/events/test_distributed_event_bus.py`

## Audit Trail

- EXTRACTED: 44 (77%)
- INFERRED: 13 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*