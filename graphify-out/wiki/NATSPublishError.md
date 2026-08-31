# NATSPublishError

> 85 nodes

## Key Concepts

- **NATSPublishError** (41 connections) — `server/services/nats_exceptions.py`
- **test_nats_service_pool.py** (24 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **NATSConnectionError** (14 connections) — `server/services/nats_exceptions.py`
- **test_nats_exceptions.py** (14 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **NATSHealthCheckError** (13 connections) — `server/services/nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **asyncio** (11 connections)
- **TestNATSConnectionError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.__init__()** (7 connections) — `server/services/nats_exceptions.py`
- **.test_all_errors_inherit_from_exception()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_all_errors_inherit_from_nats_error()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **Exception** (6 connections)
- **test_flush_batch_records_partial_success_and_cancels_batch_task()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_batch_returns_false_on_subject_validation_failure()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_with_pool_wraps_unexpected_exception()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_recover_failed_batches_requeues_on_repeated_failure()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_retry_failed_batch_groups_recovers_on_retry()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_validate_pool_publish_subject_rejects_invalid_subject()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_validate_pool_publish_subject_wraps_validation_error()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **nats_config()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_cleanup_connection_pool_swallows_cancelled_error()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_cleanup_connection_pool_swallows_close_error()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_cleanup_connection_pool_swallows_outer_exception()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- *... and 60 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (39 shared connections)
- [NATSError](NATSError.md) (10 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (5 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (4 shared connections)
- [.publish_with_pool](publish_with_pool.md) (3 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [SubjectValidator](SubjectValidator.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service_pool.py`

## Audit Trail

- EXTRACTED: 163 (82%)
- INFERRED: 37 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*