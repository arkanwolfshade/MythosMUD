# test_aggro_threat.py

> 109 nodes

## Key Concepts

- **test_nats_service.py** (63 connections) — `server/tests/unit/services/test_nats_service.py`
- **NATSMetrics** (33 connections) — `server/services/nats_metrics.py`
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
- *... and 84 more nodes in this community*

## Relationships

- [PrototypeRegistryError](PrototypeRegistryError.md) (42 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (10 shared connections)
- [ChatModeration](ChatModeration.md) (7 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [RateLimiter](RateLimiter.md) (3 shared connections)
- [test_command_inventory.py](test_command_inventory.py.md) (2 shared connections)
- [server/services/nats_subject_manager/__init__.py](server-services-nats_subject_manager-__init__.py.md) (1 shared connections)
- [chat_service.py](chat_service.py.md) (1 shared connections)
- [test_command_parser_helpers.py](test_command_parser_helpers.py.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 185 (82%)
- INFERRED: 41 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*