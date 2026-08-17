# LogAggregator

> 61 nodes

## Key Concepts

- **LogAggregator** (36 connections) — `server/structured_logging/log_aggregator.py`
- **LogEntry** (17 connections) — `server/structured_logging/log_aggregator.py`
- **test_log_aggregator.py** (17 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **log_aggregator.py** (16 connections) — `server/structured_logging/log_aggregator.py`
- **LogQueryFilter** (11 connections) — `server/structured_logging/log_aggregator.py`
- **.get_logs()** (10 connections) — `server/structured_logging/log_aggregator.py`
- **_entry()** (10 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **get_log_aggregator()** (8 connections) — `server/structured_logging/log_aggregator.py`
- **.export_logs()** (8 connections) — `server/structured_logging/log_aggregator.py`
- **aggregate_log_entry()** (7 connections) — `server/structured_logging/log_aggregator.py`
- **_flush_queue()** (6 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
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
- **test_filter_error_and_warning_logs()** (4 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- *... and 36 more nodes in this community*

## Relationships

- [MonitoringDashboard](MonitoringDashboard.md) (6 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (1 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (1 shared connections)

## Source Files

- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/structured_logging/test_log_aggregator.py`

## Audit Trail

- EXTRACTED: 130 (90%)
- INFERRED: 14 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*