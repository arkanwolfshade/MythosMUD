# docs nats subject patterns

> 99 nodes

## Key Concepts

- **test_nats_service.py** (56 connections) — `server/tests/unit/services/test_nats_service.py`
- **asyncio** (23 connections)
- **Exception** (8 connections)
- **NATSConfig** (6 connections)
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_circuit_breaker_opens()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_failure()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_state_machine_blocked()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_handles_drain_error()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_error()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_error()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_metrics.py** (5 connections) — `server/services/nats_metrics.py`
- **nats_config()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_success()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_flushes_batch()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_success()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_is_connected_true()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_connection_pool()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_message_batch()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_config()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_subject_manager()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_no_available_connections()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_not_initialized()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_success()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_not_connected()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 74 more nodes in this community*

## Relationships

- [baseexception](baseexception.md) (35 shared connections)
- [server commands magic commands](server_commands_magic_commands.md) (1 shared connections)
- [server config init create config](server_config_init_create_config.md) (1 shared connections)
- [server services nats metrics natsmetrics](server_services_nats_metrics_natsmetrics.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [server realtime connection state machine](server_realtime_connection_state_machine.md) (1 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (1 shared connections)

## Source Files

- `docs/NATS_SUBJECT_PATTERNS.md`
- `server/services/nats_metrics.py`
- `server/services/nats_subject_manager/nats_subject_manager.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 138 (78%)
- INFERRED: 38 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*