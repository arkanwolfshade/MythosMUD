# NATSService

> 256 nodes

## Key Concepts

- **NATSService** (165 connections) — `server/services/nats_service.py`
- **test_nats_service.py** (63 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_helpers.py** (60 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **nats_exceptions.py** (38 connections) — `server/services/nats_exceptions.py`
- **nats_service.py** (34 connections) — `server/services/nats_service.py`
- **NATSConfig** (33 connections) — `server/config/models/nats.py`
- **NATSServicePoolMixin** (28 connections) — `server/services/nats_service_pool.py`
- **asyncio** (26 connections)
- **NATSSubscribeError** (23 connections) — `server/services/nats_exceptions.py`
- **asyncio** (23 connections)
- **nats_service_pool.py** (20 connections) — `server/services/nats_service_pool.py`
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **nats_service_connect.py** (11 connections) — `server/services/nats_service_connect.py`
- **NatsConnectOptions** (9 connections) — `server/services/nats_service_connect.py`
- **JsonMap** (9 connections)
- **TestNATSSubscribeError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.disconnect()** (8 connections) — `server/services/nats_service.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **configure_nats_tls()** (6 connections) — `server/services/nats_service_connect.py`
- **nats_connect()** (6 connections) — `server/services/nats_service_connect.py`
- **.connect()** (6 connections) — `server/services/nats_service.py`
- **.__init__()** (6 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **._initialize_connection_pool()** (6 connections) — `server/services/nats_service_pool.py`
- *... and 231 more nodes in this community*

## Relationships

- [NATSPublishError](NATSPublishError.md) (39 shared connections)
- [NATSMetrics](NATSMetrics.md) (22 shared connections)
- [test_nats_service_health.py](test_nats_service_health.py.md) (21 shared connections)
- [.publish_with_pool](publish_with_pool.md) (15 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (10 shared connections)
- [AppConfig](AppConfig.md) (8 shared connections)
- [._create_tracked_task](_create_tracked_task.md) (8 shared connections)
- [NATSError](NATSError.md) (6 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (6 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (5 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/services/nats_service_connect.py`
- `server/services/nats_service_pool.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/services/test_nats_service_health.py`
- `server/tests/unit/services/test_nats_service_helpers.py`
- `server/tests/unit/services/test_nats_service_pool.py`

## Audit Trail

- EXTRACTED: 559 (82%)
- INFERRED: 126 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*