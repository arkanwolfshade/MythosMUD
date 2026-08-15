# NATSService

> 172 nodes

## Key Concepts

- **NATSService** (120 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (57 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **nats_service.py** (26 connections) — `server/services/nats_service.py`
- **asyncio** (25 connections)
- **NATSConfig** (23 connections) — `server/config/models/nats.py`
- **Any** (17 connections)
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **.disconnect()** (10 connections) — `server/services/nats_service.py`
- **.publish_with_pool()** (10 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (9 connections) — `server/services/nats_service.py`
- **.connect()** (8 connections) — `server/services/nats_service.py`
- **._flush_batch()** (7 connections) — `server/services/nats_service.py`
- **.__init__()** (7 connections) — `server/services/nats_service.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **.publish_batch()** (6 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **_assert_tracked_coro_closed()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_start_health_monitoring_creates_task()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **._get_connection()** (5 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **.publish()** (5 connections) — `server/services/nats_service.py`
- **._retry_failed_batch_groups()** (5 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **.validate_tls_files()** (4 connections) — `server/config/models/nats.py`
- **._batch_timeout()** (4 connections) — `server/services/nats_service.py`
- *... and 147 more nodes in this community*

## Relationships

- [test_nats_service.py](test_nats_service.py.md) (21 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (12 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (4 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (3 shared connections)
- [DistributedEventBus](DistributedEventBus.md) (3 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (3 shared connections)
- [test_nats_broker.py](test_nats_broker.py.md) (2 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (2 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 322 (83%)
- INFERRED: 68 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*