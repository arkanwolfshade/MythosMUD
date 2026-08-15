# DistributedEventBus

> 83 nodes

## Key Concepts

- **DistributedEventBus** (21 connections) — `server/events/distributed_event_bus.py`
- **event_serialization.py** (20 connections) — `server/events/event_serialization.py`
- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **test_distributed_event_bus.py** (15 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **deserialize_event()** (14 connections) — `server/events/event_serialization.py`
- **serialize_event()** (13 connections) — `server/events/event_serialization.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **distributed_event_bus.py** (11 connections) — `server/events/distributed_event_bus.py`
- **asyncio** (6 connections)
- **SampleEvent** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **_convert_value_from_json()** (5 connections) — `server/events/event_serialization.py`
- **_register_event_types()** (5 connections) — `server/events/event_serialization.py`
- **_register_module_events()** (5 connections) — `server/events/event_serialization.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **.publish()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_publish_with_nats_bridge_publishes_to_nats()** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_publish_without_nats_delegates_to_parent()** (5 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- **test_serialize_deserialize_player_xp_award_event()** (5 connections) — `server/tests/unit/events/test_event_serialization.py`
- **.set_nats_service()** (4 connections) — `server/events/distributed_event_bus.py`
- **_extract_event_fields()** (4 connections) — `server/events/event_serialization.py`
- **_init_kwargs_from_event_data()** (4 connections) — `server/events/event_serialization.py`
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **._subject_for_event()** (4 connections) — `server/events/nats_event_bridge.py`
- **distributed_bus()** (4 connections) — `server/tests/unit/events/test_distributed_event_bus.py`
- *... and 58 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (48 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (1 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_serialization.py`
- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_distributed_event_bus.py`
- `server/tests/unit/events/test_event_serialization.py`

## Audit Trail

- EXTRACTED: 151 (85%)
- INFERRED: 27 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*