# NATSServicePoolMixin

> 38 nodes

## Key Concepts

- **NATSServicePoolMixin** (28 connections) — `server/services/nats_service_pool.py`
- **.publish_with_pool()** (9 connections) — `server/services/nats_service_pool.py`
- **._flush_batch()** (8 connections) — `server/services/nats_service_pool.py`
- **.publish_batch()** (6 connections) — `server/services/nats_service_pool.py`
- **._get_connection()** (5 connections) — `server/services/nats_service_pool.py`
- **._retry_failed_batch_groups()** (5 connections) — `server/services/nats_service_pool.py`
- **._validate_pool_publish_subject()** (5 connections) — `server/services/nats_service_pool.py`
- **._attempt_retry_batch_groups()** (4 connections) — `server/services/nats_service_pool.py`
- **._batch_timeout()** (4 connections) — `server/services/nats_service_pool.py`
- **._create_tracked_task()** (4 connections) — `server/services/nats_service_pool.py`
- **._publish_batch_groups()** (4 connections) — `server/services/nats_service_pool.py`
- **._return_connection()** (4 connections) — `server/services/nats_service_pool.py`
- **._enqueue_exhausted_batch_groups()** (3 connections) — `server/services/nats_service_pool.py`
- **._finalize_pool_init_status()** (3 connections) — `server/services/nats_service_pool.py`
- **._group_batch_messages()** (3 connections) — `server/services/nats_service_pool.py`
- **._record_batch_flush_metrics()** (3 connections) — `server/services/nats_service_pool.py`
- **.recover_failed_batches()** (3 connections) — `server/services/nats_service_pool.py`
- **._cleanup_connection_pool()** (2 connections) — `server/services/nats_service_pool.py`
- **Client** (2 connections)
- **Task** (1 connections)
- **Set pool initialized flag and log full/partial/none success.** (1 connections) — `server/services/nats_service_pool.py`
- **Get connection from pool. Raises: NATSPublishError: If no connection is…** (1 connections) — `server/services/nats_service_pool.py`
- **Return connection to pool.** (1 connections) — `server/services/nats_service_pool.py`
- **Validate subject when subject manager and validation are enabled.** (1 connections) — `server/services/nats_service_pool.py`
- **Publish message using connection pool for high-throughput scenarios. Args:…** (1 connections) — `server/services/nats_service_pool.py`
- *... and 13 more nodes in this community*

## Relationships

- [config/models/__init__.py](config-models-__init__.py.md) (6 shared connections)
- [NATSError](NATSError.md) (5 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [NATSMetrics](NATSMetrics.md) (1 shared connections)

## Source Files

- `server/services/nats_service_pool.py`

## Audit Trail

- EXTRACTED: 65 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*