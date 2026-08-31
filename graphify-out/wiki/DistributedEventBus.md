# DistributedEventBus

> 54 nodes

## Key Concepts

- **DistributedEventBus** (21 connections) — `server/events/distributed_event_bus.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **test_distributed_event_bus.py** (16 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **distributed_event_bus.py** (12 connections) — `server/events/distributed_event_bus.py`
- **asyncio** (6 connections)
- **SampleEvent** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_publish_with_nats_bridge_publishes_to_nats()** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_publish_without_nats_delegates_to_parent()** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **.set_nats_service()** (4 connections) — `server/events/distributed_event_bus.py`
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **._subject_for_event()** (4 connections) — `server/events/nats_event_bridge.py`
- **distributed_bus()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_set_nats_service_starts_bridge_when_loop_running()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_shutdown_bridge_stop_error_is_swallowed()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_shutdown_stops_bridge()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **.__init__()** (3 connections) — `server/events/distributed_event_bus.py`
- **.publish()** (3 connections) — `server/events/distributed_event_bus.py`
- **test_distributed_event_bus_init_without_nats()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_set_nats_service_same_reference_noop()** (3 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **Any** (3 connections)
- **.shutdown()** (2 connections) — `server/events/distributed_event_bus.py`
- *... and 29 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (11 shared connections)
- [event_types.py](event_types.py.md) (10 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [NATSService](NATSService.md) (2 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_distributed_event_bus.py`

## Audit Trail

- EXTRACTED: 102 (89%)
- INFERRED: 13 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*