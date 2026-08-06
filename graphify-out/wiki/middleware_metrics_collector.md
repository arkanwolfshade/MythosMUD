# middleware metrics collector

> 27 nodes

## Key Concepts

- **MetricsCollector** (18 connections) — `server/middleware/metrics_collector.py`
- **test_metrics_collector.py** (7 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **.get_metrics()** (3 connections) — `server/middleware/metrics_collector.py`
- **.get_summary()** (3 connections) — `server/middleware/metrics_collector.py`
- **.record_message_processed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_failed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_retried()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_dlq()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_circuit_state_change()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_processing_time()** (2 connections) — `server/middleware/metrics_collector.py`
- **Any** (2 connections)
- **.reset_metrics()** (2 connections) — `server/middleware/metrics_collector.py`
- **test_record_and_get_metrics()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_get_summary()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_reset_metrics()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_circuit_state_change_trims_history()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **Simple metrics collector for NATS message delivery.      Thread-safe metrics col** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a successfully processed message.          Args:             channel: Mes** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a failed message.          Args:             channel: Message channel** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a message retry attempt.          Args:             channel: Message chan** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a message added to dead letter queue.          Args:             channel:** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a circuit breaker state change.          Args:             old_state: Pre** (1 connections) — `server/middleware/metrics_collector.py`
- **Record message processing time.          Args:             duration_ms: Processi** (1 connections) — `server/middleware/metrics_collector.py`
- **Get current metrics snapshot.          Returns:             Dictionary containin** (1 connections) — `server/middleware/metrics_collector.py`
- **Reset all metrics counters.          Useful for clearing metrics after a deploym** (1 connections) — `server/middleware/metrics_collector.py`
- *... and 2 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [event connection helpers](event_connection_helpers.md) (1 shared connections)
- [follow game service](follow_game_service.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/tests/unit/middleware/test_metrics_collector.py`

## Audit Trail

- EXTRACTED: 66 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*