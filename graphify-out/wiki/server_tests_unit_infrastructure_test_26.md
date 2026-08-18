# server tests unit infrastructure test

> 86 nodes

## Key Concepts

- **test_nats_broker.py** (57 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **asyncio** (35 connections)
- **nats_broker()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **nats_config()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_failure()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_with_tls_enabled_passes_tls_options()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_error_handling()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_failure()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_not_connected()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_request_failure()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_request_not_connected()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_subscribe_failure()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_subscribe_not_connected()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_unsubscribe_failure()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_already_connected()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_sets_callbacks()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_success()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_connect_with_user_password()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_handles_unsubscribe_error()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_no_client()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_success()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnect_unsubscribes_all()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_disconnected_callback()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_error_callback()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_json_serialization()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- *... and 61 more nodes in this community*

## Relationships

- [server infrastructure message broker](server_infrastructure_message_broker.md) (21 shared connections)
- [server config models nats natsconfig](server_config_models_nats_natsconfig.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 133 (92%)
- INFERRED: 12 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*