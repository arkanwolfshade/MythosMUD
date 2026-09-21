# NATSService

> 199 nodes

## Key Concepts

- **NATSService** (155 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (59 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **NATSConfig** (34 connections) — `server/config/models/nats.py`
- **asyncio** (26 connections)
- **test_nats_service_health.py** (23 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_nats_service_pool.py** (23 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **asyncio** (15 connections)
- **asyncio** (11 connections)
- **._create_tracked_task()** (7 connections) — `server/services/nats_service.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **.connect()** (6 connections) — `server/services/nats_service.py`
- **.__init__()** (6 connections) — `server/services/nats_service.py`
- **_assert_tracked_coro_closed()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_start_health_monitoring_creates_task()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_nats_service_init_with_config()** (6 connections) — `server/tests/unit/services/test_nats_service.py`
- **.disconnect()** (5 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_flush_batch_records_partial_success_and_cancels_batch_task()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_batch_returns_false_on_subject_validation_failure()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_with_pool_wraps_unexpected_exception()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_recover_failed_batches_requeues_on_repeated_failure()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- *... and 174 more nodes in this community*

## Relationships

- [NATSError](NATSError.md) (56 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (5 shared connections)
- [NatsSubscription](NatsSubscription.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [combat_service.py](combat_service.py.md) (2 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (2 shared connections)
- [SubjectValidator](SubjectValidator.md) (2 shared connections)
- [test_config_models.py](test_config_models.py.md) (1 shared connections)
- [AppConfig](AppConfig.md) (1 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/services/test_nats_service_health.py`
- `server/tests/unit/services/test_nats_service_helpers.py`
- `server/tests/unit/services/test_nats_service_pool.py`

## Audit Trail

- EXTRACTED: 353 (76%)
- INFERRED: 113 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*