# log structured logging

> 58 nodes

## Key Concepts

- **LogAggregator** (34 connections) — `server/structured_logging/log_aggregator.py`
- **log_aggregator.py** (15 connections) — `server/structured_logging/log_aggregator.py`
- **LogEntry** (15 connections) — `server/structured_logging/log_aggregator.py`
- **test_log_aggregator.py** (15 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **.get_logs()** (9 connections) — `server/structured_logging/log_aggregator.py`
- **get_log_aggregator()** (8 connections) — `server/structured_logging/log_aggregator.py`
- **aggregate_log_entry()** (8 connections) — `server/structured_logging/log_aggregator.py`
- **.export_logs()** (7 connections) — `server/structured_logging/log_aggregator.py`
- **.__init__()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **.add_log_entry()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **_flush_queue()** (6 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **._export_json()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **._export_csv()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_error_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.get_warning_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.get_user_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.get_correlation_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **._update_stats()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **Path** (4 connections)
- **test_export_logs_json()** (4 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **Any** (3 connections)
- **.get_stats()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **.add_aggregation_callback()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **._start_processing_thread()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **test_get_logs_after_flush()** (3 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- *... and 33 more nodes in this community*

## Relationships

- [room cache services](room_cache_services.md) (6 shared connections)
- [aggro threat services](aggro_threat_services.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [logging handlers structured](logging_handlers_structured.md) (1 shared connections)
- [metrics memory leak](metrics_memory_leak.md) (1 shared connections)

## Source Files

- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/structured_logging/test_log_aggregator.py`

## Audit Trail

- EXTRACTED: 226 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*