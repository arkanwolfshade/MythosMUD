# NATSService

> 144 nodes

## Key Concepts

- **NATSService** (149 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (59 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **NATSConfig** (30 connections) — `server/config/models/nats.py`
- **asyncio** (26 connections)
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **.disconnect()** (8 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (7 connections) — `server/services/nats_service.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **nats_service()** (7 connections) — `server/tests/unit/services/test_nats_service.py`
- **.connect()** (6 connections) — `server/services/nats_service.py`
- **.__init__()** (6 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **_assert_tracked_coro_closed()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_start_health_monitoring_creates_task()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_nats_service_init_with_config()** (6 connections) — `server/tests/unit/services/test_nats_service.py`
- **.__init__()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **test_nats_service_init_with_subject_manager()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_tls_files()** (4 connections) — `server/config/models/nats.py`
- **._handle_error_async()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- **._on_disconnect()** (4 connections) — `server/services/nats_service.py`
- **._on_reconnect()** (4 connections) — `server/services/nats_service.py`
- **test_create_tracked_task_closes_coro_when_create_task_fails()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- *... and 119 more nodes in this community*

## Relationships

- [test_nats_service.py](test_nats_service.py.md) (53 shared connections)
- [NATSMetrics](NATSMetrics.md) (10 shared connections)
- [JsonMap](JsonMap.md) (9 shared connections)
- [test_nats_broker.py](test_nats_broker.py.md) (4 shared connections)
- [NATSError](NATSError.md) (4 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (3 shared connections)
- [NATSPublishError](NATSPublishError.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [AppConfig](AppConfig.md) (2 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/infrastructure/nats_broker.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 259 (70%)
- INFERRED: 113 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*