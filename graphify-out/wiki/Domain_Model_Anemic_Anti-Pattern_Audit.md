# Domain Model Anemic Anti-Pattern Audit

> 34 nodes · cohesion 0.07

## Key Concepts

- **MetricsCollector** (18 connections) — `server/middleware/metrics_collector.py`
- **Lock** (8 connections)
- **test_metrics_collector.py** (7 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **.get_metrics()** (3 connections) — `server/middleware/metrics_collector.py`
- **.get_summary()** (3 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **.record_circuit_state_change()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_dlq()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_failed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_processed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_retried()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_processing_time()** (2 connections) — `server/middleware/metrics_collector.py`
- **.reset_metrics()** (2 connections) — `server/middleware/metrics_collector.py`
- **Any** (2 connections)
- **test_circuit_state_change_trims_history()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_get_summary()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_record_and_get_metrics()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_reset_metrics()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **Record a circuit breaker state change. Args: old_state: Previous circuit state…** (1 connections) — `server/middleware/metrics_collector.py`
- **Record message processing time. Args: duration_ms: Processing duration in…** (1 connections) — `server/middleware/metrics_collector.py`
- **Get current metrics snapshot. Returns: Dictionary containing all metrics AI:…** (1 connections) — `server/middleware/metrics_collector.py`
- **Reset all metrics counters. Useful for clearing metrics after a deployment or…** (1 connections) — `server/middleware/metrics_collector.py`
- **Simple metrics collector for NATS message delivery. Thread-safe metrics…** (1 connections) — `server/middleware/metrics_collector.py`
- *... and 9 more nodes in this community*

## Relationships

- [Room](Room.md) (3 shared connections)
- [test_metadata.py](test_metadata.py.md) (2 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (1 shared connections)
- [_find_item_in_inventory](_find_item_in_inventory.md) (1 shared connections)
- [EventHandler](EventHandler.md) (1 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/tests/unit/middleware/test_metrics_collector.py`

## Audit Trail

- EXTRACTED: 43 (88%)
- INFERRED: 6 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*