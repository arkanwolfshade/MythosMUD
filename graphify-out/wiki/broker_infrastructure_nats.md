# broker infrastructure nats

> 97 nodes

## Key Concepts

- **test_nats_broker.py** (56 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **nats_broker.py** (17 connections) — `server/infrastructure/nats_broker.py`
- **MessageBrokerError** (13 connections) — `server/infrastructure/message_broker.py`
- **message_broker.py** (11 connections) — `server/infrastructure/message_broker.py`
- **PublishError** (9 connections) — `server/infrastructure/message_broker.py`
- **SubscribeError** (9 connections) — `server/infrastructure/message_broker.py`
- **RequestError** (9 connections) — `server/infrastructure/message_broker.py`
- **MessageBrokerConnectionError** (8 connections) — `server/infrastructure/message_broker.py`
- **UnsubscribeError** (8 connections) — `server/infrastructure/message_broker.py`
- **nats_config()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
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
- *... and 72 more nodes in this community*

## Relationships

- [infrastructure nats broker](infrastructure_nats_broker.md) (17 shared connections)
- [combat validator validators](combat_validator_validators.md) (4 shared connections)
- [infrastructure message broker](infrastructure_message_broker.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [schemas nats messages](schemas_nats_messages.md) (1 shared connections)
- [zone npc config](zone_npc_config.md) (1 shared connections)
- [manager subject services](manager_subject_services.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 250 (91%)
- INFERRED: 24 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*