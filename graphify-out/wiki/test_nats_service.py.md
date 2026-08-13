# test_nats_service.py

> 87 nodes

## Key Concepts

- **test_nats_service.py** (77 connections) — `server/tests/unit/services/test_nats_service.py`
- **asyncio** (37 connections)
- **test_cancel_background_tasks()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_cancel_background_tasks_empty()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_circuit_breaker_opens()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_failure()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_state_machine_blocked()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_success()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_flushes_batch()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_handles_drain_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_removes_all_subscriptions()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_success()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_flush_batch_empty()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_flush_batch_success()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_is_connected_true()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_connection_pool()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_config()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_dict()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_perform_health_check_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_perform_health_check_no_client()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_perform_health_check_success()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_perform_health_check_timeout()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_batch_adds_to_batch()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_batch_flushes_when_full()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_no_available_connections()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 62 more nodes in this community*

## Relationships

- [NATSMetrics](NATSMetrics.md) (16 shared connections)
- [NATSService](NATSService.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_nats_service_init_with_subject_manager](test_nats_service_init_with_subject_manager.md) (3 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (2 shared connections)
- [nats_service](nats_service.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [AppConfig](AppConfig.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 158 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*