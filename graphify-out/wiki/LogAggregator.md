# LogAggregator

> 67 nodes

## Key Concepts

- **LogAggregator** (37 connections) — `server/structured_logging/log_aggregator.py`
- **log_aggregator.py** (21 connections) — `server/structured_logging/log_aggregator.py`
- **test_log_aggregator.py** (18 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **LogEntry** (17 connections) — `server/structured_logging/log_aggregator.py`
- **LogQueryFilter** (11 connections) — `server/structured_logging/log_aggregator.py`
- **.get_logs()** (10 connections) — `server/structured_logging/log_aggregator.py`
- **_entry()** (10 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **aggregate_log_entry()** (7 connections) — `server/structured_logging/log_aggregator.py`
- **.export_logs()** (7 connections) — `server/structured_logging/log_aggregator.py`
- **_query_filter_from_mapping()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **_flush_queue()** (6 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **log_time_formats.py** (6 connections) — `server/structured_logging/log_time_formats.py`
- **._export_csv()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **._export_json()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_correlation_logs()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_error_logs()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_user_logs()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_warning_logs()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.__init__()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **._log_matches_filter()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **test_export_logs_json()** (5 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **test_get_logs_after_flush()** (5 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **.add_log_entry()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **._update_stats()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **test_aggregate_log_entry_helper()** (4 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- *... and 42 more nodes in this community*

## Relationships

- [lifespan.py](lifespan.py.md) (4 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (2 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (1 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (1 shared connections)

## Source Files

- `server/structured_logging/log_aggregator.py`
- `server/structured_logging/log_time_formats.py`
- `server/tests/unit/structured_logging/test_log_aggregator.py`

## Audit Trail

- EXTRACTED: 155 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*