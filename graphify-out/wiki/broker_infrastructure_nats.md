# broker infrastructure nats

> 56 nodes

## Key Concepts

- **test_nats_broker.py** (49 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **nats_config()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
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
- **test_subscribe_with_queue_group()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_subscribe_without_queue_group()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_subscribe_message_wrapper_calls_handler()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_subscribe_message_wrapper_handles_error()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_unsubscribe_success()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_unsubscribe_not_found()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_request_success()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_request_timeout()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_error_callback()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- *... and 31 more nodes in this community*

## Relationships

- [command factories communication](command_factories_communication.md) (10 shared connections)
- [game models enums](game_models_enums.md) (3 shared connections)
- [message handlers realtime](message_handlers_realtime.md) (3 shared connections)
- [infrastructure nats broker](infrastructure_nats_broker.md) (3 shared connections)
- [config models rationale](config_models_rationale.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 132 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*