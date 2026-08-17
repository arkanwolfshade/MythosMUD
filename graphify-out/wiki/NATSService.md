# NATSService

> 184 nodes

## Key Concepts

- **NATSService** (151 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (60 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **NATSConfig** (35 connections) — `server/config/models/nats.py`
- **asyncio** (26 connections)
- **test_nats_service_health.py** (23 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **asyncio** (15 connections)
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **.disconnect()** (8 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (7 connections) — `server/services/nats_service.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **.connect()** (6 connections) — `server/services/nats_service.py`
- **.__init__()** (6 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **_assert_tracked_coro_closed()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_start_health_monitoring_creates_task()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_nats_service_init_with_config()** (6 connections) — `server/tests/unit/services/test_nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_subject_manager()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_error()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_not_found()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_tls_files()** (4 connections) — `server/config/models/nats.py`
- **._handle_error_async()** (4 connections) — `server/services/nats_service.py`
- *... and 159 more nodes in this community*

## Relationships

- [NATSError](NATSError.md) (49 shared connections)
- [JsonMap](JsonMap.md) (9 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (6 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [NATSMetrics](NATSMetrics.md) (3 shared connections)
- [AppConfig](AppConfig.md) (2 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (2 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (2 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/services/test_nats_service_health.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 321 (74%)
- INFERRED: 113 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*