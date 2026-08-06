# occupants npc commands

> 16 nodes

## Key Concepts

- **NATSConfig** (26 connections) — `server/config/models/nats.py`
- **test_nats_service_init_with_dict()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_none()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_tls_files()** (3 connections) — `server/config/models/nats.py`
- **nats_config()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_max_payload()** (2 connections) — `server/config/models/nats.py`
- **.validate_positive()** (2 connections) — `server/config/models/nats.py`
- **BaseSettings** (1 connections)
- **Any** (1 connections)
- **NATS messaging configuration.** (1 connections) — `server/config/models/nats.py`
- **Validate TLS file paths exist when TLS is enabled.** (1 connections) — `server/config/models/nats.py`
- **Validate max payload is reasonable.** (1 connections) — `server/config/models/nats.py`
- **Validate value is positive.** (1 connections) — `server/config/models/nats.py`
- **Create a NATSConfig instance.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test NATSService initialization with dict config.** (1 connections) — `server/tests/unit/services/test_nats_service.py`
- **Test NATSService initialization with None config.** (1 connections) — `server/tests/unit/services/test_nats_service.py`

## Relationships

- [combat validator validators](combat_validator_validators.md) (6 shared connections)
- [combat commands handler](combat_commands_handler.md) (4 shared connections)
- [broker infrastructure nats](broker_infrastructure_nats.md) (3 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [calendar models rationale](calendar_models_rationale.md) (1 shared connections)
- [manager subject services](manager_subject_services.md) (1 shared connections)
- [connection state machine](connection_state_machine.md) (1 shared connections)
- [target resolution service](target_resolution_service.md) (1 shared connections)
- [holiday service services](holiday_service_services.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 48 (91%)
- INFERRED: 5 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*