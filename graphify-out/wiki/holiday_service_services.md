# holiday service services

> 47 nodes

## Key Concepts

- **NATSMessageBroker** (31 connections) — `server/infrastructure/nats_broker.py`
- **.publish()** (6 connections) — `server/infrastructure/nats_broker.py`
- **.__init__()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.connect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.disconnect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.is_connected()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.subscribe()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.request()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._start_health_monitoring()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._configure_tls()** (4 connections) — `server/infrastructure/nats_broker.py`
- **.unsubscribe()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._error_callback()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_error_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_reconnect_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._health_check_loop()** (4 connections) — `server/infrastructure/nats_broker.py`
- **test_connect_with_tls_enabled_passes_tls_options()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Any** (3 connections)
- **._disconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._handle_disconnect_async()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._reconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._stop_health_monitoring()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._perform_health_check()** (3 connections) — `server/infrastructure/nats_broker.py`
- **nats_broker()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Exception** (2 connections)
- **test_connect_with_user_password()** (2 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- *... and 22 more nodes in this community*

## Relationships

- [broker infrastructure nats](broker_infrastructure_nats.md) (17 shared connections)
- [combat validator validators](combat_validator_validators.md) (2 shared connections)
- [manager subject services](manager_subject_services.md) (1 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)
- [schemas nats messages](schemas_nats_messages.md) (1 shared connections)
- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (1 shared connections)

## Source Files

- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 141 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*