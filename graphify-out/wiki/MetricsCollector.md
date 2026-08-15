# MetricsCollector

> 29 nodes

## Key Concepts

- **MetricsCollector** (18 connections) — `server/middleware/metrics_collector.py`
- **test_metrics_collector.py** (7 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
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
- **test_circuit_state_change_trims_history()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_get_summary()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_record_and_get_metrics()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_reset_metrics()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **Any** (2 connections)
- **Record a circuit breaker state change. Args: old_state: Previous circuit state…** (1 connections) — `server/middleware/metrics_collector.py`
- **Record message processing time. Args: duration_ms: Processing duration in…** (1 connections) — `server/middleware/metrics_collector.py`
- **Get current metrics snapshot. Returns: Dictionary containing all metrics AI:…** (1 connections) — `server/middleware/metrics_collector.py`
- **Reset all metrics counters. Useful for clearing metrics after a deployment or…** (1 connections) — `server/middleware/metrics_collector.py`
- **Simple metrics collector for NATS message delivery. Thread-safe metrics…** (1 connections) — `server/middleware/metrics_collector.py`
- **Get concise metrics summary. Returns: High-level metrics summary AI: For quick…** (1 connections) — `server/middleware/metrics_collector.py`
- **Initialize metrics collector. AI: Uses Lock for thread-safety in async context.** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a successfully processed message. Args: channel: Message channel for…** (1 connections) — `server/middleware/metrics_collector.py`
- *... and 4 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [HealthMonitor](HealthMonitor.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/tests/unit/middleware/test_metrics_collector.py`

## Audit Trail

- EXTRACTED: 32 (86%)
- INFERRED: 5 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*