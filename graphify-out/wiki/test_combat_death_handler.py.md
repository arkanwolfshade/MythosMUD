# test_combat_death_handler.py

> 50 nodes · cohesion 0.04

## Key Concepts

- **NATSMetrics** (35 connections) — `server/services/nats_metrics.py`
- **.__init__()** (6 connections) — `server/services/nats_service.py`
- **.get_metrics()** (3 connections) — `server/services/nats_metrics.py`
- **test_nats_metrics_get_metrics()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_get_metrics_empty_processing_times()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_init()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_message_processing_times_maxlen()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_record_batch_flush_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_record_batch_flush_success()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_record_publish_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_record_publish_success()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_record_subscribe_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_record_subscribe_success()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_update_connection_health()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_update_connection_health_clamped()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_update_pool_utilization()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_metrics_update_pool_utilization_clamped()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **.record_ack_failure()** (2 connections) — `server/services/nats_metrics.py`
- **.record_ack_success()** (2 connections) — `server/services/nats_metrics.py`
- **.record_batch_flush()** (2 connections) — `server/services/nats_metrics.py`
- **.record_nak()** (2 connections) — `server/services/nats_metrics.py`
- **.record_publish()** (2 connections) — `server/services/nats_metrics.py`
- **.record_subscribe()** (2 connections) — `server/services/nats_metrics.py`
- **.update_connection_health()** (2 connections) — `server/services/nats_metrics.py`
- **.update_pool_utilization()** (2 connections) — `server/services/nats_metrics.py`
- *... and 25 more nodes in this community*

## Relationships

- [CombatAttackHandler](CombatAttackHandler.md) (18 shared connections)
- [TestRoomDataFixer](TestRoomDataFixer.md) (6 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (1 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (1 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (1 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (1 shared connections)

## Source Files

- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 74 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*