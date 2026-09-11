# NATSError

> 102 nodes

## Key Concepts

- **NATSError** (70 connections) — `server/services/nats_exceptions.py`
- **NATSPublishError** (41 connections) — `server/services/nats_exceptions.py`
- **NATSSubscribeError** (23 connections) — `server/services/nats_exceptions.py`
- **test_nats_service_pool.py** (23 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **NATSConnectionError** (14 connections) — `server/services/nats_exceptions.py`
- **NATSHealthCheckError** (13 connections) — `server/services/nats_exceptions.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **asyncio** (11 connections)
- **TestNATSConnectionError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.__init__()** (7 connections) — `server/services/nats_exceptions.py`
- **.test_all_errors_inherit_from_exception()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_all_errors_inherit_from_nats_error()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **Exception** (6 connections)
- **TestNATSError** (5 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **test_flush_batch_records_partial_success_and_cancels_batch_task()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_batch_returns_false_on_subject_validation_failure()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_with_pool_wraps_unexpected_exception()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_recover_failed_batches_requeues_on_repeated_failure()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_retry_failed_batch_groups_recovers_on_retry()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_validate_pool_publish_subject_rejects_invalid_subject()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_validate_pool_publish_subject_wraps_validation_error()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- *... and 77 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (33 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (17 shared connections)
- [combat_service.py](combat_service.py.md) (13 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (12 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (7 shared connections)
- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (7 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (5 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (4 shared connections)
- [test_combat_persistence_handler_events.py](test_combat_persistence_handler_events.py.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [test_nats_message_handler_chat.py](test_nats_message_handler_chat.py.md) (3 shared connections)
- [.publish_with_pool](publish_with_pool.md) (3 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service_pool.py`

## Audit Trail

- EXTRACTED: 212 (74%)
- INFERRED: 74 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*