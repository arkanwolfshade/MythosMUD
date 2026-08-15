# test_nats_service.py

> 151 nodes

## Key Concepts

- **test_nats_service.py** (77 connections) — `server/tests/unit/services/test_nats_service.py`
- **asyncio** (37 connections)
- **NATSMetrics** (31 connections) — `server/services/nats_metrics.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **nats_service()** (6 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_config()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_config()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_subject_manager()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_no_available_connections()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_not_initialized()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_error()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_not_connected()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_timeout()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_connected()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_running()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_error()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_not_found()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_metrics.py** (4 connections) — `server/services/nats_metrics.py`
- **.get_metrics()** (3 connections) — `server/services/nats_metrics.py`
- **test_cancel_background_tasks()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_cancel_background_tasks_empty()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_circuit_breaker_opens()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_failure()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_state_machine_blocked()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_success()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 126 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (21 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (9 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (3 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)
- [NATSError](NATSError.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/services/nats_metrics.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 210 (85%)
- INFERRED: 36 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*