# nats services service

> 90 nodes

## Key Concepts

- **test_nats_service.py** (76 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_subject_manager()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_config()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_connection_pool()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_message_batch()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_not_initialized()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_no_available_connections()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_connected()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_running()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_not_found()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_not_connected()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_timeout()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_success()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_state_machine_blocked()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_failure()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_circuit_breaker_opens()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_success()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_flushes_batch()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_handles_drain_error()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_success()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_success()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_with_manual_ack()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 65 more nodes in this community*

## Relationships

- [nats services metrics](nats_services_metrics.md) (17 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (11 shared connections)
- [Item Instances](Item_Instances.md) (9 shared connections)
- [config models rationale](config_models_rationale.md) (4 shared connections)
- [connection state machine](connection_state_machine.md) (2 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 215 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*