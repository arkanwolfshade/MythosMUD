# nats config()

> 108 nodes

## Key Concepts

- **test_nats_service.py** (76 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_service.py** (23 connections) — `server/services/nats_service.py`
- **NATSConfig** (22 connections) — `server/config/models/nats.py`
- **NATSUnsubscribeError** (12 connections) — `server/services/nats_exceptions.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (5 connections) — `server/infrastructure/nats_broker.py`
- **test_nats_service_init_with_config()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_metrics.py** (4 connections) — `server/services/nats_metrics.py`
- **test_nats_service_init_with_dict()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_none()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_tls_files()** (3 connections) — `server/config/models/nats.py`
- **.validate_tls_config()** (3 connections) — `server/config/models/nats.py`
- **nats_config()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **nats_config()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_not_initialized()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_no_available_connections()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_connected()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_running()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_not_found()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_not_connected()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_timeout()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test NATSService initialization with NATSConfig.** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_max_payload()** (2 connections) — `server/config/models/nats.py`
- *... and 83 more nodes in this community*

## Relationships

- [NATSMetrics](NATSMetrics.md) (18 shared connections)
- [. init ()](_init_%28%29.md) (16 shared connections)
- [NATS](NATS.md) (15 shared connections)
- [main()](main%28%29.md) (9 shared connections)
- [message broker](message_broker.md) (5 shared connections)
- [connection state machine](connection_state_machine.md) (5 shared connections)
- [get subject manager dependency()](get_subject_manager_dependency%28%29.md) (3 shared connections)
- [init](init.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (2 shared connections)
- [test nats message handler](test_nats_message_handler.md) (1 shared connections)
- [Test unsubscribe from subject() handles](Test_unsubscribe_from_subject%28%29_handles.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/infrastructure/nats_broker.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 303 (93%)
- INFERRED: 23 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*