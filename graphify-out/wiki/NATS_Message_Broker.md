# NATS Message Broker

> 81 nodes · cohesion 0.03

## Key Concepts

- **test_nats_broker.py** (47 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **nats_broker()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **nats_config()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_with_tls_enabled_passes_tls_options()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test is_connected() returns False when not connected.** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_already_connected()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_failure()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_sets_callbacks()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_success()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_error_handling()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_handles_unsubscribe_error()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_no_client()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_success()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_unsubscribes_all()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnected_callback()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_error_callback()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_is_connected_false_no_client()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_is_connected_false_not_connected()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_is_connected_true()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_nats_message_broker_init()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_failure()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_json_serialization()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_not_connected()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_success()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_reconnected_callback()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- *... and 56 more nodes in this community*

## Relationships

- [[Message Broker Errors]] (9 shared connections)
- [[Combat Domain Events]] (4 shared connections)
- [[Application Config Settings]] (2 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_nats_broker.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 177 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
