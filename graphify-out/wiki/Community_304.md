# Community 304

> 55 nodes

## Key Concepts

- **NATSServicePoolMixin** (26 connections) — `server/services/nats_service_pool.py`
- **NatsConnectOptions** (9 connections) — `server/services/nats_service_connect.py`
- **.publish_with_pool()** (9 connections) — `server/services/nats_service_pool.py`
- **._flush_batch()** (8 connections) — `server/services/nats_service_pool.py`
- **configure_nats_tls()** (6 connections) — `server/services/nats_service_connect.py`
- **nats_connect()** (6 connections) — `server/services/nats_service_connect.py`
- **._initialize_connection_pool()** (6 connections) — `server/services/nats_service_pool.py`
- **.publish_batch()** (6 connections) — `server/services/nats_service_pool.py`
- **._configure_tls()** (5 connections) — `server/services/nats_service_pool.py`
- **._create_pool_connections()** (5 connections) — `server/services/nats_service_pool.py`
- **._get_connection()** (5 connections) — `server/services/nats_service_pool.py`
- **._retry_failed_batch_groups()** (5 connections) — `server/services/nats_service_pool.py`
- **._validate_pool_publish_subject()** (5 connections) — `server/services/nats_service_pool.py`
- **._attempt_retry_batch_groups()** (4 connections) — `server/services/nats_service_pool.py`
- **._batch_timeout()** (4 connections) — `server/services/nats_service_pool.py`
- **._build_connect_options()** (4 connections) — `server/services/nats_service_pool.py`
- **._create_tracked_task()** (4 connections) — `server/services/nats_service_pool.py`
- **._publish_batch_groups()** (4 connections) — `server/services/nats_service_pool.py`
- **._return_connection()** (4 connections) — `server/services/nats_service_pool.py`
- **_NatsConnectFn** (3 connections) — `server/services/nats_service_connect.py`
- **._enqueue_exhausted_batch_groups()** (3 connections) — `server/services/nats_service_pool.py`
- **._finalize_pool_init_status()** (3 connections) — `server/services/nats_service_pool.py`
- **._group_batch_messages()** (3 connections) — `server/services/nats_service_pool.py`
- **._record_batch_flush_metrics()** (3 connections) — `server/services/nats_service_pool.py`
- **.recover_failed_batches()** (3 connections) — `server/services/nats_service_pool.py`
- *... and 30 more nodes in this community*

## Relationships

- [Community 63](Community_63.md) (5 shared connections)
- [Community 69](Community_69.md) (4 shared connections)
- [Community 96](Community_96.md) (4 shared connections)
- [NATS Service Config](NATS_Service_Config.md) (2 shared connections)

## Source Files

- `server/services/nats_service_connect.py`
- `server/services/nats_service_pool.py`

## Audit Trail

- EXTRACTED: 92 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*