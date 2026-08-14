# NATSConfig

> 18 nodes

## Key Concepts

- **NATSConfig** (23 connections) — `server/config/models/nats.py`
- **.__init__()** (7 connections) — `server/services/nats_service.py`
- **nats_service()** (6 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_tls_files()** (4 connections) — `server/config/models/nats.py`
- **nats_config()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
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
- **Create a NATSConfig instance.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Create a NATSService instance.** (1 connections) — `server/tests/unit/services/test_nats_service.py`

## Relationships

- [NATSService](NATSService.md) (6 shared connections)
- [AppConfig](AppConfig.md) (5 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (3 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (2 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (2 shared connections)
- [nats_broker](nats_broker.md) (1 shared connections)
- [test_nats_broker.py](test_nats_broker.py.md) (1 shared connections)
- [test_config_models.py](test_config_models.py.md) (1 shared connections)
- [NATSMetrics](NATSMetrics.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 42 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*