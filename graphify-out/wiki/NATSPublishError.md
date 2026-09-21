# NATSPublishError

> 157 nodes

## Key Concepts

- **NATSPublishError** (41 connections) — `server/services/nats_exceptions.py`
- **NATSMetrics** (35 connections) — `server/services/nats_metrics.py`
- **nats_service.py** (31 connections) — `server/services/nats_service.py`
- **NATSServicePoolMixin** (28 connections) — `server/services/nats_service_pool.py`
- **test_nats_service_pool.py** (23 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **nats_service_pool.py** (19 connections) — `server/services/nats_service_pool.py`
- **nats_service_connect.py** (11 connections) — `server/services/nats_service_connect.py`
- **asyncio** (11 connections)
- **NatsConnectOptions** (9 connections) — `server/services/nats_service_connect.py`
- **.publish_with_pool()** (9 connections) — `server/services/nats_service_pool.py`
- **._flush_batch()** (8 connections) — `server/services/nats_service_pool.py`
- **configure_nats_tls()** (6 connections) — `server/services/nats_service_connect.py`
- **nats_connect()** (6 connections) — `server/services/nats_service_connect.py`
- **._initialize_connection_pool()** (6 connections) — `server/services/nats_service_pool.py`
- **.publish_batch()** (6 connections) — `server/services/nats_service_pool.py`
- **nats_metrics.py** (6 connections) — `server/services/nats_metrics.py`
- **_NatsListenerClient** (5 connections) — `server/services/nats_service.py`
- **._configure_tls()** (5 connections) — `server/services/nats_service_pool.py`
- **._create_pool_connections()** (5 connections) — `server/services/nats_service_pool.py`
- **._get_connection()** (5 connections) — `server/services/nats_service_pool.py`
- **._retry_failed_batch_groups()** (5 connections) — `server/services/nats_service_pool.py`
- **._validate_pool_publish_subject()** (5 connections) — `server/services/nats_service_pool.py`
- **test_flush_batch_records_partial_success_and_cancels_batch_task()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_batch_returns_false_on_subject_validation_failure()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_with_pool_wraps_unexpected_exception()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- *... and 132 more nodes in this community*

## Relationships

- [NATSError](NATSError.md) (45 shared connections)
- [NATSService](NATSService.md) (29 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (10 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (4 shared connections)
- [test_config_models.py](test_config_models.py.md) (4 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (2 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/services/nats_service_connect.py`
- `server/services/nats_service_pool.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/services/test_nats_service_pool.py`

## Audit Trail

- EXTRACTED: 294 (89%)
- INFERRED: 35 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*