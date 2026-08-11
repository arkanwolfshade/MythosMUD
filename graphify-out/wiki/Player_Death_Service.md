# Player Death Service

> 20 nodes

## Key Concepts

- **NATSConfig** (22 connections) — `server/config/models/nats.py`
- **.__init__()** (5 connections) — `server/infrastructure/nats_broker.py`
- **test_connect_with_tls_enabled_passes_tls_options()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
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
- **Initialize NATS message broker.          Args:             config: NATS confi** (1 connections) — `server/infrastructure/nats_broker.py`
- **Create a NATSConfig instance.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test connect() passes TLS options to nats.connect when tls_enabled=True.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Create a NATSConfig instance.** (1 connections) — `server/tests/unit/services/test_nats_service.py`

## Relationships

- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (4 shared connections)
- [Realtime Event Delegation](Realtime_Event_Delegation.md) (3 shared connections)
- [Combat Persistence Events](Combat_Persistence_Events.md) (3 shared connections)
- [Combat Monitoring Service](Combat_Monitoring_Service.md) (3 shared connections)
- [Command Parser](Command_Parser.md) (2 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (2 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (1 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (1 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 55 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*