# InstanceManager

> 32 nodes

## Key Concepts

- **test_nats_service_health.py** (23 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **asyncio** (15 connections)
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
- **Test _cancel_background_tasks() cancels all tasks.** (2 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **NATS health-check, batch flush, and subscription-lifecycle tests.** (1 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **Test _stop_health_monitoring() handles no task.** (1 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **Test publish_batch() adds message to batch.** (1 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **Test publish_batch() flushes when batch is full.** (1 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **Test _flush_batch() successfully flushes batch.** (1 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **Test _flush_batch() handles empty batch.** (1 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **Test get_connection_stats() returns connection statistics.** (1 connections) — `server/tests/unit/services/test_nats_service_health.py`
- *... and 7 more nodes in this community*

## Relationships

- [PrototypeRegistryError](PrototypeRegistryError.md) (19 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [ChatModeration](ChatModeration.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_nats_service_health.py`

## Audit Trail

- EXTRACTED: 52 (78%)
- INFERRED: 15 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*