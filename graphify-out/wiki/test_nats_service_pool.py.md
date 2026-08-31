# test_nats_service_pool.py

> 32 nodes

## Key Concepts

- **test_nats_service_pool.py** (24 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **asyncio** (11 connections)
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
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
- **test_publish_batch_returns_false_on_unexpected_exception()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_recover_failed_batches_recovers_successfully()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **fixture** (2 connections)
- **Unit tests for NATSServicePoolMixin's exception-handling and retry branches.…** (1 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **_cleanup_connection_pool's outer try/except tolerates a failure enumerating the…** (1 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **publish_batch returns False (not raise) when subject validation rejects the…** (1 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **publish_batch's outer handler catches an unexpected exception and returns False.** (1 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **_flush_batch reports partial success when one subject group fails, then clears…** (1 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **_retry_failed_batch_groups republishes a failed group successfully on its retry…** (1 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **recover_failed_batches puts a message back in the failed queue if recovery also…** (1 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **recover_failed_batches drains the failed queue and reports the recovered count.** (1 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- *... and 7 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (14 shared connections)
- [NATSError](NATSError.md) (8 shared connections)
- [NATSConfig](NATSConfig.md) (3 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [SubjectValidator](SubjectValidator.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_nats_service_pool.py`

## Audit Trail

- EXTRACTED: 56 (76%)
- INFERRED: 18 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*