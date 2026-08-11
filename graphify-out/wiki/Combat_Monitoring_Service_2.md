# Combat Monitoring Service

> 74 nodes

## Key Concepts

- **test_nats_broker.py** (49 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **nats_broker()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_error_handling()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_not_connected()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_subscribe_not_connected()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_subscribe_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_unsubscribe_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_request_not_connected()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_request_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_nats_message_broker_init()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_success()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_already_connected()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_sets_callbacks()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_no_client()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_success()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_unsubscribes_all()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_handles_unsubscribe_error()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_is_connected_true()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_is_connected_false_no_client()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_is_connected_false_not_connected()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_success()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_json_serialization()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_subscribe_success()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- *... and 49 more nodes in this community*

## Relationships

- [Realtime Event Delegation](Realtime_Event_Delegation.md) (19 shared connections)
- [Player Death Service](Player_Death_Service.md) (3 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 159 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*