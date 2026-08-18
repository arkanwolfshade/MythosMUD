# test_nats_service_health.py

> 38 nodes

## Key Concepts

- **test_nats_service_health.py** (23 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **asyncio** (15 connections)
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **nats_config()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_cancel_background_tasks()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_cancel_background_tasks_empty()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_disconnect_removes_all_subscriptions()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_flush_batch_empty()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_flush_batch_success()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_perform_health_check_error()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_perform_health_check_no_client()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_perform_health_check_success()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_perform_health_check_timeout()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_publish_batch_adds_to_batch()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_publish_batch_flushes_when_full()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_service_restart_no_duplicate_subscriptions()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_stop_health_monitoring()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_stop_health_monitoring_no_task()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_get_connection_stats()** (3 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **fixture** (2 connections)
- **NATS health-check, batch flush, and subscription-lifecycle tests.** (1 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **Test _stop_health_monitoring() handles no task.** (1 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **Test publish_batch() adds message to batch.** (1 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **Test publish_batch() flushes when batch is full.** (1 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **Test _flush_batch() successfully flushes batch.** (1 connections) — `server/tests/unit/services/test_nats_service_health.py`
- *... and 13 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (17 shared connections)
- [NATSConfig](NATSConfig.md) (3 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_nats_service_health.py`

## Audit Trail

- EXTRACTED: 59 (80%)
- INFERRED: 15 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*