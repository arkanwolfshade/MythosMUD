# NATSEventBusBridge

> 23 nodes

## Key Concepts

- **NATSEventBusBridge** (16 connections) — `server/events/nats_event_bridge.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **.set_nats_service()** (4 connections) — `server/events/distributed_event_bus.py`
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **test_handle_nats_message_injects_remote_origin()** (4 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **test_handle_nats_message_skips_own_origin()** (4 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **.__init__()** (3 connections) — `server/events/distributed_event_bus.py`
- **Any** (3 connections)
- **.start()** (2 connections) — `server/events/nats_event_bridge.py`
- **.stop()** (2 connections) — `server/events/nats_event_bridge.py`
- **Any** (2 connections)
- **asyncio** (2 connections)
- **Initialize distributed EventBus. Args: nats_service: NATS service for…** (1 connections) — `server/events/distributed_event_bus.py`
- **Set NATS service and start the bridge (call after NATS connects).** (1 connections) — `server/events/distributed_event_bus.py`
- **Subscribe to NATS domain events and start receiving.** (1 connections) — `server/events/nats_event_bridge.py`
- **Stop the bridge and unsubscribe from NATS.** (1 connections) — `server/events/nats_event_bridge.py`
- **Bridges domain events between local EventBus and NATS for distribution. When…** (1 connections) — `server/events/nats_event_bridge.py`
- **Initialize the NATS EventBus bridge. Args: event_bus: Local EventBus instance…** (1 connections) — `server/events/nats_event_bridge.py`
- **Process a NATS message - deserialize and inject into local EventBus. Public for…** (1 connections) — `server/events/nats_event_bridge.py`
- **Handle message received from NATS - deserialize and inject into local EventBus.** (1 connections) — `server/events/nats_event_bridge.py`
- **NATS bridge must not inject events that originated from this instance (prevents…** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **NATS bridge must inject events from other instances.** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`

## Relationships

- [event_types.py](event_types.py.md) (9 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [NATSService](NATSService.md) (1 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 37 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*