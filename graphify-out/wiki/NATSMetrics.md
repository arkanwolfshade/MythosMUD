# NATSMetrics

> 47 nodes

## Key Concepts

- **NATSMetrics** (31 connections) — `server/services/nats_metrics.py`
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
- **.record_publish()** (2 connections) — `server/services/nats_metrics.py`
- **.record_subscribe()** (2 connections) — `server/services/nats_metrics.py`
- **.record_batch_flush()** (2 connections) — `server/services/nats_metrics.py`
- **.update_connection_health()** (2 connections) — `server/services/nats_metrics.py`
- **.update_pool_utilization()** (2 connections) — `server/services/nats_metrics.py`
- **.record_ack_success()** (2 connections) — `server/services/nats_metrics.py`
- **.record_ack_failure()** (2 connections) — `server/services/nats_metrics.py`
- **.record_nak()** (2 connections) — `server/services/nats_metrics.py`
- **Test NATSMetrics.record_publish() records successful publish.** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 22 more nodes in this community*

## Relationships

- [nats config()](nats_config%28%29.md) (18 shared connections)
- [NATS](NATS.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)

## Source Files

- `server/services/nats_metrics.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 115 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*