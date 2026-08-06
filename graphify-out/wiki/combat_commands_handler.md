# combat commands handler

> 127 nodes

## Key Concepts

- **test_nats_service.py** (76 connections) — `server/tests/unit/services/test_nats_service.py`
- **NATSMetrics** (31 connections) — `server/services/nats_metrics.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_config()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_metrics.py** (4 connections) — `server/services/nats_metrics.py`
- **test_nats_service_init_with_subject_manager()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **.get_metrics()** (3 connections) — `server/services/nats_metrics.py`
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
- **test_nats_metrics_get_metrics()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_get_metrics_empty_processing_times()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_message_processing_times_maxlen()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_connection_pool()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_message_batch()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_not_found()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 102 more nodes in this community*

## Relationships

- [combat validator validators](combat_validator_validators.md) (10 shared connections)
- [commands communication say](commands_communication_say.md) (7 shared connections)
- [connection state machine](connection_state_machine.md) (6 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (4 shared connections)
- [commands inventory put](commands_inventory_put.md) (4 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)
- [mythos mud mapbuilder](mythos_mud_mapbuilder.md) (1 shared connections)
- [target resolution service](target_resolution_service.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (1 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (1 shared connections)

## Source Files

- `server/services/nats_metrics.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 314 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*