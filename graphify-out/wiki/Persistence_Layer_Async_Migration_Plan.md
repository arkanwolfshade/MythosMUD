# Persistence Layer Async Migration Plan

> 11 nodes

## Key Concepts

- **test_nats_event_bridge.py** (10 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **test_handle_nats_message_injects_remote_origin()** (5 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **test_publish_adds_origin_and_calls_nats()** (5 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **test_handle_nats_message_bad_payload_logs_warning()** (4 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **test_handle_nats_message_skips_own_origin()** (4 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **asyncio** (4 connections)
- **Tests for NATS EventBus bridge - skip self-echo to prevent duplicate event…** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **NATS bridge must not inject events that originated from this instance (prevents…** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **NATS bridge must inject events from other instances.** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **publish() serializes event and forwards to NATS with origin metadata.** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`
- **Invalid payloads are ignored without injecting.** (1 connections) — `server/tests/unit/events/test_nats_event_bridge.py`

## Relationships

- [pylint.py](pylint.py.md) (5 shared connections)
- [NPCDefinition](NPCDefinition.md) (5 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 18 (75%)
- INFERRED: 6 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*