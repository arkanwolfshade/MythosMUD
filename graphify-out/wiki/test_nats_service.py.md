# test_nats_service.py

> 77 nodes

## Key Concepts

- **test_nats_service.py** (63 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_service.py** (33 connections) — `server/services/nats_service.py`
- **NATSSubscribeError** (23 connections) — `server/services/nats_exceptions.py`
- **asyncio** (23 connections)
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **TestNATSSubscribeError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **test_publish_no_available_connections()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_not_initialized()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_error()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_not_connected()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_timeout()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_connected()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_running()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_error()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_not_found()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_metrics.py** (5 connections) — `server/services/nats_metrics.py`
- **test_connect_circuit_breaker_opens()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_failure()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_state_machine_blocked()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_success()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_flushes_batch()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_handles_drain_error()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_success()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_is_connected_true()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 52 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (35 shared connections)
- [NATSMetrics](NATSMetrics.md) (17 shared connections)
- [NATSError](NATSError.md) (14 shared connections)
- [NATSConfig](NATSConfig.md) (8 shared connections)
- [JsonMap](JsonMap.md) (7 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (7 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (4 shared connections)
- [.__init__](__init__.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 186 (81%)
- INFERRED: 43 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*