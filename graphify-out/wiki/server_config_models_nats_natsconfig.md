# server config models nats natsconfig

> 27 nodes

## Key Concepts

- **NATSConfig** (35 connections) — `server/config/models/nats.py`
- **.__init__()** (6 connections) — `server/services/nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_subject_manager()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_tls_config()** (4 connections) — `server/config/models/nats.py`
- **.validate_tls_files()** (4 connections) — `server/config/models/nats.py`
- **nats_config()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_connection_pool()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_message_batch()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_max_payload()** (3 connections) — `server/config/models/nats.py`
- **.validate_positive()** (3 connections) — `server/config/models/nats.py`
- **field_validator** (3 connections)
- **fixture** (2 connections)
- **Any** (1 connections)
- **BaseSettings** (1 connections)
- **model_validator** (1 connections)
- **NATS messaging configuration.** (1 connections) — `server/config/models/nats.py`
- **Validate TLS file paths exist when TLS is enabled.** (1 connections) — `server/config/models/nats.py`
- **Validate TLS configuration is complete when enabled.** (1 connections) — `server/config/models/nats.py`
- **Validate max payload is reasonable.** (1 connections) — `server/config/models/nats.py`
- **Validate value is positive.** (1 connections) — `server/config/models/nats.py`
- **Initialize NATS service with state machine and connection pooling. Args:…** (1 connections) — `server/services/nats_service.py`
- **Test NATSService initialization with subject manager.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test NATSService initializes connection pool structures.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test NATSService initializes message batching structures.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 2 more nodes in this community*

## Relationships

- [server services nats service natsservice](server_services_nats_service_natsservice.md) (10 shared connections)
- [server services nats exceptions natsrequesterror](server_services_nats_exceptions_natsrequesterror.md) (7 shared connections)
- [server config init](server_config_init.md) (6 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server tests unit infrastructure test](server_tests_unit_infrastructure_test.md) (2 shared connections)
- [server infrastructure message broker](server_infrastructure_message_broker.md) (2 shared connections)
- [server services combat event publisher](server_services_combat_event_publisher.md) (2 shared connections)
- [msg](msg.md) (1 shared connections)
- [server services nats metrics natsmetrics](server_services_nats_metrics_natsmetrics.md) (1 shared connections)
- [server realtime connection state machine](server_realtime_connection_state_machine.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 66 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*