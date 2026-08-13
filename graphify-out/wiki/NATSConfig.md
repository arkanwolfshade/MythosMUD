# NATSConfig

> 21 nodes

## Key Concepts

- **NATSConfig** (19 connections) — `server/config/models/nats.py`
- **.__init__()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.validate_tls_config()** (4 connections) — `server/config/models/nats.py`
- **.validate_tls_files()** (4 connections) — `server/config/models/nats.py`
- **nats_broker()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **nats_config()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
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
- **Initialize NATS message broker. Args: config: NATS configuration…** (1 connections) — `server/infrastructure/nats_broker.py`
- **Create a NATSConfig instance.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Create a NATSMessageBroker instance.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`

## Relationships

- [AppConfig](AppConfig.md) (6 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (3 shared connections)
- [test_nats_broker.py](test_nats_broker.py.md) (3 shared connections)
- [nats_service](nats_service.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 39 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*