# Nats Event Bridge

> 24 nodes

## Key Concepts

- **NATSEventBusBridge** (18 connections) — `server/events/nats_event_bridge.py`
- **test_nats_event_bridge.py** (10 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
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
- **Tests for NATS EventBus bridge - skip self-echo to prevent duplicate event…** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **NATS bridge must not inject events that originated from this instance (prevents…** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **NATS bridge must inject events from other instances.** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **publish() serializes event and forwards to NATS with origin metadata.** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **Invalid payloads are ignored without injecting.** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`

## Relationships

- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (3 shared connections)
- [Test Distributed Event Bus](Test_Distributed_Event_Bus.md) (2 shared connections)
- [Event Serialization](Event_Serialization.md) (1 shared connections)
- [NATS Service Client](NATS_Service_Client.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/events/nats_event_bridge.py`
- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 40 (83%)
- INFERRED: 8 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*