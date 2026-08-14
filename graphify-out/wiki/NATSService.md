# NATSService

> 107 nodes

## Key Concepts

- **NATSService** (122 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (57 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **asyncio** (25 connections)
- **NATSUnsubscribeError** (11 connections) — `server/services/nats_exceptions.py`
- **.disconnect()** (10 connections) — `server/services/nats_service.py`
- **.connect()** (8 connections) — `server/services/nats_service.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **_assert_tracked_coro_closed()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_start_health_monitoring_creates_task()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **._build_connect_options()** (4 connections) — `server/services/nats_service.py`
- **._configure_tls()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- **test_create_tracked_task_closes_coro_when_create_task_fails()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_on_disconnect_creates_tracked_task()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_on_error_closes_coro_when_create_task_fails()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_on_error_creates_tracked_task()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_on_reconnect_creates_tracked_task()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_subscribe_message_handler_bad_json_with_manual_ack()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **._cancel_background_tasks()** (3 connections) — `server/services/nats_service.py`
- **._check_connection_allowed()** (3 connections) — `server/services/nats_service.py`
- **._cleanup_connection_pool()** (3 connections) — `server/services/nats_service.py`
- **._close_all_subscriptions()** (3 connections) — `server/services/nats_service.py`
- **._close_nats_connection()** (3 connections) — `server/services/nats_service.py`
- *... and 82 more nodes in this community*

## Relationships

- [Any](Any.md) (28 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (8 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (6 shared connections)
- [NATSConfig](NATSConfig.md) (6 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (3 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [NATSMetrics](NATSMetrics.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 264 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*