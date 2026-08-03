# main rationale failure()

> 31 nodes

## Key Concepts

- **DistributedEventBus** (22 connections) — `server/events/distributed_event_bus.py`
- **test_distributed_event_bus.py** (14 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **SampleEvent** (6 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **.set_nats_service()** (4 connections) — `server/events/distributed_event_bus.py`
- **test_publish_without_nats_delegates_to_parent()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_publish_with_nats_bridge_publishes_to_nats()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **.__init__()** (3 connections) — `server/events/distributed_event_bus.py`
- **.publish()** (3 connections) — `server/events/distributed_event_bus.py`
- **distributed_bus()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_distributed_event_bus_init_without_nats()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_set_nats_service_same_reference_noop()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_shutdown_stops_bridge()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_shutdown_bridge_stop_error_is_swallowed()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_set_nats_service_starts_bridge_when_loop_running()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Any** (2 connections)
- **.shutdown()** (2 connections) — `server/events/distributed_event_bus.py`
- **EventBus that distributes domain events via NATS for horizontal scaling.      Wh** (1 connections) — `server/events/distributed_event_bus.py`
- **Initialize distributed EventBus.          Args:             nats_service: NATS s** (1 connections) — `server/events/distributed_event_bus.py`
- **Set NATS service and start the bridge (call after NATS connects).** (1 connections) — `server/events/distributed_event_bus.py`
- **Publish event locally and to NATS when bridge is active.** (1 connections) — `server/events/distributed_event_bus.py`
- **Shutdown EventBus and stop NATS bridge.** (1 connections) — `server/events/distributed_event_bus.py`
- **Unit tests for DistributedEventBus.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Minimal event for distributed bus tests.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Create a DistributedEventBus without NATS.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Single-instance mode has no bridge until NATS is set.** (1 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- *... and 6 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (10 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [memory lifespan app](memory_lifespan_app.md) (1 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/tests/unit/events/test_distributed_event_bus.py`

## Audit Trail

- EXTRACTED: 88 (91%)
- INFERRED: 9 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*