# .publish_with_pool

> 32 nodes

## Key Concepts

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
- **._group_batch_messages()** (3 connections) — `server/services/nats_service_pool.py`
- **._record_batch_flush_metrics()** (3 connections) — `server/services/nats_service_pool.py`
- **.recover_failed_batches()** (3 connections) — `server/services/nats_service_pool.py`
- **Client** (2 connections)
- **Task** (1 connections)
- **Get connection from pool. Raises: NATSPublishError: If no connection is…** (1 connections) — `server/services/nats_service_pool.py`
- **Return connection to pool.** (1 connections) — `server/services/nats_service_pool.py`
- **Validate subject when subject manager and validation are enabled.** (1 connections) — `server/services/nats_service_pool.py`
- **Publish message using connection pool for high-throughput scenarios. Args:…** (1 connections) — `server/services/nats_service_pool.py`
- **Add message to batch for efficient bulk publishing. Args: subject: NATS subject…** (1 connections) — `server/services/nats_service_pool.py`
- **Handle batch timeout for low-traffic scenarios.** (1 connections) — `server/services/nats_service_pool.py`
- **Group batched (subject, data) pairs by subject.** (1 connections) — `server/services/nats_service_pool.py`
- **Publish each subject group; return successful subjects and failed groups.** (1 connections) — `server/services/nats_service_pool.py`
- *... and 7 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (3 shared connections)

## Source Files

- `server/services/nats_service_pool.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*