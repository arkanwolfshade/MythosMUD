# nats services service

> 161 nodes

## Key Concepts

- **test_nats_service.py** (76 connections) — `server/tests/unit/services/test_nats_service.py`
- **NATSMetrics** (31 connections) — `server/services/nats_metrics.py`
- **NATSConfig** (22 connections) — `server/config/models/nats.py`
- **.__init__()** (7 connections) — `server/services/nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_config()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_metrics.py** (4 connections) — `server/services/nats_metrics.py`
- **test_nats_service_init_with_dict()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_none()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_subject_manager()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_tls_files()** (3 connections) — `server/config/models/nats.py`
- **.validate_tls_config()** (3 connections) — `server/config/models/nats.py`
- **.get_metrics()** (3 connections) — `server/services/nats_metrics.py`
- **nats_config()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_init()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_record_publish_success()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_record_publish_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_record_subscribe_success()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_record_subscribe_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_record_batch_flush_success()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_record_batch_flush_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_update_connection_health()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_update_connection_health_clamped()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_update_pool_utilization()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_update_pool_utilization_clamped()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 136 more nodes in this community*

## Relationships

- [nats exceptions services](nats_exceptions_services.md) (18 shared connections)
- [combat validator validators](combat_validator_validators.md) (11 shared connections)
- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [connection state machine](connection_state_machine.md) (4 shared connections)
- [broker infrastructure nats](broker_infrastructure_nats.md) (3 shared connections)
- [manager subject services](manager_subject_services.md) (3 shared connections)
- [player event handlers](player_event_handlers.md) (2 shared connections)
- [infrastructure nats broker](infrastructure_nats_broker.md) (2 shared connections)
- [message nats handler](message_nats_handler.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 391 (95%)
- INFERRED: 20 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*