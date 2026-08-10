# Combat Service Bundle

> 161 nodes

## Key Concepts

- **test_nats_service.py** (76 connections) — `server/tests/unit/services/test_nats_service.py`
- **NATSMetrics** (31 connections) — `server/services/nats_metrics.py`
- **NATSConfig** (22 connections) — `server/config/models/nats.py`
- **.__init__()** (5 connections) — `server/infrastructure/nats_broker.py`
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

- [Combat Domain Events](Combat_Domain_Events.md) (18 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (11 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (5 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (3 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (2 shared connections)
- [Combat Monitoring Service](Combat_Monitoring_Service.md) (2 shared connections)
- [Realtime Event Delegation](Realtime_Event_Delegation.md) (2 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (2 shared connections)
- [Multiplayer Browser Helpers](Multiplayer_Browser_Helpers.md) (1 shared connections)
- [Architecture Decisions Adr](Architecture_Decisions_Adr.md) (1 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)
- [Realtime Connection](Realtime_Connection.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/infrastructure/nats_broker.py`
- `server/services/nats_metrics.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 389 (95%)
- INFERRED: 20 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*