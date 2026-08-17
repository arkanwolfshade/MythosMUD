# NATSService

> 67 nodes

## Key Concepts

- **NATSService** (149 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (59 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **asyncio** (26 connections)
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
- **svc()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_acknowledge_message_failure()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_acknowledge_message_success()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_acknowledge_message_without_ack()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_build_connect_options_with_token()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_build_connect_options_with_user_password()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_call_callback_async()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_call_callback_sync()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_cleanup_connection_pool()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_close_all_subscriptions()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_close_nats_connection()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- *... and 42 more nodes in this community*

## Relationships

- [test_nats_service.py](test_nats_service.py.md) (43 shared connections)
- [JsonMap](JsonMap.md) (16 shared connections)
- [._create_tracked_task](_create_tracked_task.md) (13 shared connections)
- [NATSConfig](NATSConfig.md) (11 shared connections)
- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [NATSUnsubscribeError](NATSUnsubscribeError.md) (4 shared connections)
- [._connect_nats](_connect_nats.md) (1 shared connections)
- [event_serialization.py](event_serialization.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [NATSMetrics](NATSMetrics.md) (1 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 150 (59%)
- INFERRED: 105 (41%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*