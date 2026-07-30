# MapZoneContext

> 24 nodes

## Key Concepts

- **NATSConfig** (22 connections) — `server/config/models/nats.py`
- **.__init__()** (5 connections) — `server/infrastructure/nats_broker.py`
- **test_connect_with_tls_enabled_passes_tls_options()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_nats_service_init_with_dict()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_none()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_tls_files()** (3 connections) — `server/config/models/nats.py`
- **.validate_tls_config()** (3 connections) — `server/config/models/nats.py`
- **nats_config()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **nats_config()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_max_payload()** (2 connections) — `server/config/models/nats.py`
- **.validate_positive()** (2 connections) — `server/config/models/nats.py`
- **BaseSettings** (1 connections)
- **Any** (1 connections)
- **NATS messaging configuration.** (1 connections) — `server/config/models/nats.py`
- **Validate TLS file paths exist when TLS is enabled.** (1 connections) — `server/config/models/nats.py`
- **Validate TLS configuration is complete when enabled.** (1 connections) — `server/config/models/nats.py`
- **Validate max payload is reasonable.** (1 connections) — `server/config/models/nats.py`
- **Validate value is positive.** (1 connections) — `server/config/models/nats.py`
- **Initialize NATS message broker.          Args:             config: NATS configur** (1 connections) — `server/infrastructure/nats_broker.py`
- **Create a NATSConfig instance.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test connect() passes TLS options to nats.connect when tls_enabled=True.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Create a NATSConfig instance.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test NATSService initialization with dict config.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test NATSService initialization with None config.** (1 connections) — `server/tests/unit/services/test_nats_service.py`

## Relationships

- [message broker](message_broker.md) (6 shared connections)
- [world](world.md) (4 shared connections)
- [BaseUserManager](BaseUserManager.md) (4 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [connection state machine](connection_state_machine.md) (1 shared connections)
- [get subject manager dependency()](get_subject_manager_dependency%28%29.md) (1 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 63 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*