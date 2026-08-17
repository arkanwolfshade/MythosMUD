# NATSMetrics

> 89 nodes

## Key Concepts

- **NATSMetrics** (33 connections) — `server/services/nats_metrics.py`
- **nats_service.py** (33 connections) — `server/services/nats_service.py`
- **nats_service_pool.py** (20 connections) — `server/services/nats_service_pool.py`
- **NATSServicePoolMixin** (19 connections) — `server/services/nats_service_pool.py`
- **.publish_with_pool()** (8 connections) — `server/services/nats_service_pool.py`
- **Client** (7 connections)
- **nats_connect()** (6 connections) — `server/services/nats_service_pool.py`
- **._flush_batch()** (6 connections) — `server/services/nats_service_pool.py`
- **WebSocket** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **WebSocket** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **NatsConnectOptions** (5 connections) — `server/services/nats_service_pool.py`
- **._get_connection()** (5 connections) — `server/services/nats_service_pool.py`
- **._initialize_connection_pool()** (5 connections) — `server/services/nats_service_pool.py`
- **.publish_batch()** (5 connections) — `server/services/nats_service_pool.py`
- **nats_metrics.py** (5 connections) — `server/services/nats_metrics.py`
- **._batch_timeout()** (4 connections) — `server/services/nats_service_pool.py`
- **._build_connect_options()** (4 connections) — `server/services/nats_service_pool.py`
- **._configure_tls()** (4 connections) — `server/services/nats_service_pool.py`
- **._create_tracked_task()** (4 connections) — `server/services/nats_service_pool.py`
- **._retry_failed_batch_groups()** (4 connections) — `server/services/nats_service_pool.py`
- **._return_connection()** (4 connections) — `server/services/nats_service_pool.py`
- **_NatsConnectFn** (3 connections) — `server/services/nats_service_pool.py`
- **.get_metrics()** (3 connections) — `server/services/nats_metrics.py`
- **.__call__()** (3 connections) — `server/services/nats_service_pool.py`
- **.recover_failed_batches()** (3 connections) — `server/services/nats_service_pool.py`
- *... and 64 more nodes in this community*

## Relationships

- [test_nats_service.py](test_nats_service.py.md) (18 shared connections)
- [NATSService](NATSService.md) (10 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [NATSPublishError](NATSPublishError.md) (6 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (5 shared connections)
- [JsonMap](JsonMap.md) (5 shared connections)
- [NATSError](NATSError.md) (3 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (3 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (2 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (2 shared connections)
- [deque](deque.md) (1 shared connections)
- [testing_examples.py](testing_examples.py.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/websocket_integration.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/services/nats_service_pool.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 157 (87%)
- INFERRED: 23 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*