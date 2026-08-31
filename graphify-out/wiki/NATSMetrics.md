# NATSMetrics

> 64 nodes

## Key Concepts

- **NATSMetrics** (33 connections) — `server/services/nats_metrics.py`
- **NATSServicePoolMixin** (28 connections) — `server/services/nats_service_pool.py`
- **.publish_with_pool()** (9 connections) — `server/services/nats_service_pool.py`
- **._flush_batch()** (8 connections) — `server/services/nats_service_pool.py`
- **._initialize_connection_pool()** (6 connections) — `server/services/nats_service_pool.py`
- **.publish_batch()** (6 connections) — `server/services/nats_service_pool.py`
- **._get_connection()** (5 connections) — `server/services/nats_service_pool.py`
- **._retry_failed_batch_groups()** (5 connections) — `server/services/nats_service_pool.py`
- **._validate_pool_publish_subject()** (5 connections) — `server/services/nats_service_pool.py`
- **._attempt_retry_batch_groups()** (4 connections) — `server/services/nats_service_pool.py`
- **._batch_timeout()** (4 connections) — `server/services/nats_service_pool.py`
- **._build_connect_options()** (4 connections) — `server/services/nats_service_pool.py`
- **._create_tracked_task()** (4 connections) — `server/services/nats_service_pool.py`
- **._publish_batch_groups()** (4 connections) — `server/services/nats_service_pool.py`
- **._return_connection()** (4 connections) — `server/services/nats_service_pool.py`
- **.get_metrics()** (3 connections) — `server/services/nats_metrics.py`
- **._enqueue_exhausted_batch_groups()** (3 connections) — `server/services/nats_service_pool.py`
- **._finalize_pool_init_status()** (3 connections) — `server/services/nats_service_pool.py`
- **._group_batch_messages()** (3 connections) — `server/services/nats_service_pool.py`
- **._record_batch_flush_metrics()** (3 connections) — `server/services/nats_service_pool.py`
- **.recover_failed_batches()** (3 connections) — `server/services/nats_service_pool.py`
- **.__init__()** (2 connections) — `server/services/nats_metrics.py`
- **.record_ack_failure()** (2 connections) — `server/services/nats_metrics.py`
- **.record_ack_success()** (2 connections) — `server/services/nats_metrics.py`
- **.record_batch_flush()** (2 connections) — `server/services/nats_metrics.py`
- *... and 39 more nodes in this community*

## Relationships

- [test_nats_service.py](test_nats_service.py.md) (15 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [NATSError](NATSError.md) (4 shared connections)
- [NATSConfig](NATSConfig.md) (2 shared connections)
- [NATSService](NATSService.md) (2 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (1 shared connections)

## Source Files

- `server/services/nats_metrics.py`
- `server/services/nats_service_pool.py`

## Audit Trail

- EXTRACTED: 112 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*