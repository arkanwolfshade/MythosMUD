# server services nats service natsservice

> 67 nodes

## Key Concepts

- **NATSService** (151 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (60 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
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

- [server services nats exceptions natsrequesterror](server_services_nats_exceptions_natsrequesterror.md) (33 shared connections)
- [server services nats service natsservice](server_services_nats_service_natsservice.md) (21 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (17 shared connections)
- [server config models nats natsconfig](server_config_models_nats_natsconfig.md) (10 shared connections)
- [msg](msg.md) (10 shared connections)
- [server events combat events](server_events_combat_events.md) (4 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (3 shared connections)
- [moduletype](moduletype.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (1 shared connections)
- [server services nats metrics natsmetrics](server_services_nats_metrics_natsmetrics.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 166 (64%)
- INFERRED: 92 (36%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*