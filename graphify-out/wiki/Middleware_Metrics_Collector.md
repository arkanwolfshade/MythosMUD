# Middleware Metrics Collector

> 23 nodes · cohesion 0.09

## Key Concepts

- **MetricsCollector** (12 connections) — `server/middleware/metrics_collector.py`
- **.get_metrics()** (3 connections) — `server/middleware/metrics_collector.py`
- **.get_summary()** (3 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.record_circuit_state_change()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_dlq()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_failed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_processed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_retried()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_processing_time()** (2 connections) — `server/middleware/metrics_collector.py`
- **.reset_metrics()** (2 connections) — `server/middleware/metrics_collector.py`
- **Any** (2 connections) — `server/middleware/metrics_collector.py`
- **Record a circuit breaker state change.          Args:             old_state: Pre** (1 connections) — `server/middleware/metrics_collector.py`
- **Record message processing time.          Args:             duration_ms: Processi** (1 connections) — `server/middleware/metrics_collector.py`
- **Get current metrics snapshot.          Returns:             Dictionary containin** (1 connections) — `server/middleware/metrics_collector.py`
- **Reset all metrics counters.          Useful for clearing metrics after a deploym** (1 connections) — `server/middleware/metrics_collector.py`
- **Simple metrics collector for NATS message delivery.      Thread-safe metrics col** (1 connections) — `server/middleware/metrics_collector.py`
- **Get concise metrics summary.          Returns:             High-level metrics su** (1 connections) — `server/middleware/metrics_collector.py`
- **Initialize metrics collector.          AI: Uses Lock for thread-safety in async** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a successfully processed message.          Args:             channel: Mes** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a failed message.          Args:             channel: Message channel** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a message retry attempt.          Args:             channel: Message chan** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a message added to dead letter queue.          Args:             channel:** (1 connections) — `server/middleware/metrics_collector.py`

## Relationships

- [[NPC Admin API]] (1 shared connections)
- [[Inventory Service Helpers]] (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`

## Audit Trail

- EXTRACTED: 47 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
