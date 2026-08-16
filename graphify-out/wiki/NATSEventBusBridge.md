# NATSEventBusBridge

> 22 nodes

## Key Concepts

- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **._handle_nats_message_impl()** (5 connections) — `server/events/nats_event_bridge.py`
- **test_handle_nats_message_injects_remote_origin()** (5 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **test_publish_adds_origin_and_calls_nats()** (5 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **.handle_nats_message()** (4 connections) — `server/events/nats_event_bridge.py`
- **.__init__()** (4 connections) — `server/events/nats_event_bridge.py`
- **test_handle_nats_message_bad_payload_logs_warning()** (4 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **test_handle_nats_message_skips_own_origin()** (4 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **asyncio** (4 connections)
- **Any** (3 connections)
- **.start()** (2 connections) — `server/events/nats_event_bridge.py`
- **.stop()** (2 connections) — `server/events/nats_event_bridge.py`
- **Subscribe to NATS domain events and start receiving.** (1 connections) — `server/events/nats_event_bridge.py`
- **Stop the bridge and unsubscribe from NATS.** (1 connections) — `server/events/nats_event_bridge.py`
- **Bridges domain events between local EventBus and NATS for distribution. When…** (1 connections) — `server/events/nats_event_bridge.py`
- **Initialize the NATS EventBus bridge. Args: event_bus: Local EventBus instance…** (1 connections) — `server/events/nats_event_bridge.py`
- **Process a NATS message - deserialize and inject into local EventBus. Public for…** (1 connections) — `server/events/nats_event_bridge.py`
- **Handle message received from NATS - deserialize and inject into local EventBus.** (1 connections) — `server/events/nats_event_bridge.py`
- **NATS bridge must not inject events that originated from this instance (prevents…** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **NATS bridge must inject events from other instances.** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **publish() serializes event and forwards to NATS with origin metadata.** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **Invalid payloads are ignored without injecting.** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [DistributedEventBus](DistributedEventBus.md) (2 shared connections)
- [NATSService](NATSService.md) (1 shared connections)

## Source Files

- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 35 (81%)
- INFERRED: 8 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*