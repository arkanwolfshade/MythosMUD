# combat commands handler

> 138 nodes

## Key Concepts

- **test_nats_service.py** (76 connections) — `server/tests/unit/services/test_nats_service.py`
- **NATSMetrics** (31 connections) — `server/services/nats_metrics.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_config()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_metrics.py** (4 connections) — `server/services/nats_metrics.py`
- **test_nats_service_init_with_subject_manager()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
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
- **test_nats_metrics_get_metrics()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_get_metrics_empty_processing_times()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_message_processing_times_maxlen()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_connection_pool()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_message_batch()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_not_initialized()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 113 more nodes in this community*

## Relationships

- [combat validator validators](combat_validator_validators.md) (17 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (4 shared connections)
- [skill game service](skill_game_service.md) (4 shared connections)
- [connection state machine](connection_state_machine.md) (3 shared connections)
- [game chat service](game_chat_service.md) (3 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)
- [player event state](player_event_state.md) (1 shared connections)
- [mythos mud mapbuilder](mythos_mud_mapbuilder.md) (1 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (1 shared connections)
- [aggro threat services](aggro_threat_services.md) (1 shared connections)

## Source Files

- `server/services/nats_metrics.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 331 (96%)
- INFERRED: 13 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*