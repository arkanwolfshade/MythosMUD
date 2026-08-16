# NATSServicePoolMixin

> 29 nodes

## Key Concepts

- **NATSServicePoolMixin** (19 connections) — `server/services/nats_service_pool.py`
- **.publish_with_pool()** (8 connections) — `server/services/nats_service_pool.py`
- **._flush_batch()** (6 connections) — `server/services/nats_service_pool.py`
- **._get_connection()** (5 connections) — `server/services/nats_service_pool.py`
- **._initialize_connection_pool()** (5 connections) — `server/services/nats_service_pool.py`
- **.publish_batch()** (5 connections) — `server/services/nats_service_pool.py`
- **._batch_timeout()** (4 connections) — `server/services/nats_service_pool.py`
- **._build_connect_options()** (4 connections) — `server/services/nats_service_pool.py`
- **._configure_tls()** (4 connections) — `server/services/nats_service_pool.py`
- **._create_tracked_task()** (4 connections) — `server/services/nats_service_pool.py`
- **._retry_failed_batch_groups()** (4 connections) — `server/services/nats_service_pool.py`
- **._return_connection()** (4 connections) — `server/services/nats_service_pool.py`
- **.recover_failed_batches()** (3 connections) — `server/services/nats_service_pool.py`
- **._cleanup_connection_pool()** (2 connections) — `server/services/nats_service_pool.py`
- **Task** (1 connections)
- **Implemented on NATSService.** (1 connections) — `server/services/nats_service_pool.py`
- **Build connection options for NATS (primary client and pool).** (1 connections) — `server/services/nats_service_pool.py`
- **Configure TLS settings for NATS connection.** (1 connections) — `server/services/nats_service_pool.py`
- **Initialize connection pool for high-throughput scenarios. AI: Tracks successful…** (1 connections) — `server/services/nats_service_pool.py`
- **Get connection from pool. Raises: NATSPublishError: If no connection is…** (1 connections) — `server/services/nats_service_pool.py`
- **Return connection to pool.** (1 connections) — `server/services/nats_service_pool.py`
- **Publish message using connection pool for high-throughput scenarios. Args:…** (1 connections) — `server/services/nats_service_pool.py`
- **Clean up connection pool during shutdown.** (1 connections) — `server/services/nats_service_pool.py`
- **Add message to batch for efficient bulk publishing. Args: subject: NATS subject…** (1 connections) — `server/services/nats_service_pool.py`
- **Handle batch timeout for low-traffic scenarios.** (1 connections) — `server/services/nats_service_pool.py`
- *... and 4 more nodes in this community*

## Relationships

- [NATSSubjectManager](NATSSubjectManager.md) (5 shared connections)
- [NATSPublishError](NATSPublishError.md) (3 shared connections)
- [Client](Client.md) (2 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [NATSMetrics](NATSMetrics.md) (1 shared connections)

## Source Files

- `server/services/nats_service_pool.py`

## Audit Trail

- EXTRACTED: 49 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*