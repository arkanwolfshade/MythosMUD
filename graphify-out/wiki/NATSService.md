# NATSService

> 176 nodes

## Key Concepts

- **NATSService** (155 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (59 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **NATSConfig** (34 connections) — `server/config/models/nats.py`
- **asyncio** (26 connections)
- **test_nats_service_health.py** (23 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **asyncio** (15 connections)
- **._create_tracked_task()** (7 connections) — `server/services/nats_service.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **.connect()** (6 connections) — `server/services/nats_service.py`
- **.__init__()** (6 connections) — `server/services/nats_service.py`
- **_assert_tracked_coro_closed()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_start_health_monitoring_creates_task()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_nats_service_init_with_config()** (6 connections) — `server/tests/unit/services/test_nats_service.py`
- **.disconnect()** (5 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_nats_service_init_with_subject_manager()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_tls_files()** (4 connections) — `server/config/models/nats.py`
- **._cancel_background_tasks()** (4 connections) — `server/services/nats_service.py`
- **._force_cancel_pending_tasks()** (4 connections) — `server/services/nats_service.py`
- **._handle_error_async()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- *... and 151 more nodes in this community*

## Relationships

- [NATSError](NATSError.md) (45 shared connections)
- [NATSPublishError](NATSPublishError.md) (29 shared connections)
- [test_config_models.py](test_config_models.py.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (2 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/services/test_nats_service_health.py`
- `server/tests/unit/services/test_nats_service_helpers.py`
- `server/tests/unit/services/test_nats_service_pool.py`

## Audit Trail

- EXTRACTED: 313 (75%)
- INFERRED: 107 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*