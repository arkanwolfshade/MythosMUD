# MetricsCollector

> 27 nodes

## Key Concepts

- **MetricsCollector** (18 connections) — `server/middleware/metrics_collector.py`
- **test_metrics_collector.py** (7 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **.get_metrics()** (3 connections) — `server/middleware/metrics_collector.py`
- **.get_summary()** (3 connections) — `server/middleware/metrics_collector.py`
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
- **Record a successfully processed message. Args: channel: Message channel for…** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a failed message. Args: channel: Message channel error_type: Type of…** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a message retry attempt. Args: channel: Message channel attempt: Retry…** (1 connections) — `server/middleware/metrics_collector.py`
- *... and 2 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (2 shared connections)
- [NATSError](NATSError.md) (1 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/tests/unit/middleware/test_metrics_collector.py`

## Audit Trail

- EXTRACTED: 31 (89%)
- INFERRED: 4 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*