# test_nats_service.py

> 87 nodes

## Key Concepts

- **test_nats_service.py** (78 connections) — `server/tests/unit/services/test_nats_service.py`
- **asyncio** (37 connections)
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **test_publish_no_available_connections()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_not_initialized()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_error()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_not_connected()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_timeout()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_connected()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_running()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_error()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_not_found()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_cancel_background_tasks()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_cancel_background_tasks_empty()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_circuit_breaker_opens()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_failure()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_state_machine_blocked()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_success()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_flushes_batch()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_handles_drain_error()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_removes_all_subscriptions()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_success()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_flush_batch_empty()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_flush_batch_success()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_is_connected_true()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 62 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (46 shared connections)
- [NATSMetrics](NATSMetrics.md) (15 shared connections)
- [NATSPublishError](NATSPublishError.md) (7 shared connections)
- [NATSConfig](NATSConfig.md) (7 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (4 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (2 shared connections)
- [JsonMap](JsonMap.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 161 (76%)
- INFERRED: 51 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*