# server services nats exceptions natsrequesterror

> 64 nodes

## Key Concepts

- **test_nats_service.py** (63 connections) — `server/tests/unit/services/test_nats_service.py`
- **asyncio** (23 connections)
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **test_nats_service_init_with_config()** (6 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_no_available_connections()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_not_initialized()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_error()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_not_connected()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_timeout()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_connected()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_running()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_error()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_not_found()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_circuit_breaker_opens()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_failure()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_state_machine_blocked()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_success()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_flushes_batch()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_handles_drain_error()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_success()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_is_connected_true()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_success()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_success()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_success()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 39 more nodes in this community*

## Relationships

- [server services nats service natsservice](server_services_nats_service_natsservice.md) (33 shared connections)
- [server services nats metrics natsmetrics](server_services_nats_metrics_natsmetrics.md) (16 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (13 shared connections)
- [server config models nats natsconfig](server_config_models_nats_natsconfig.md) (7 shared connections)
- [msg](msg.md) (5 shared connections)
- [server realtime connection state machine](server_realtime_connection_state_machine.md) (3 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [server services combat event publisher](server_services_combat_event_publisher.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 136 (78%)
- INFERRED: 39 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*