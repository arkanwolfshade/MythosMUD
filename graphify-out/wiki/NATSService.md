# NATSService

> 71 nodes

## Key Concepts

- **NATSService** (149 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (59 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **asyncio** (26 connections)
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **_assert_tracked_coro_closed()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_start_health_monitoring_creates_task()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_create_tracked_task_closes_coro_when_create_task_fails()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_initialize_connection_pool_passes_auth_token()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_on_disconnect_creates_tracked_task()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_on_error_closes_coro_when_create_task_fails()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_on_error_creates_tracked_task()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_on_reconnect_creates_tracked_task()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_subscribe_message_handler_bad_json_with_manual_ack()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_unsubscribe_missing_subject_raises()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **.unsubscribe()** (3 connections) — `server/services/nats_service.py`
- **svc()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_acknowledge_message_failure()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_acknowledge_message_success()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_acknowledge_message_without_ack()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_build_connect_options_with_token()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_build_connect_options_with_user_password()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_call_callback_async()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_call_callback_sync()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_cleanup_connection_pool()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- *... and 46 more nodes in this community*

## Relationships

- [test_nats_service.py](test_nats_service.py.md) (46 shared connections)
- [._create_tracked_task](_create_tracked_task.md) (13 shared connections)
- [NATSConfig](NATSConfig.md) (11 shared connections)
- [JsonMap](JsonMap.md) (8 shared connections)
- [.disconnect](disconnect.md) (8 shared connections)
- [CombatInstance](CombatInstance.md) (6 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [NATSPublishError](NATSPublishError.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (1 shared connections)
- [test_unsubscribe_from_subject_not_found](test_unsubscribe_from_subject_not_found.md) (1 shared connections)
- [.initialize](initialize.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 159 (60%)
- INFERRED: 108 (40%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*