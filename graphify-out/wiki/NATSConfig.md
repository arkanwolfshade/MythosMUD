# NATSConfig

> 26 nodes

## Key Concepts

- **NATSConfig** (35 connections) — `server/config/models/nats.py`
- **.__init__()** (6 connections) — `server/services/nats_service.py`
- **test_nats_service_init_with_config()** (6 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_subject_manager()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
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
- **NATS messaging configuration.** (1 connections) — `server/config/models/nats.py`
- **Validate TLS file paths exist when TLS is enabled.** (1 connections) — `server/config/models/nats.py`
- **Validate max payload is reasonable.** (1 connections) — `server/config/models/nats.py`
- **Validate value is positive.** (1 connections) — `server/config/models/nats.py`
- **Initialize NATS service with state machine and connection pooling. Args:…** (1 connections) — `server/services/nats_service.py`
- **Test NATSService initialization with NATSConfig.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test NATSService initialization with subject manager.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test NATSService initializes connection pool structures.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test NATSService initializes message batching structures.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Create a NATSConfig instance.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 1 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (11 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_nats_service_health.py](test_nats_service_health.py.md) (3 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (2 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (2 shared connections)
- [AppConfig](AppConfig.md) (2 shared connections)
- [NATSMetrics](NATSMetrics.md) (2 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (2 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)
- [nats_broker](nats_broker.md) (1 shared connections)
- [test_nats_broker.py](test_nats_broker.py.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 66 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*