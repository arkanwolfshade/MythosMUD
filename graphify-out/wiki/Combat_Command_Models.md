# Combat Command Models

> 54 nodes

## Key Concepts

- **NATSMetrics** (31 connections) — `server/services/nats_metrics.py`
- **test_nats_service_init_with_config()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_metrics.py** (4 connections) — `server/services/nats_metrics.py`
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
- **.__init__()** (2 connections) — `server/services/nats_metrics.py`
- **.record_publish()** (2 connections) — `server/services/nats_metrics.py`
- **.record_subscribe()** (2 connections) — `server/services/nats_metrics.py`
- **.record_batch_flush()** (2 connections) — `server/services/nats_metrics.py`
- **.update_connection_health()** (2 connections) — `server/services/nats_metrics.py`
- **.update_pool_utilization()** (2 connections) — `server/services/nats_metrics.py`
- **.record_ack_success()** (2 connections) — `server/services/nats_metrics.py`
- *... and 29 more nodes in this community*

## Relationships

- [Combat Service Bundle](Combat_Service_Bundle.md) (17 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (4 shared connections)
- [Combat Persistence Events](Combat_Persistence_Events.md) (1 shared connections)
- [Architecture Decisions Adr](Architecture_Decisions_Adr.md) (1 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (1 shared connections)

## Source Files

- `server/services/nats_metrics.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 125 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*