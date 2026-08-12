# MetricsCollector

> 28 nodes

## Key Concepts

- **MetricsCollector** (12 connections) — `server/middleware/metrics_collector.py`
- **Lock** (8 connections)
- **.get_metrics()** (3 connections) — `server/middleware/metrics_collector.py`
- **.get_summary()** (3 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **.get_lock()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **.record_circuit_state_change()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_dlq()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_failed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_processed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_retried()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_processing_time()** (2 connections) — `server/middleware/metrics_collector.py`
- **.reset_metrics()** (2 connections) — `server/middleware/metrics_collector.py`
- **Any** (2 connections)
- **Record a circuit breaker state change. Args: old_state: Previous circuit state…** (1 connections) — `server/middleware/metrics_collector.py`
- **Record message processing time. Args: duration_ms: Processing duration in…** (1 connections) — `server/middleware/metrics_collector.py`
- **Get current metrics snapshot. Returns: Dictionary containing all metrics AI:…** (1 connections) — `server/middleware/metrics_collector.py`
- **Reset all metrics counters. Useful for clearing metrics after a deployment or…** (1 connections) — `server/middleware/metrics_collector.py`
- **Simple metrics collector for NATS message delivery. Thread-safe metrics…** (1 connections) — `server/middleware/metrics_collector.py`
- **Get concise metrics summary. Returns: High-level metrics summary AI: For quick…** (1 connections) — `server/middleware/metrics_collector.py`
- **Initialize metrics collector. AI: Uses Lock for thread-safety in async context.** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a successfully processed message. Args: channel: Message channel for…** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a failed message. Args: channel: Message channel error_type: Type of…** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a message retry attempt. Args: channel: Message channel attempt: Retry…** (1 connections) — `server/middleware/metrics_collector.py`
- *... and 3 more nodes in this community*

## Relationships

- [threading.py](threading.py.md) (2 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [test_connection_initialization.py](test_connection_initialization.py.md) (1 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`

## Audit Trail

- EXTRACTED: 56 (88%)
- INFERRED: 8 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*