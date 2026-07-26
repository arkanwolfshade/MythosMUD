# LogAggregator

> 43 nodes · cohesion 0.08

## Key Concepts

- **LogAggregator** (23 connections) — `server/structured_logging/log_aggregator.py`
- **log_aggregator.py** (13 connections) — `server/structured_logging/log_aggregator.py`
- **LogEntry** (13 connections) — `server/structured_logging/log_aggregator.py`
- **.get_logs()** (9 connections) — `server/structured_logging/log_aggregator.py`
- **.export_logs()** (7 connections) — `server/structured_logging/log_aggregator.py`
- **aggregate_log_entry()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **.add_log_entry()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **.__init__()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **._export_csv()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **._export_json()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_correlation_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.get_error_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.get_user_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.get_warning_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **._update_stats()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **Path** (4 connections)
- **.add_aggregation_callback()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **.get_stats()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **._start_processing_thread()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **Any** (3 connections)
- **._process_logs()** (2 connections) — `server/structured_logging/log_aggregator.py`
- **.shutdown()** (2 connections) — `server/structured_logging/log_aggregator.py`
- **datetime** (2 connections)
- **Log aggregation and centralized collection system for MythosMUD server.  This mo** (1 connections) — `server/structured_logging/log_aggregator.py`
- **Add a log entry to the aggregation system.          Args:             level: Log** (1 connections) — `server/structured_logging/log_aggregator.py`
- *... and 18 more nodes in this community*

## Relationships

- [lifespan.py](lifespan.py.md) (8 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (1 shared connections)

## Source Files

- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 152 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*